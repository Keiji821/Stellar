import os
import json
import requests
import urllib.parse
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()
API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"
HISTORIAL_ARCHIVO = 'historial_chat.json'
MAX_CONTEXT_MESSAGES = 5
TIMEOUT = 10

ERROR_MESSAGES = {
    "api_key": "[bold red]Error: Clave de API no configurada.[/bold red]",
    "empty_input": "[bold red]Error: Entrada vacía.[/bold red]",
    "timeout": "[bold red]Error: La solicitud a la API ha excedido el tiempo de espera.[/bold red]",
    "connection": "[bold red]Error de conexión. Verifique su conexión a Internet.[/bold red]",
    "http": "[bold red]Error HTTP: {error}[/bold red]",
    "request": "[bold red]Error en la solicitud: {error}[/bold red]",
    "json_decode": "[bold red]Error: Respuesta no válida de la API.[/bold red]",
    "unexpected": "[bold red]Error inesperado: {error}[/bold red]",
    "no_response": "[bold red]No se pudo obtener una respuesta de la IA.[/bold red]",
    "history_load": "[bold red]Error al cargar el historial: {error}. Se iniciará uno nuevo.[/bold red]",
    "history_save": "[bold red]Error al guardar el historial: {error}[/bold red]"
}

def cargar_historial():
    if os.path.exists(HISTORIAL_ARCHIVO):
        try:
            with open(HISTORIAL_ARCHIVO, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            console.print(ERROR_MESSAGES["history_load"].format(error=e))
    return []

def guardar_en_historial(historial):
    try:
        with open(HISTORIAL_ARCHIVO, 'w', encoding='utf-8') as f:
            json.dump(historial, f, ensure_ascii=False, indent=4)
    except IOError as e:
        console.print(ERROR_MESSAGES["history_save"].format(error=e))

def get_ai_response(user_input, historial):
    if not API_KEY:
        console.print(ERROR_MESSAGES["api_key"])
        return None

    if not user_input.strip():
        console.print(ERROR_MESSAGES["empty_input"])
        return None

    context = historial[-MAX_CONTEXT_MESSAGES:]
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
                return ai_response[0].get("response", ERROR_MESSAGES["no_response"])
            return ERROR_MESSAGES["no_response"]

    except requests.exceptions.Timeout:
        console.print(ERROR_MESSAGES["timeout"])
    except requests.exceptions.ConnectionError:
        console.print(ERROR_MESSAGES["connection"])
    except requests.exceptions.HTTPError as http_err:
        console.print(ERROR_MESSAGES["http"].format(error=http_err))
    except requests.exceptions.RequestException as req_err:
        console.print(ERROR_MESSAGES["request"].format(error=req_err))
    except json.JSONDecodeError:
        console.print(ERROR_MESSAGES["json_decode"])
    except Exception as e:
        console.print(ERROR_MESSAGES["unexpected"].format(error=e))

    return None

def display_response(response):
    console.print("")
    console.print(Markdown(response))
    console.print("\n")

def main():
    console.print(Panel("[bold green]Chat LlaMa IA[/bold green]", title="[code][bold yellow]Bienvenido", title_align="center"))
    historial = cargar_historial()

    while True:
        user_input = Prompt.ask("[bold green]Tú >[/bold green] ", default="")

        if user_input.lower() == "salir":
            console.print("[bold yellow]¡Hasta luego![/bold yellow]")
            break

        ai_response = get_ai_response(user_input, historial)
        if ai_response:
            historial.append({"role": "Usuario", "message": user_input})
            historial.append({"role": "IA", "message": ai_response})
            guardar_en_historial(historial)
            display_response(ai_response)
        else:
            console.print(ERROR_MESSAGES["no_response"])

if __name__ == "__main__":
    main()