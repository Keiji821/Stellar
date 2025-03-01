import requests
import json
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
import textwrap
import urllib.parse
import os

console = Console()
API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"
HISTORIAL_ARCHIVO = 'historial_chat.json'
MAX_CONTEXT_MESSAGES = 300
conversation_history = []

def cargar_historial():
    global conversation_history
    if os.path.exists(HISTORIAL_ARCHIVO):
        try:
            with open(HISTORIAL_ARCHIVO, 'r', encoding='utf-8') as f:
                conversation_history = json.load(f)
            console.print("[bold green]Historial de chat cargado exitosamente.[/bold green]")
        except (json.JSONDecodeError, IOError) as e:
            console.print(f"[bold red]Error al cargar el historial: {e}[/bold red]")
            conversation_history = []
    else:
        conversation_history = []
        try:
            with open(HISTORIAL_ARCHIVO, 'w', encoding='utf-8') as f:
                json.dump(conversation_history, f)
            console.print("[bold yellow]No se encontró historial previo. Se ha creado un nuevo archivo de historial.[/bold yellow]")
        except IOError as e:
            console.print(f"[bold red]Error al crear el historial: {e}[/bold red]")

def guardar_en_historial():
    try:
        with open(HISTORIAL_ARCHIVO, 'w', encoding='utf-8') as f:
            json.dump(conversation_history, f, ensure_ascii=False, indent=4)
    except IOError as e:
        console.print(f"[bold red]Error al guardar el historial: {e}[/bold red]")

def get_ai_response(user_input):
    if not API_KEY:
        console.print("[bold red]Error: Clave de API no proporcionada.[/bold red]")
        return None
    if not user_input.strip():
        console.print("[bold red]Error: La entrada del usuario está vacía.[/bold red]")
        return None
    context = conversation_history[-MAX_CONTEXT_MESSAGES:]
    prompt_lines = []
    for interaction in context:
        role = interaction.get("role", "")
        message = interaction.get("message", "")
        prompt_lines.append(f"{role}: {message}")
    prompt_lines.append(f"Usuario: {user_input}")
    prompt = "\n".join(prompt_lines)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://api.kastg.xyz/api/ai/fast-llamaV3-large?key={API_KEY}&prompt={encoded_prompt}"
    try:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True, console=console) as progress:
            progress.add_task(description="Obteniendo respuesta de la IA...", total=None)
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            ai_response = data.get("result", [{}])[0].get("response", "No se recibió respuesta.")
            return ai_response
    except requests.exceptions.Timeout:
        console.print("[bold red]Error: La solicitud a la API ha excedido el tiempo de espera.[/bold red]")
    except requests.exceptions.ConnectionError:
        console.print("[bold red]Error de conexión. Verifique su conexión a Internet.[/bold red]")
    except requests.exceptions.HTTPError as http_err:
        console.print(f"[bold red]Error HTTP: {http_err}[/bold red]")
    except requests.exceptions.RequestException as req_err:
        console.print(f"[bold red]Error en la solicitud: {req_err}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error inesperado: {e}[/bold red]")
    return None

def display_response(response):
    wrapped_response = textwrap.fill(response, width=50)
    table = Table(title="Respuesta de LlaMa IA", title_justify="center", title_style="bold magenta")
    table.add_column("Respuesta", style="white")
    md = Markdown(wrapped_response)
    table.add_row(md)
    console.print(table)
    console.print("\n")

def main():
    console.print(Panel("[bold blue]Chat LlaMa IA[/bold blue]\n[dim]Tu asistente virtual de inteligencia artificial[/dim]", title="Bienvenido", title_align="center"))
    cargar_historial()
    while True:
        user_input = Prompt.ask("[bold green]Tú >[/bold green] ", default="")
        if user_input.lower() == "salir":
            console.print("[bold yellow]¡Hasta luego![/bold yellow]")
            break
        ai_response = get_ai_response(user_input)
        if ai_response:
            conversation_history.append({"role": "Usuario", "message": user_input})
            conversation_history.append({"role": "IA", "message": ai_response})
            guardar_en_historial()
            display_response(ai_response)
        else:
            console.print("[bold red]No se pudo obtener una respuesta de la IA.[/bold red]")

if __name__ == "__main__":
    main()