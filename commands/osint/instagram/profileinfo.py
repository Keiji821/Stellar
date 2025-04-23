from instagramy import InstagramUser
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_profile_info(username, session_id=None):
    try:
        user = InstagramUser(username, sessionid=session_id if session_id else None)
        
        profile_info = {
            "👤 Usuario": f"[bold cyan]{user.username}[/]",
            "📛 Nombre completo": user.full_name,
            "📜 Biografía": f"[italic]{user.biography}[/]",
            "📈 Seguidores": f"[bold]{user.number_of_followers:,}[/]",
            "📉 Siguiendo": f"{user.number_of_followings:,}",
            "🖼️ Publicaciones": f"{user.number_of_posts:,}",
            "✅ Verificado": "[green]Sí[/]" if user.is_verified else "[red]No[/]",
            "🔒 Privado": "[green]Sí[/]" if user.is_private else "[red]No[/]",
            "🏢 Cuenta Negocio": "[green]Sí[/]" if user.is_business_account else "[red]No[/]",
            "🌐 URL externa": user.external_url if user.external_url else "[grey]N/A[/]",
            "📅 Recién unido": "[green]Sí[/]" if user.joined_recently else "[red]No[/]",
            "🖼️ Foto perfil": user.profile_picture_url,
            "📱 Publicaciones destacadas": user.highlight_reel_count,
            "📹 Videos IGTV": user.igtv_video_count,
            "📰 Historias activas": user.has_active_story,
            "📊 Tasa de engagement": f"{round((user.average_engagement * 100), 2)}%",
            "🔗 Facebook conectado": user.connected_fb_page if user.connected_fb_page else "[grey]N/A[/]",
            "🏷️ Categoría": user.business_category_name if user.business_category_name else "[grey]N/A[/]",
            "📧 Correo empresarial": user.business_email if user.business_email else "[grey]N/A[/]",
            "📞 Teléfono empresarial": user.business_phone_number if user.business_phone_number else "[grey]N/A[/]"
        }
        
        return profile_info
    
    except Exception as e:
        return f"[bold red]Error: {str(e)}[/]"

session_id = console.input("[bold green]Ingresa tu Session ID (opcional): [/]")
username = console.input("[bold green]Ingresa el usuario de Instagram: [/]")

info = get_profile_info(username, session_id)

if isinstance(info, dict):
    console.print(Panel.fit(f"[bold]Información de @{username}[/]", style="blue"))
    for key, value in info.items():
        console.print(f"[bold yellow]{key}:[/] {value}", justify="left")
else:
    console.print(Panel.fit(info, style="red", title="Error"))