from rich.console import Console
from rich.style import Style

console = Console(style="grey78 on grey23")

commandos = {
    "SISTEMA": [
        ("reload", "Recargar configuración"),
        ("clear", "Limpiar terminal"),
        ("bash", "Reiniciar terminal"),
        ("ui", "Personalizar interfaz")
    ],
    "UTILIDADES": [
        ("ia", "Asistente de IA"),
        ("ia-image", "Generar imágenes IA"),
        ("traductor", "Traducción instantánea"),
        ("myip", "Información de IP")
    ],
    "OSINT": [
        ("ipinfo", "Analizar direcciones IP"),
        ("phoneinfo", "Buscar teléfonos"),
        ("urlinfo", "Analizar enlaces"),
        ("metadatainfo", "Extraer metadatos"),
        ("emailsearch", "Buscar correos"),
        ("userfinder", "Rastrear usuarios")
    ],
    "DISCORD": [
        ("userinfo", "Consultar usuario")
    ]
}

console.print("\nCENTRO DE COMANDOS STELLAR", style="bold", justify="center")
console.print("v3.1.0\n", style="dim", justify="center")

for categoria, items in commandos.items():
    console.print(categoria, style="bold grey93")
    for cmd, desc in items:
        console.print(f"  {cmd:<12} {desc}", style="grey78")
    console.print()

console.print("ATAJOS:", style="bold grey93")
console.print("  CTRL+Z  Detener proceso", style="grey78")
console.print("  CTRL+C  Forzar terminación\n", style="grey78")

console.print("Navegación: TAB ↹ ↑ ↓", style="dim", justify="center")