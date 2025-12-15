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
            return False, f"Código de estado: {respuesta.status_code}"
        except Exception as e:
            return False, str(e)

    def mostrar_resumen(self, webhooks, mensaje, cantidad, delay, hilos):
        tabla = Table(title="[bold]Resumen de Configuración[/]")
        tabla.add_column("[bold cyan]Parámetro[/]", style="bold cyan")
        tabla.add_column("[bold magenta]Valor[/]", style="bold magenta")

        tabla.add_row("[bold]Webhooks válidos[/]", f"[bold]{len(webhooks)}[/]")
        tabla.add_row("[bold]Mensaje[/]", f"[bold]{mensaje[:50] + '...' if len(mensaje) > 50 else mensaje}[/]")
        tabla.add_row("[bold]Repeticiones[/]", f"[bold]{cantidad}[/]")
        tabla.add_row("[bold]Delay (seg)[/]", f"[bold]{delay}[/]")
        tabla.add_row("[bold]Hilos[/]", f"[bold]{hilos}[/]")

        console.print(Panel.fit(tabla, style="bold blue"))

    def obtener_datos(self):
        console.print(Panel.fit("[bold]Configuración de Webhooks[/]", style="bold green"))
        
        webhooks = []
        while not webhooks:
            urls = Prompt.ask("[bold green]Ingrese URLs de webhooks (separadas por coma)[/]").split(',')
            webhooks = [url.strip() for url in urls if self.validar_webhook(url.strip())]
            if not webhooks:
                console.print("[bold red]No se encontraron webhooks válidos. Intente nuevamente.[/]")

        mensaje = Prompt.ask("[bold green]Mensaje a enviar[/]")
        cantidad = int(Prompt.ask("[bold green]Cantidad de envíos por webhook[/]", default="1"))
        delay = float(Prompt.ask("[bold green]Delay entre envíos (segundos)[/]", default="0.5"))
        hilos = int(Prompt.ask("[bold green]Número de hilos a usar[/]", default="5"))

        username = Prompt.ask("[bold green]Nombre de usuario personalizado (opcional)[/]", default="")
        avatar_url = Prompt.ask("[bold green]URL de avatar personalizado (opcional)[/]", default="")

        payload = {"content": mensaje}
        if username: payload["username"] = username
        if avatar_url: payload["avatar_url"] = avatar_url

        self.mostrar_resumen(webhooks, mensaje, cantidad, delay, hilos)

        if not Prompt.ask("[bold red]¿Confirmar envío? (s/n)[/]", default="s").lower().startswith('s'):
            console.print("[bold red]Operación cancelada[/]")
            exit()

        return webhooks, payload, cantidad, delay, hilos

    def ejecutar_envios(self, webhooks, payload, cantidad, delay, hilos):
        total_tareas = len(webhooks) * cantidad
        console.print(f"\n[bold]Iniciando envío de {total_tareas} mensajes...[/]")

        with Progress() as progreso:
            tarea = progreso.add_task("[bold cyan]Progreso[/]", total=total_tareas)

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
        tabla = Table(title="[bold]Resultados Finales[/]")
        tabla.add_column("[bold cyan]Estadística[/]", style="bold cyan")
        tabla.add_column("[bold magenta]Cantidad[/]", style="bold magenta")

        tabla.add_row("[bold]Envíos exitosos[/]", f"[bold]{self.stats['exitosos']}[/]")
        tabla.add_row("[bold]Envíos fallidos[/]", f"[bold]{self.stats['fallidos']}[/]")
        tabla.add_row("[bold]Rate limits encontrados[/]", f"[bold]{self.stats['rate_limited']}[/]")
        tabla.add_row("[bold]Tasa de éxito[/]", 
                     f"[bold]{(self.stats['exitosos']/sum(self.stats.values()))*100:.2f}%[/]")

        console.print(Panel.fit(tabla, style="bold blue"))
        console.print("[bold green]Proceso completado[/]")

if __name__ == "__main__":
    manager = WebhookManager()
    try:
        webhooks, payload, cantidad, delay, hilos = manager.obtener_datos()
        manager.ejecutar_envios(webhooks, payload, cantidad, delay, hilos)
    except KeyboardInterrupt:
        console.print("\n[bold red]Ejecución interrumpida por el usuario[/]")
    except Exception as e:
        console.print(f"\n[bold red]Error inesperado: {str(e)}[/]")