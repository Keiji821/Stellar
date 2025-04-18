import requests
import json
from rich.console import Console
from typing import Dict, Any, Optional, List

console = Console()
ERROR_STYLE = "bold red"
SUCCESS_STYLE = "bold green"
INFO_STYLE = "bold blue"

def get_server_id() -> str:
    return console.input(f"[{SUCCESS_STYLE}]Ingrese el ID del servidor:[/{SUCCESS_STYLE}] ")

def fetch_widget_data(server_id: str) -> Optional[Dict[str, Any]]:
    widget_url = f"https://discord.com/api/guilds/{server_id}/widget.json"
    
    try:
        response = requests.get(widget_url, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[{ERROR_STYLE}]Error al conectar con Discord: {e}[/{ERROR_STYLE}]")
        return None
    except json.JSONDecodeError:
        console.print(f"[{ERROR_STYLE}]Error al decodificar la respuesta JSON[/{ERROR_STYLE}]")
        return None

def display_members(members: List[Dict[str, Any]], limit: int = 150) -> None:
    for member in members[:limit]:
        username = member.get('username', 'Desconocido')
        discriminator = member.get('discriminator', '0000')
        console.print(f"[{SUCCESS_STYLE}]{username}#{discriminator}[/{SUCCESS_STYLE}]")

def get_guild_info(server_id: str) -> Dict[str, Any]:
    widget_url = f"https://discord.com/api/guilds/{server_id}/widget.json"
    
    try:
        response = requests.get(widget_url, timeout=10)
        data = response.json()
    except requests.exceptions.RequestException:
        return {"Error": "No se pudo conectar al widget"}
    except json.JSONDecodeError:
        return {"Error": "Widget desactivado por el servidor"}

    if response.status_code == 200:
        return {
            "Nombre": data.get("name", "Desconocido"),
            "Miembros_online": len(data.get("members", [])),
            "Canales_voice": [ch["name"] for ch in data.get("channels", [])],
            "URL_invitación": data.get("instant_invite", "No disponible"),
            "Timestamp": data.get("timestamp", "No disponible")
        }
    elif response.status_code == 403:
        return {"Error": "Widget deshabilitado (código 403)"}
    else:
        return {"Error": f"Código HTTP {response.status_code}"}

def main() -> None:
    server_id = get_server_id()
    
    widget_data = fetch_widget_data(server_id)
    
    if widget_data:
        if 'members' in widget_data:
            console.print(f"\n[{INFO_STYLE}]Miembros en línea ({len(widget_data['members'])}):[/{INFO_STYLE}]\n")
            display_members(widget_data['members'])
        else:
            console.print(f"[{ERROR_STYLE}]Widget desactivado o acceso denegado[/{ERROR_STYLE}]")
     console.print(f"\n[{INFO_STYLE}]Información del servidor:[/{INFO_STYLE}]")
    guild_info = get_guild_info(server_id)
    console.print(json.dumps(guild_info, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()