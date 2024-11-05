from rich.console import Console
from rich.markdown import Markdown

console = Console()

console.print(" ")
MARKDOWN = """
# Comandos de Stellar
"""
console = Console()
md = Markdown(MARKDOWN)
console.print(md)

console.print(" ")
console.print("  PRINCIPALES")
console.print("   reload", ">", "Reinicia su sesion de termux/bash.")

console.print(" ")
console.print("  UTILIDADES")
console.print("   ia", ">", "Un pequeño servicio de inteligencia artificial.")

console.print(" ")
console.print("  OSINT")
console.print("   ipinfo", ">", "Obtiene la información de una ip, ya sea IPV4 o IPV6.")
console.print("   phoneinfo", ">", "Obtiene la información de un numero de teléfono.")
console.print("   urlinfo", ">", "Obtiene información relevante de una url o enlace.")
console.print("   metadatainfo", ">", "Recupera los metadatos de una imagen, archivo o video.")

console.print(" ")
console.print("CTRL + Z", " Esto detendrá cualquier comando o preceso existente.")
console.print(" ")