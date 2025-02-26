import requests
from rich.progress import Progress, SpinnerColumn
from rich.console import Console
import textwrap
from rich.table import Table
from rich.markdown import Markdown

console = Console()

API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"

def get_ai_response(user_input):
    with Progress(SpinnerColumn("dots")) as progress:
        task = progress.add_task("[red]Cargando...")
        try:
            url = f"https://api.kastg.xyz/api/ai/fast-llamaV3-large?key={API_KEY}&prompt={user_input}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()["result"][0]["response"]
        except requests.exceptions.RequestException as e:
            console.print("[bold red] Error: " + str(e) + "[/bold red]")
            return None

def print_ai_response(response):
    wrapped_response = textwrap.fill(response, width=50)
    print(" ")
    table = Table(title="LlaMa IA", title_justify="center", title_style="bold magenta")
    table.add_column("Respuesta", style="bold white", no_wrap=False)

    MARKDOWN = wrapped_response
    md = Markdown(MARKDOWN)
    table.add_row(md)
    console.print(table)
    console.print(" ")

while True:
    user_input = console.input("[bold green]> [/bold green]")
    response = get_ai_response(user_input)
    if response:
        print_ai_response(response)
    else:
        console.print("[bold red]Error[/bold red]")
