from rich.console import Console
from rich.table import Table
import pyfiglet

console = Console()

console.print("")
banner = pyfiglet.figlet_format("Comandos", font="cyberlarge")
console.print(banner, style="bright_blue", justify="center")
console.print("""
Stellar es un OS dedicado a termux para mejorar su aburrida apariencia pero también agrega una selección de comandos (scripts) para su uso, estos comandos están orientados al osint y hacking en varias áreas, abajo encontrarás los comandos listados.

Stellar puede ser modificado y clonado, es un proyecto de codigo abierto el cual mejora significativamente la seguridad en tu terminal de termux brindando una capa de anonimato con tor.

[bold cyan]Att: [underline]Keiji821[/underline][/bold cyan]""", justify="center")
console.print("")
console.print("")
console.print("")

table = Table(title="Lista", title_justify="center", title_style="bold green")
table.add_column("[bold green]Comando", style="bold white", no_wrap=False)
table.add_column("[bold green]Descripción", style="bold white")
table.add_column("[bold green]Estado", style="bold white")

table.add_row("Sistema", style="bold green")
table.add_row("• reload", "Recargar el banner", "🟢 Activo")
table.add_row("• ui", "Personaliza el banner y sus colores", "🟢 Activo") 
table.add_row("• uninstall", "Desinstala Stellar", "🟢 Activo")
table.add_row("• update", "Actualiza desde el repositorio de github", "🟢 Activo")
table.add_row("• bash", "Reinicia su sesión de la terminal", "🟢 Activo")

table.add_row("")
table.add_row("Utilidades", style="bold green")

table.add_row("• ia", "Un servicio de ai desde de una API gratuita", "🟡 Dañado")
table.add_row("• ia-image", "Generador de imágenes IA", "🟡 Dañado")
table.add_row("• traductor", "Traducción en tiempo real", "🟢 Activo")
table.add_row("• myip", "Muestra tu ip real", "🟢 Activo")

table.add_row("")
table.add_row("Osint", style="bold green")

table.add_row("• ipinfo", "Obtiene información de una ip", "🟢 Activo") 
table.add_row("• urlinfo", "Analizador de URL", "🟢 Activo")
table.add_row("• userfinder", "Busca un nombre de usuario en diferentes páginas", "🟢 Activo")
table.add_row("• phoneinfo", "Obtiene información de un número de teléfono", "🟢 Activo")
table.add_row("• metadatainfo", "Extrae metadatos de imágenes y documentos", "🟢 Activo")
table.add_row("• emailsearch", "Búsqueda de emails", "🟢 Activo")

table.add_row("")
table.add_row("Osint/Discord", style="bold green")

table.add_row("• userinfo", "Obtiene información apartir de una id", "🟢 Activo")
table.add_row("• serverinfo", "Obtiene información sobre un servidor a partir de su id", "🟢 Activo")
table.add_row("• searchinvites", "Busca invitaciones en páginas ingresando el nombre del servidor", "🟢 Activo")
table.add_row("• inviteinfo", "Obtiene información sobre un enlace de invitación", "🟢 Activo")

table.add_row("")
table.add_row("Osint/Instagram", style="bold green")

table.add_row("• profileinfo", "Obtiene los metadatos del perfil", "🟡 Dañado")

table.add_row("")
table.add_row("Pentesting", style="bold green")

table.add_row("• ddos", "Realiza un ataque ddos mediante la ip y puerto", "🟢 Activo")

console.print(table, style="bright_cyan", justify="center")
console.print("")