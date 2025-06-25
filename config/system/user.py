from rich.console import Console
import os
from os import system
from rich.table import Table

console = Console()

# Sistema

with open("user.txt", encoding="utf-8") as f:
    user = f.read().strip()

with open("password.txt", encoding="utf-8") as f:
    password = f.read().strip()

with open("login_method.txt", encoding="utf-8") as f:
    login_method = f.read().strip()

# Ruta

os.chdir(os.path.expanduser("~/Stellar/config/themes"))

# Temas

with open("banner_color.txt", encoding="utf-8") as f:
    banner_color = f.read().strip()

with open("banner_background.txt", encoding="utf-8") as f:
    banner_background = f.read().strip()

with open("banner_background_color.txt", encoding="utf-8") as f:
    banner_background_color = f.read().strip()

# Usuario 

if user=="Stellar":
    while True:
        response_user = console.input("No tiene un usuario configurado\n¿Desea configurarlo? (y/n): ", style="bold green")
        if response_user=="y":
            response_user_config = console.input("Ingrese un nombre de usuario: ", style="bold green")
            if not response_user_config:
                console.print("Error: No se puede dejar en blanco. Intente de nuevo.", style="bold red")
                continue
            else:
                os.system(f"echo {response_user_config} > user.txt")
                console.print("Usuario configurado correctamente", style="bold green")

# Bloqueo
if login_method="":
    while True:
        login_method_response = console.input("No tiene un método de bloqueo para su Termux\n¿Desea configurar uno? (y/n): ", style="bold green")
        if login_method_response=="":
            login_method_response_list = console.input("Métodos disponibles: Huella dactilar\nSeleccione un método de bloqueo: ", style="bold green")
            if not login_method_response_list:
                console.print("Error: No puede quedar vacío, Intente de nuevo.", style="bold green")
                continúe
            else:
                os.system(f"echo {login_method_response_list} > login_method.txt")
                console.print("Su método de desbloqueo ha sido correctamente configurado", style"bold green")

            
console.print("")
table = Table(title="Perfil", title_justify="center", title_style="bold green")
table.add_column(f"[bold green] Información", style="code", no_wrap=False)
table.add_column("[bold green] Descripción", style="code")

table.add_row("General", style="bold green")
table.add_row("")
table.add_row("Usuario", user)
table.add_row("")
table.add_row("Preferencias", style="bold green")
table.add_row("")
table.add_row("Color del banner", banner_color)
table.add_row("Fondo del banner", banner_background)
table.add_row("Color del fondo del banner", banner_background_color)

console.print(table, style="bright_white", justify="center")
console.print("")

