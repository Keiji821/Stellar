from rich.console import Console
from rich.table import Table
import pyfiglet

console = Console()

console.print("")
banner = pyfiglet.figlet_format("Comandos", font="cyberlarge")
console.print(banner, style="bold red", justify="center")
console.print("""
Stellar es un OS dedicado a termux para mejorar su aburrida apariencia pero también agrega una selección de comandos (scripts) para su uso, estos comandos están orientados al osint y hacking en varias áreas, abajo encontrarás los comandos listados.""", justify="center")
console.print("")
console.print("")
console.print("")

table = Table(title="Lista", title_justify="center", title_style="bold green")
table.add_column("[bold green]Comando", style="code", no_wrap=False)
table.add_column("[bold green]Descripción", style="code")

table.add_row("[code]Sistema[code]", style="bold green")

table.add_row("• reload", "Recargar el banner")
table.add_row ("• ui", "Personaliza el banner y sus colores") 
table.add_row("• uninstall", "Desinstala Stellar")
table.add_row("• update", "Actualiza desde el repositorio de github")
table.add_row("• bash", "Reinicia su sesión de la terminal")

table.add_row("")
table.add_row("[code]Utilidades[code]", style="bold green")

table.add_row("• ia", "Un servicio de ai desde de una API gratuita")
table.add_row("• ia-image", "Generador de imágenes IA")
table.add_row("• traductor", "Traducción en tiempo real")
table.add_row("• myip", "Muestra tu ip real")

table.add_row("")
table.add_row("[code]Osint[code]", style="bold green")

table.add_row("• ipinfo", "Obtiene información de una ip") 
table.add_row("• urlinfo", "Analizador de URL")
table.add_row("• userfinder", "Busca un nombre de usuario en diferentes páginas")
table.add_row("• phoneinfo", "Obtiene información de un número de teléfono") 
table.add_row("• emailsearch", "Búsqueda de emails")

table.add_row("")
table.add_row("[code]Osint/Discord[code]", style="bold green")

table.add_row("• userinfo", "Obtiene información apartir de una id")
table.add_row("• serverinfo", "Obtiene información sobre un servidor a partir de su id")
table.add_row("• searchinvites", "Busca invitaciones en páginas ingresando el nombre del servidor")
table.add_row("• inviteinfo", "Obtiene información sobre un enlace de invitación")

table.add_row("")
table.add_row("[code]Pentesting[code]", style="bold green")

table.add_row("• ddos", "Realiza un ataque ddos mediante la ip y puerto")

console.print(table)
console.print("")
