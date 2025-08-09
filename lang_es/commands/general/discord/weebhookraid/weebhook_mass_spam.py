import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.prompt import Prompt
from rich.table import Table
from rich.style import Style
from fake_useragent import UserAgent

console = Console()
user_agent = UserAgent()

class WebhookManager:
    def __init__(self):
        self.stats = {
            'exitosos': 0,
            'fallidos': 0,
            'rate_limited': 0
        }
        self.session = requests.Session()

    def validar_webhook(self, url):
        return url.strip().startswith((
            "https://discord.com/api/webhooks/",
            "http://discord.com/api/webhooks/",
            "https://canary.discord.com/api/webhooks/",
            "https://ptb.discord.com/api/webhooks/"
        ))

    def enviar_mensaje(self, webhook, payload):
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': user_agent.random
        }

        try:
            respuesta = self.session.post(
                webhook,
                json=payload,
                headers=headers,
                timeout=10
            )

            if respuesta.status_code == 204:
                return True, None
            elif respuesta.status_code == 429:
                retry_after = respuesta.json().get('retry_after', 1)
                time.sleep(retry_after)
                return self.enviar_mensaje(webhook, payload)
            return False, f"Codigo de estado: {respuesta.status_code}"
        except Exception as e:
            return False, str(e)

    def mostrar_resumen(self, webhooks, mensaje, cantidad, delay, hilos):
        tabla = Table(title="Resumen de Configuracion")
        tabla.add_column("Parametro", style="cyan")
        tabla.add_column("Valor", style="magenta")

        tabla.add_row("Webhooks validos", str(len(webhooks)))
        tabla.add_row("Mensaje", mensaje[:50] + "..." if len(mensaje) > 50 else mensaje)
        tabla.add_row("Repeticiones", str(cantidad))
        tabla.add_row("Delay (seg)", str(delay))
        tabla.add_row("Hilos", str(hilos))

        console.print(Panel.fit(tabla))

    def obtener_datos(self):
        console.print(Panel.fit("Configuracion de Webhooks"))
        
        webhooks = []
        while not webhooks:
            urls = Prompt.ask("Ingrese URLs de webhooks (separadas por coma)").split(',')
            webhooks = [url.strip() for url in urls if self.validar_webhook(url.strip())]
            if not webhooks:
                console.print("No se encontraron webhooks validos. Intente nuevamente.", style="red")

        mensaje = Prompt.ask("Mensaje a enviar")
        cantidad = int(Prompt.ask("Cantidad de envios por webhook", default="1"))
        delay = float(Prompt.ask("Delay entre envios (segundos)", default="0.5"))
        hilos = int(Prompt.ask("Numero de hilos a usar", default="5"))

        username = Prompt.ask("Nombre de usuario personalizado (opcional)", default="")
        avatar_url = Prompt.ask("URL de avatar personalizado (opcional)", default="")

        payload = {"content": mensaje}
        if username: payload["username"] = username
        if avatar_url: payload["avatar_url"] = avatar_url

        self.mostrar_resumen(webhooks, mensaje, cantidad, delay, hilos)

        if not Prompt.ask("Confirmar envio? (s/n)", default="s").lower().startswith('s'):
            console.print("Operacion cancelada", style="red")
            exit()

        return webhooks, payload, cantidad, delay, hilos

    def ejecutar_envios(self, webhooks, payload, cantidad, delay, hilos):
        total_tareas = len(webhooks) * cantidad
        console.print(f"\nIniciando envio de {total_tareas} mensajes...")

        with Progress() as progreso:
            tarea = progreso.add_task("Progreso", total=total_tareas)

            with ThreadPoolExecutor(max_workers=hilos) as executor:
                futuros = []
                for webhook in webhooks:
                    for _ in range(cantidad):
                        futuros.append(executor.submit(self.enviar_mensaje, webhook, payload))
                        time.sleep(delay)

                for futuro in as_completed(futuros):
                    exito, error = futuro.result()
                    if exito:
                        self.stats['exitosos'] += 1
                    else:
                        self.stats['fallidos'] += 1
                        if "rate limit" in str(error).lower():
                            self.stats['rate_limited'] += 1

                    progreso.update(tarea, advance=1)

        self.mostrar_resultados()

    def mostrar_resultados(self):
        tabla = Table(title="Resultados Finales")
        tabla.add_column("Estadistica", style="cyan")
        tabla.add_column("Cantidad", style="magenta")

        tabla.add_row("Envios exitosos", str(self.stats['exitosos']))
        tabla.add_row("Envios fallidos", str(self.stats['fallidos']))
        tabla.add_row("Rate limits encontrados", str(self.stats['rate_limited']))
        tabla.add_row("Tasa de exito", 
                     f"{(self.stats['exitosos']/sum(self.stats.values()))*100:.2f}%")

        console.print(Panel.fit(tabla))
        console.print("Proceso completado", style="green")

if __name__ == "__main__":
    manager = WebhookManager()
    try:
        webhooks, payload, cantidad, delay, hilos = manager.obtener_datos()
        manager.ejecutar_envios(webhooks, payload, cantidad, delay, hilos)
    except KeyboardInterrupt:
        console.print("\nEjecucion interrumpida por el usuario", style="red")
    except Exception as e:
        console.print(f"\nError inesperado: {str(e)}", style="red")