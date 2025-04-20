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
modelo = console.input("[bold green]Ingrese el modelo a usar: [/bold green]")
api_key = console.input("[bold green]Ingrese su clave API de kastg: [/bold green]")

api_url = f"https://api.kastg.xyz/api/ai/{modelo}"

def get_image_url(prompt):
    try:
        response = requests.get(f"{api_url}?prompt={prompt}&n_p=(anime, modern, colorful, vibrant, stylized, digital, computer-generated, CGI, Japanese, animation)&style=anime&art_style=digital&ra[...]", headers={"Authorization": f"Bearer {api_key}"})
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "true" and data.get("result"):
            return data["result"][0].get("url", "No disponible")
        else:
            return "No disponible"
    except requests.RequestException as e:
        console.print(f"[bold red]Error al realizar la solicitud: {e}[/bold red]")
        return None

prompt = console.input("[bold green]> [/bold green]")
image_url = get_image_url(prompt)
if image_url:
    console.print("")
    console.print(f"[bold red]URL de la imagen: {image_url}[/bold red]")
    console.print("")
    os.system(f"termux-open {image_url}")
