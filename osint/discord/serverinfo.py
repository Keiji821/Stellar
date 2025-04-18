import requests
import json
from rich.console import Console
from typing import Dict, Any, Optional, List
from datetime import datetime

console = Console(highlight=False)
ERROR_STYLE = "bold red"
SUCCESS_STYLE = "bold green"
INFO_STYLE = "bold blue"
INPUT_STYLE = "bold green"
HEADER_STYLE = "bold cyan"
MEMBER_STYLE = "bold"
STATUS_STYLE = {
    "online": "green",
    "idle": "yellow",
    "dnd": "red",
    "offline": "dim",
    "invisible": "dim",
    "desconocido": "magenta"
}

def get_server_id() -> str:
    return console.input(f"[{INPUT_STYLE}]»[/] [{INPUT_STYLE}]Ingrese el ID del servidor: [/]")

def fetch_widget_data(server_id: str) -> Optional[Dict[str, Any]]:
    widget_url = f"https://discord.com/api/guilds/{server_id}/widget.json"
    
    try:
        with console.status(f"[{INFO_STYLE}]Conectando con Discord...[/]", spinner="dots"):
            response = requests.get(widget_url, timeout=15)
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"\n[{ERROR_STYLE}]✘ Error al conectar con Discord:[/] {e}")
        return None
    except json.JSONDecodeError:
        console.print(f"\n[{ERROR_STYLE}]✘ Error al leer los datos[/]")
        return None

def format_member_name(member: Dict[str, Any]) -> str:
    username = member.get('username', 'Desconocido')
    discriminator = member.get('discriminator', '0000')
    return f"{username}#{discriminator}"

def get_member_status(member: Dict[str, Any]) -> str:
    return member.get('status', 'desconocido').lower()

def display_members(members: List[Dict[str, Any]], limit: int = 150) -> None:
    console.print(f"[{HEADER_STYLE}]┌{'─' * 50}[/]")
    console.print(f"[{HEADER_STYLE}]│[/] [{HEADER_STYLE}]Miembros conectados ({len(members)}):[/]")
    console.print(f"[{HEADER_STYLE}]└{'─' * 50}[/]\n")
    
    for member in members[:limit]:
        name = format_member_name(member)
        status = get_member_status(member)
        status_color = STATUS_STYLE.get(status, "magenta")
        
        console.print(
            f"[{MEMBER_STYLE}]{name.ljust(35)}[/] "
            f"[{status_color}]◉ {status.capitalize()}[/]"
        )

def get_guild_info(server_id: str) -> Dict[str, Any]:
    widget_url = f"https://discord.com/api/guilds/{server_id}/widget.json"
    
    try:
        response = requests.get(widget_url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        return {"Error": "No se pudo conectar al servidor"}
    except json.JSONDecodeError:
        return {"Error": "Widget desactivado o datos incorrectos"}

    if response.status_code != 200:
        return {"Error": f"Error al obtener datos (Código {response.status_code})"}

    return {
        "Nombre del servidor": data.get("name", "Desconocido"),
        "Miembros en línea": len(data.get("members", [])),
        "Canales de voz": [ch["name"] for ch in data.get("channels", [])],
        "Invitación": data.get("instant_invite", "No disponible"),
        "Actualizado": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

def display_guild_info(info: Dict[str, Any]) -> None:
    console.print(f"\n[{HEADER_STYLE}]┌{'─' * 50}[/]")
    console.print(f"[{HEADER_STYLE}]│[/] [{HEADER_STYLE}]Información del servidor[/]")
    console.print(f"[{HEADER_STYLE}]└{'─' * 50}[/]")
    
    if "Error" in info:
        console.print(f"\n[{ERROR_STYLE}]✘ {info['Error']}[/]")
        return
    
    max_key_length = max(len(key) for key in info.keys())
    
    for key, value in info.items():
        key_display = f"{key}:".ljust(max_key_length + 2)
        
        if isinstance(value, list):
            console.print(f"\n[{SUCCESS_STYLE}]{key_display}[/]")
            for item in value:
                console.print(f"  [{INFO_STYLE}]•[/] {item}")
        else:
            console.print(f"[{SUCCESS_STYLE}]{key_display}[/] [{INFO_STYLE}]{value}[/]")

def main() -> None:
    console.print(f"\n[{HEADER_STYLE}] Información de Servidores Discord [/]\n")
    
    server_id = get_server_id()
    widget_data = fetch_widget_data(server_id)

    if widget_data and 'members' in widget_data:
        display_members(widget_data['members'])
    
    guild_info = get_guild_info(server_id)
    display_guild_info(guild_info)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print(f"\n[{ERROR_STYLE}]✘ Operación cancelada[/]")
    except Exception as e:
        console.print(f"\n[{ERROR_STYLE}]✘ Error: {e}[/]")