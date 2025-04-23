from rich.console import Console
import pyfiglet

console = Console()

console.print("")
banner = pyfiglet.figlet_format("Comandos", font="doom")
console.print(banner, style="bold red", justify="center")
console.print("""
Stellar es un OS dedicado a termux para mejorar su aburrida apariencia pero también agrega una selección de comandos (scripts) para su uso, estos comandos están orientados al osint y hacking en varias áreas, abajo encontrarás los comandos listados.""", justify="center")
console.print("")
console.print("")
console.print("")
console.print("[code]Sistema[code]", style="bold green")
console.print("""
• reload > Recargar el banner
• ui > Personaliza el banner y sus colores 
• uninstall > Desinstala Stellar
• update > Actualiza desde el repositorio de github
• bash > Reinicia su sesión de la terminal""", style="bold cyan")

console.print("")
console.print("[code]Utilidades[code]", style="bold green")
console.print("""
• ia > Un servicio de ai desde de una API gratuita 
• ia-image > Generador de imágenes IA
• traductor > Traducción en tiempo real
• myip > Muestra tu ip real""", style="bold cyan")

console.print("")
console.print("[code]Osint[code]", style="bold green")
console.print("""
• ipinfo > Obtiene información de una ip 
• urlinfo > Analizador de URL
• userfinder > Busca un nombre de usuario en diferentes páginas 
• phoneinfo > Obtiene información de un número de teléfono 
• emailsearch > Búsqueda de emails""", style="bold cyan")

console.print("")
console.print("[code]Osint/Discord[code]", style="bold green")
console.print("""
• userinfo > Obtiene información apartir de una id
• serverinfo > Obtiene información sobre un servidor a partir de su id
• searchinvites > Busca invitaciones en páginas ingresando el nombre del servidor
• inviteinfo > Obtiene información sobre un enlace de invitación""", style="bold cyan")

console.print("")
console.print("[code]Pentesting[code]", style="bold green")
console.print("""
• ddos > Realiza un ataque ddos mediante la ip y puerto""", style="bold cyan")
console.print("")
