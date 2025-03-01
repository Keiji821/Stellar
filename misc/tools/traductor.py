import requests
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from urllib.parse import quote

console = Console()

API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"

def translate(text, target_language):
    if not text or not target_language:
        console.print("[bold red]Error:[/bold red] El texto y el idioma objetivo no pueden estar vacíos.")
        return None

    encoded_text = quote(text)
    url = f"https://api.kastg.xyz/api/tool/translate?input={encoded_text}&to={target_language}&from=auto"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "true" and data.get("result"):
                return data["result"][0].get("output")
        console.print(f"[bold red]Error:[/bold red] No se pudo obtener la traducción.")
        return None
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error en la solicitud:[/bold red] {e}")
        return None

def display_translation(original, translated):
    original_panel = Panel(
        Text(original, style="bold white"),
        title="[bold magenta]Texto Original[/bold magenta]",
        border_style="blue",
        width=50,
        padding=(1, 2),
        expand=False)
    
    translated_panel = Panel(
        Text(translated, style="bold green"),
        title="[bold magenta]Texto Traducido[/bold magenta]",
        border_style="green",
        width=50,
        padding=(1, 2),
        expand=False)
    
    console.print(original_panel)
    console.print(translated_panel)

if __name__ == "__main__":
    text_to_translate = input("Introduce el texto a traducir: ")
    target_language = input("Introduce el idioma al que deseas traducir (ej. 'fr' para francés): ")
    
    translated_text = translate(text_to_translate, target_language)
    
    if translated_text:
        display_translation(text_to_translate, translated_text)
    else:
        console.print("[bold red]No se pudo obtener la traducción.[/bold red]")