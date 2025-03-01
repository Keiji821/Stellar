from rich.console import Console
import requests
import os

console = Console()

console.print("")
console.print("""
• AIIG >> aiig
• PixArt Sigma >> pixart-sigma
• Playground >> playground
• Prodia >> prodia
• Leonardo >> leonardo
• AnimeDiff >> animediff
• Blue Pencil >> blue-pencil
""")
console.print("")
Modelo = console.input("[bold green]Ingrese el modelo a usar: [/bold green]")

API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"
API_URL = f"https://api.kastg.xyz/api/ai/{Modelo}"

def get_image_url(prompt):
    try:
        response = requests.get(f"{API_URL}?prompt={prompt}&n_p=(anime, modern, colorful, vibrant, stylized, digital, computer-generated, CGI, Japanese, animation)&style=anime&art_style=digital&ratio=square&key={API_KEY}")
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "true" and data.get("result"):
            return data["result"][0].get("url", "No disponible")
        else:
            return "No disponible"
    except requests.RequestException as e:
        console.print(f"[bold red]Error al realizar la solicitud: [bold red]{e}")
        return None

prompt = console.input("[bold green]> [bold green]")
image_url = get_image_url(prompt)
if image_url:
    console.print("")
    console.print(f"[bold red]URL de la imagen: [bold red]{image_url}")
    console.print("")
    os.system(f"termux-open {image_url}")