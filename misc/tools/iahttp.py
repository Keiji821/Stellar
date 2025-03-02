import os
import json
import requests
import textwrap
import urllib.parse
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()
API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"
HISTORIAL_ARCHIVO = 'historial_chat.json'
MAX_CONTEXT_MESSAGES = 5  # Reduce el número de mensajes de contexto
TIMEOUT = 10

def cargar_historial():
    if os.path.exists(HISTORIAL_ARCHIVO):
        try:
            with open(HISTORIAL_ARCHIVO, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            console.print("[bold red]Error al cargar el historial. Se iniciará uno nuevo.[/bold red]")
    return []

def guardar_en_historial(historial):
    try:
        with open(HISTORIAL_ARCHIVO, 'w', encoding='utf-8') as f:
            json.dump(historial, f, ensure_ascii=False, indent=4)
    except IOError as e:
        console.print(f"[bold red]Error al guardar el historial: {e}[/bold red]")

conversation_history = cargar_historial()

def get_ai_response(user_input):
    if not API_KEY:
        console.print("[bold red]Error: Clave de API no configurada.[/bold red]")
        return None

    if not user_input.strip():
        console.print("[bold red]Error: Entrada vacía.[/bold red]")
        return None

    context = conversation_history[-MAX_CONTEXT_MESSAGES:]
    prompt_lines = [f"{entry['role']}: {entry['message']}" for entry in context]
    prompt_lines.append(f"Usuario: {user_input}")
    prompt = "\n".join(prompt_lines)

    encoded_prompt = urllib.parse.quote(prompt[:2000])  # Limitar la longitud del prompt
    url = f"https://api.kastg.xyz/api/ai/fast-llamaV3-large?key={API_KEY}&prompt={encoded_prompt}"

    try:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True, console=console) as progress:
            progress.add_task(description="Obteniendo respuesta de la IA...", total=None)
            response = requests.get(url, timeout=TIMEOUT)
            response.raise_for_status()

            data = response.json()
            ai_response = data.get("result", [{}])

            if isinstance(ai_response, list) and ai_response:
                return ai_response[0].get("response", "No se recibió respuesta.")
            return "No se recibió respuesta."

    except requests.exceptions.Timeout:
        console.print("[bold red]Error: La solicitud a la API ha excedido el tiempo de espera.[/bold red]")
    except requests.exceptions.ConnectionError:
        console.print("[bold red]Error de conexión. Verifique su conexión a Internet.[/bold red]")
    except requests.exceptions.HTTPError as http_err:
        console.print(f"[bold red]Error HTTP: {http_err}[/bold red]")
    except requests.exceptions.RequestException as req_err:
        console.print(f"[bold red]Error en la solicitud: {req_err}[/bold red]")
    except json.JSONDecodeError:
        console.print("[bold red]Error: Respuesta no válida de la API.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error inesperado: {e}[/bold red]")

    return None

def display_response(response):
    console.print("")
    console.print(Markdown(response))    
    console.print("\n")

def main():
    console.print(Panel("[bold green]Chat LlaMa IA[/bold green]", title="[code][bold yellow]Bienvenido", title_align="center"))

    while True:
        user_input = Prompt.ask("[bold green]Tú >[/bold green] ", default="")

        if user_input.lower() == "salir":
            console.print("[bold yellow]¡Hasta luego![/bold yellow]")
            break

        ai_response = get_ai_response(user_input)
        if ai_response:
            conversation_history.append({"role": "Usuario", "message": user_input})
            conversation_history.append({"role": "IA", "message": ai_response})
            guardar_en_historial(conversation_history)
            display_response(ai_response)
        else:
            console.print("[bold red]No se pudo obtener una respuesta de la IA.[/bold red]")

if __name__ == "__main__":
    main()