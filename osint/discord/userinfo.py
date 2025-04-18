import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

console = Console()

def formatear_fecha(fecha_str):
    try:
        fecha = datetime.fromisoformat(fecha_str.replace('Z', '+00:00'))
        return fecha.strftime("%d/%m/%Y a las %H:%M:%S")
    except:
        return fecha_str

def mostrar_insignias(insignias):
    if not insignias:
        return "Ninguna"
    return ", ".join(insignia.replace("_", " ").title() for insignia in insignias)

def obtener_info_usuario():
    try:
        id_usuario = console.input("[bold green]» Ingrese el ID de usuario: [/]")
        
        with console.status("[bold blue]Buscando información...[/]", spinner="dots"):
            respuesta = requests.get(
                f"https://discordlookup.mesalytic.moe/v1/user/{id_usuario}",
                timeout=10
            )
            
            if respuesta.status_code == 404:
                console.print("[bold red]✘ Usuario no encontrado[/]")
                return
            elif respuesta.status_code != 200:
                console.print(f"[bold red]✘ Error {respuesta.status_code}[/]")
                return

            datos = respuesta.json()

        tabla = Table(show_header=False, box=None)
        tabla.add_column(style="bold green", width=20)
        tabla.add_column(style="blue")

        tabla.add_row("Usuario", datos.get("username", "Desconocido"))
        tabla.add_row("Nombre global", datos.get("global_name", "N/A"))
        tabla.add_row("ID", datos.get("id", "N/A"))
        tabla.add_row("Creación", formatear_fecha(datos.get("created_at", "N/A")))
        
        avatar = datos.get("avatar", {})
        tabla.add_row("Avatar", avatar.get("link", "N/A"))
        tabla.add_row("Animado", "Sí" if avatar.get("is_animated", False) else "No")
        
        tabla.add_row("Insignias", mostrar_insignias(datos.get("badges")))

        console.print(Panel.fit(
            tabla,
            title="[bold cyan]Información del Usuario[/]",
            border_style="cyan",
            padding=(1, 4)
        ))

    except requests.exceptions.RequestException:
        console.print("[bold red]✘ Error de conexión[/]")
    except:
        console.print("[bold red]✘ Error inesperado[/]")

if __name__ == "__main__":
    console.print("\n[bold cyan]Buscador de Usuarios de Discord[/]\n")
    obtener_info_usuario()