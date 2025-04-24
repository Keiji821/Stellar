from rich.console import Console
from rich.table import Table
import pyfiglet

console = Console()

console.print("")
banner = pyfiglet.figlet_format("Comandos", font="cyberlarge")
console.print(banner, style="bright_red", justify="center")
console.print("""
Stellar es un OS dedicado a termux para mejorar su aburrida apariencia pero también agrega una selección de comandos (scripts) para su uso, estos comandos están orientados al osint y hacking en varias áreas, abajo encontrarás los comandos listados.

Stellar puede ser modificado y clonado, es un proyecto de codigo abierto el cual mejora significativamente la seguridad en tu terminal de termux brindando una capa de anonimato con tor.

[bold cyan]Att: [underline]Keiji821[/underline][/bold cyan]""", justify="center")
console.print("")
console.print("")
console.print("")

table = Table(title="Lista", title_justify="center", title_style="bold green")
table.add_column("[bold yellow]Comando", style="bold red", no_wrap=False)
table.add_column("[bold yellow]Descripción", style="code")

table.add_row("[code]Sistema[code]", style="bold white")

table.add_row("[code]• reload", "Recargar el banner")
table.add_row("[code]• ui", "Personaliza el banner y sus colores") 
table.add_row("[code]• uninstall", "Desinstala Stellar")
table.add_row("[code]• update", "Actualiza desde el repositorio de github")
table.add_row("[code]• bash", "Reinicia su sesión de la terminal")

table.add_row("")
table.add_row("[code]Utilidades[code]", style="bold white")

table.add_row("[code]• ia", "Un servicio de ai desde de una API gratuita")
table.add_row("[code]• ia-image", "Generador de imágenes IA")
table.add_row("[code]• traductor", "Traducción en tiempo real")
table.add_row("[code]• myip", "Muestra tu ip real")

table.add_row("")
table.add_row("[code]Osint[code]", style="bold white")

table.add_row("[code]• ipinfo", "Obtiene información de una ip") 
table.add_row("[code]• urlinfo", "Analizador de URL")
table.add_row("[code]• userfinder", "Busca un nombre de usuario en diferentes páginas")
table.add_row("[code]• phoneinfo", "Obtiene información de un número de teléfono") 
table.add_row("[code]• emailsearch", "Búsqueda de emails")

table.add_row("")
table.add_row("[code]Osint/Discord[code]", style="bold white")

table.add_row("[code]• userinfo", "Obtiene información apartir de una id")
table.add_row("[code]• serverinfo", "Obtiene información sobre un servidor a partir de su id")
table.add_row("[code]• searchinvites", "Busca invitaciones en páginas ingresando el nombre del servidor")
table.add_row("[code]• inviteinfo", "Obtiene información sobre un enlace de invitación")

table.add_row("")
table.add_row("[code]Pentesting[code]", style="bold white")

table.add_row("[code]• ddos", "Realiza un ataque ddos mediante la ip y puerto")

console.print(table, justify="center")
console.print("")
