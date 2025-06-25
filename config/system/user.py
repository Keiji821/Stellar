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

# Configuración de usuario
if user == "Stellar":
    while True:
        response_user = console.input("[bold green]No tiene un usuario configurado\n¿Desea configurarlo? (y/n): [/bold green]")
        
        if response_user.lower() == "y":
            while True:
                response_user_config = console.input("[bold green]Ingrese un nombre de usuario: [/bold green]").strip()
                
                if not response_user_config:
                    console.print("Error: No se puede dejar en blanco. Intente de nuevo.", style="bold red")
                    continue
                
                try:
                    with open("user.txt", "w") as f:
                        f.write(response_user_config)
                    console.print("✓ Usuario configurado correctamente", style="bold green")
                    break
                except Exception as e:
                    console.print(f"Error al guardar: {str(e)}", style="bold red")
                    continue
            break
            
        elif response_user.lower() == "n":
            break
            
        else:
            console.print("Error: Opción no válida. Por favor ingrese 'y' o 'n'.", style="bold red")

# Configuración de método de bloqueo
if login_method == "":
    while True:
        login_method_response = console.input("[bold green]No tiene un método de bloqueo\n¿Desea configurar uno? (y/n): [/bold green]").lower()
        
        if login_method_response == "y":
            while True:
                console.print("[bold]Métodos disponibles:[/bold]\n1. Huella dactilar", style="green")
                login_method_response_list = console.input("[bold green]Seleccione un método: [/bold green]").strip()
                
                if login_method_response_list == "1":
                    method = "termux-fingerprint"
                    break
                else:
                    console.print("Error: Opción no válida. Intente nuevamente.", style="bold red")
                    continue
            
            try:
                with open("login_method.txt", "w") as f:
                    f.write(method)
                console.print("✓ Método de desbloqueo configurado correctamente", style="bold green")
                break
            except Exception as e:
                console.print(f"Error al guardar: {str(e)}", style="bold red")
                continue
                
        elif login_method_response == "n":
            break
            
        else:
            console.print("Error: Opción no válida. Por favor ingrese 'y' o 'n'.", style="bold red")

            
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

