import random
import string
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns

console = Console()

def generar_contraseña_nuclear(longitud=64):
    caracteres = (
        string.ascii_uppercase + 
        string.ascii_lowercase + 
        string.digits + 
        "!@#$%&*?¡¿[]{}<>~^+-_=()"
    )
    return ''.join(random.SystemRandom().choice(caracteres) for _ in range(longitud))

def crear_panel_contraseña(contraseña):
    estilo = random.choice(["red", "green", "yellow", "cyan", "magenta"])
    return Panel(
        Text(contraseña, justify="center", style=f"bold {estilo}"),
        border_style=estilo,
        box=random.choice([box.DOUBLE, box.ROUNDED, box.SQUARE]),
        padding=(0, 2)
    )

def main():
    console.print("\n")
    
    contraseñas = [generar_contraseña_nuclear() for _ in range(5)]
    paneles = [crear_panel_contraseña(pwd) for pwd in contraseñas]
    
    console.print(
        Columns(paneles, expand=True, equal=True),
        justify="center"
    )
    
    console.print(
        Panel.fit(
            "⚠️ [bold white on red] NUNCA COMPARTAS ESTAS CONTRASEÑAS [/] ⚠️",
            border_style="red",
            box=box.HEAVY
        ),
        justify="center"
    )

if __name__ == "__main__":
    main()