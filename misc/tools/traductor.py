import requests
from rich.console import Console
from rich.table import Table

console = Console()

API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"

def translate(text, target_language):
    url = f"https://api.kastg.xyz/api/tool/translate?input={text}&to={target_language}&from=auto"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    console.print(f"Sending request to: {url}")  # Debug: URL being requested
    response = requests.get(url, headers=headers)
    console.print(f"Response status code: {response.status_code}")  # Debug: Response status code
    console.print(f"Response content: {response.content}")  # Debug: Response content
    if response.status_code == 200:
        return response.json().get("translatedText")
    else:
        console.print(f"Error: {response.status_code}")
        return None

def display_translation(original, translated):
    table = Table(title="Traductor", title_justify="center", title_style="bold magenta")
    table.add_column("Original", style="bold white", no_wrap=False)
    table.add_column("Traducido", style="bold white", no_wrap=False)
    table.add_row(original, translated)
    console.print(table)

if __name__ == "__main__":
    text_to_translate = input("Introduce el texto a traducir: ")
    target_language = input("Introduce el idioma al que deseas traducir (ej. 'fr' para francés): ")
    translated_text = translate(text_to_translate, target_language)
    if translated_text:
        display_translation(text_to_translate, translated_text)
    else:
        console.print("No se pudo obtener la traducción.")