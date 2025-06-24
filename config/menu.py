from rich.console import Console
from rich.table import Table
import pyfiglet

console = Console()

console.print("")
banner = pyfiglet.figlet_format("Comandos", font="standard")
console.print(banner, style="bright_blue", justify="center")

console.print("")

table = Table(title="Lista", title_justify="center", title_style="bold green")
table.add_column("[bold green]Comando", style="code", no_wrap=False)
table.add_column("[bold green]Descripción", style="code", no_wrap=False)
table.add_column("[bold green]Estado", style="code", no_wrap=False)

table.add_row("[code]Sistema", style="bold green")
table.add_row("")
table.add_row("• reload", "Recargar el banner", "🟢 Activo")
table.add_row("• ui", "Personaliza el banner y sus colores", "🟢 Activo") 
table.add_row("• uninstall", "Desinstala Stellar", "🟢 Activo")
table.add_row("• update", "Actualiza desde el repositorio de github", "🟢 Activo")
table.add_row("• bash", "Reinicia su sesión de la terminal", "🟢 Activo")
table.add_row("• history -c", "Elimina cache de comandos en la terminal", "🟢 Activo")
table.add_row("• reset", "Reestablece la terminal", "🟢 Activo")
table.add_row("• userconf", "Configura tu usuario de Stellar", "🟢 Activo")
table.add_row("• my", "Visualiza tu perfil de Stellar", "🟢 Activo")

table.add_row("")
table.add_row("[code]Utilidades", style="bold green")
table.add_row("")
table.add_row("• ia", "Un servicio de IA desde de una API gratuita", "🟢 Activo")
table.add_row("• ia-image", "Generador de imágenes IA", "🔴 Dañado")
table.add_row("• traductor", "Traducción en tiempo real", "🟢 Activo")
table.add_row("• myip", "Muestra tu IP real", "🟢 Activo")
table.add_row("• passwordgen", "Genera contraseñas seguras para usar", "🟢 Activo")
table.add_row("• encrypt-file", "Encripta archivos", "🟢 Activo")

table.add_row("")
table.add_row("[code]Discord", style="bold green")
table.add_row("")
table.add_row("• webhook-mass-spam", "Envia mensajes a un canal de forma masiva", "🟢 Activo")
table.add_row("• mass-delete-channels", "Elimina de forma masiva canales", "🔴 Dañado")

table.add_row("")
table.add_row("[code]Osint", style="bold green")
table.add_row("")
table.add_row("• ipinfo", "Obtiene información de una IP", "🟢 Activo") 
table.add_row("• urlinfo", "Analizador de URL", "🟢 Activo")
table.add_row("• userfinder", "Busca un nombre de usuario en el internet", "🟢 Activo")
table.add_row("• phoneinfo", "Obtiene información de un número de teléfono", "🟢 Activo")
table.add_row("• metadatainfo", "Extrae metadatos de imágenes y documentos", "🟢 Activo")
table.add_row("• emailsearch", "Búsqueda de emails", "🟢 Activo")

table.add_row("")
table.add_row("[code]Osint/Discord", style="bold green")
table.add_row("")
table.add_row("• userinfo", "Obtiene información apartir de una ID", "🟢 Activo")
table.add_row("• serverinfo", "Obtiene información sobre un servidor", "🟢 Activo")
table.add_row("• searchinvites", "Busca enlaces de invitación", "🟢 Activo")
table.add_row("• inviteinfo", "Obtiene datos sobre un enlace de invitación", "🟢 Activo")
table.add_row("• role-mapper", "Mapea roles apartir del ID del servidor", "🟢 Activo")
table.add_row("• mutual-servers", "Verifica si hay un servidor común entre usuarios", "🟢 Activo")

table.add_row("")
table.add_row("[code]Osint/Instagram", style="bold green")
table.add_row("")
table.add_row("• profileinfo", "Obtiene los metadatos del perfil", "🔴 Dañado")

table.add_row("")
table.add_row("[code]Phishing", style="bold green")
table.add_row("")
table.add_row("• tunnel", "Expone una imagen que captura la IP", "🔴 Dañado")

table.add_row("")
table.add_row("[code]Pentesting", style="bold green")
table.add_row("")
table.add_row("• ddos", "Realiza un ataque DDOS mediante la IP y puerto", "🟢 Activo")

console.print(table, style="bright_white", justify="center")
console.print("")