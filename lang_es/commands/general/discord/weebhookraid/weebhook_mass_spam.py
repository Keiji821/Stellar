import requests
import time
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def send_discord_message():
    webhooks_input = Prompt.ask("Ingrese URLs de webhooks (separadas por coma)")
    webhooks = [url.strip() for url in webhooks_input.split(",") if url.strip()]
    
    valid_webhooks = []
    for url in webhooks:
        if url.startswith("https://discord.com/api/webhooks/"):
            valid_webhooks.append(url)
        else:
            console.print(f"✗ URL inválida omitida: {url[:50]}...")
    
    if not valid_webhooks:
        console.print("✗ No hay webhooks válidos para enviar")
        return
        
    message = Prompt.ask("Mensaje a enviar")
    
    try:
        count = int(Prompt.ask("Cantidad de veces a enviar", default="1"))
        delay = float(Prompt.ask("Retraso entre envíos (segundos)", default="1.0"))
        username = Prompt.ask("Nombre de usuario personalizado (opcional)", default="")
        avatar_url = Prompt.ask("URL de avatar personalizado (opcional)", default="")
    except ValueError:
        count = 1
        delay = 1.0
    
    total_messages = len(valid_webhooks) * count
    console.print(f"\nResumen:")
    console.print(f"- Webhooks: {len(valid_webhooks)}")
    console.print(f"- Mensajes por webhook: {count}")
    console.print(f"- Mensajes totales: {total_messages}")
    console.print(f"- Retraso: {delay} segundos")
    
    if not Prompt.ask("\n¿Confirmar envío? (s/n)").lower().startswith('s'):
        console.print("✗ Envío cancelado")
        return
    
    console.print("\nINICIANDO ENVÍO...")
    
    for i, webhook in enumerate(valid_webhooks):
        console.print(f"\nWebhook {i+1}/{len(valid_webhooks)}: {webhook[:50]}...")
        
        for j in range(count):
            payload = {
                "content": message,
                "username": username if username else None,
                "avatar_url": avatar_url if avatar_url else None
            }
            
            try:
                response = requests.post(webhook, json=payload)
                
                if response.status_code == 204:
                    console.print(f"✓ Mensaje {j+1}/{count} enviado")
                else:
                    console.print(f"✗ Error ({response.status_code}): {response.text}")
                
                if j < count - 1:
                    time.sleep(delay)
                    
            except Exception as e:
                console.print(f"✗ Error de conexión: {str(e)}")
    
    console.print("\n¡ENVÍO COMPLETADO!")

if __name__ == "__main__":
    send_discord_message()
