import requests
from rich.console import Console
from rich.table import Table

console = Console()

API_KEY = ""

def translate(text, target_language):
    url = f"https://api.kastg.xyz/api/tool/translate?input={text}&to={target_language}&from=auto"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
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
    text_to_translate = "Hello World! This is the output in French"
    translated_text = translate(text_to_translate, "fr")
    if translated_text:
        display_translation(text_to_translate, translated_text)