from rich.console import Console

console = Console()

console.print("[code]Sistema[code]", style="bold green", justify="center")
console.print("""
• reload > Recargar el banner
• ui > Personaliza el banner y sus colores 
• uninstall > Desinstala Stellar
• update > Actualiza desde el repositorio de github
• bash > Reinicia su sesión de la terminal""")


console.print("""
• ia > Un servicio de ai desde de una API gratuita 
• ia-image > Generador de imágenes IA
• traductor > Traducción en tiempo real
• myip > Muestra tu ip real""")


console.print("""• ipinfo > Obtiene información de una ip 
• urlinfo > Analizador de URL
• userfinder > Busca un nombre de usuario en diferentes páginas 
• phoneinfo > Obtiene información de un número de teléfono 
• emailsearch > Búsqueda de emails""")


console.print("""• userinfo > Obtiene información apartir de una id
• serverinfo > Obtiene información sobre un servidor a partir de su id
• searchinvites > Busca invitaciones en páginas ingresando el nombre del servidor
• inviteinfo > Obtiene información sobre un enlace de invitación""")


console.print("""
• ddos > Realiza un ataque ddos mediante la ip y puerto""")
