import os
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED
from rich import print as rprint

console = Console()

def error(mensaje):
    console.print(f"[bold red]✖[/bold red] [white]{mensaje}[/white]")

def exito(mensaje):
    console.print(f"[bold green]✓[/bold green] [white]{mensaje}[/white]")

def pregunta(mensaje):
    console.print(f"[bold yellow]?[/bold yellow] [white]{mensaje}[/white]")

def informacion(mensaje):
    console.print(f"[bold cyan]→[/bold cyan] [white]{mensaje}[/white]")

def verificar_termux_api():
    try:
        result = subprocess.run(['pkg', 'list-installed'], 
                               capture_output=True, text=True, check=True)
        return 'termux-api' in result.stdout
    except subprocess.CalledProcessError:
        return False

def configurar_usuario():
    if os.path.exists("user.txt"):
        with open("user.txt", "r") as f:
            usuario_actual = f.read().strip()

        if usuario_actual == "Stellar":
            error("No tiene un usuario configurado")
            configurar_nuevo_usuario()
        else:
            pregunta(f"Usuario actual: [bold magenta]{usuario_actual}[/bold magenta]")
            if Confirm.ask("[yellow]¿Reemplazar usuario?[/yellow]", default=False):
                configurar_nuevo_usuario()
            else:
                informacion("Usuario no modificado")
    else:
        error("No tiene un usuario configurado")
        configurar_nuevo_usuario()

def configurar_nuevo_usuario():
    while True:
        nuevo_usuario = Prompt.ask("[cyan]Ingrese nuevo usuario[/cyan]", default="").strip()
        if not nuevo_usuario:
            error("Nombre vacío no permitido")
            continue

        try:
            with open("user.txt", "w") as f:
                f.write(nuevo_usuario)
            exito(f"Usuario [bold]{nuevo_usuario}[/bold] configurado correctamente")
            break
        except Exception as e:
            error(f"Error al guardar: {str(e)}")

def configurar_autenticacion():
    if os.path.exists("login_method.txt"):
        with open("login_method.txt", "r") as f:
            metodo_actual = f.read().strip()

        if metodo_actual == "no":
            error("No tiene método de desbloqueo configurado")
            configurar_nuevo_metodo()
        else:
            metodo = "Huella digital" if metodo_actual == "termux-fingerprint" else "Desconocido"
            pregunta(f"Método actual: [bold magenta]{metodo}[/bold magenta]")
            if Confirm.ask("[yellow]¿Reemplazar método?[/yellow]", default=False):
                configurar_nuevo_metodo()
            else:
                informacion("Método no modificado")
    else:
        error("No tiene método de desbloqueo configurado")
        configurar_nuevo_metodo()

def configurar_nuevo_metodo():
    while True:
        table = Table(box=ROUNDED, show_header=False)
        table.add_column("Opciones", style="cyan")
        table.add_row("[bold green]1)[/bold green] Huella digital")
        table.add_row("[bold green]2)[/bold green] Desactivar protección")
        console.print(table)

        opcion = Prompt.ask("[cyan]Seleccione [1-2][/cyan]", choices=["1", "2"], default="1")

        if opcion == "1":
            if verificar_termux_api():
                with open("login_method.txt", "w") as f:
                    f.write("termux-fingerprint")
                exito("Autenticación por huella digital activada")
                break
            else:
                error("Termux-API no está instalado")
                informacion("Instale con: [bold]pkg install termux-api[/bold]")
        elif opcion == "2":
            with open("login_method.txt", "w") as f:
                f.write("no")
            exito("Protección desactivada")
            break

def mostrar_encabezado():
    rprint(Panel.fit(
        "[bold white]Configuración de Stellar[/bold white]",
        style="bold white on blue",
        subtitle="[yellow]Sistema de autenticación[/yellow]"
    ))

def mostrar_estado_actual():
    estado_table = Table(box=None, show_header=False, show_edge=False)
    estado_table.add_column("", style="magenta", width=15)
    estado_table.add_column("", style="white")

    if os.path.exists("user.txt"):
        with open("user.txt", "r") as f:
            usuario = f.read().strip()
        estado_table.add_row("Usuario:", f"[bold]{usuario}[/bold]")

    if os.path.exists("login_method.txt"):
        with open("login_method.txt", "r") as f:
            metodo = f.read().strip()
        estado = "[bold green]Huella activada" if metodo == "termux-fingerprint" else "[bold yellow]Protección desactivada"
        estado_table.add_row("Seguridad:", estado)

    console.print(estado_table)

def menu_principal():
    while True:
        mostrar_encabezado()
        mostrar_estado_actual()

        menu_table = Table(box=ROUNDED, show_header=False)
        menu_table.add_column("Opciones", style="cyan")
        menu_table.add_row("[bold green]1)[/bold green] Configurar usuario")
        menu_table.add_row("[bold green]2)[/bold green] Configurar seguridad")
        menu_table.add_row("[bold green]3)[/bold green] Probar sistema")
        menu_table.add_row("[bold green]4)[/bold green] Salir")
        console.print(menu_table)

        opcion = Prompt.ask("[cyan]Seleccione opción [1-4][/cyan]", choices=["1", "2", "3", "4"])

        if opcion == "1":
            configurar_usuario()
        elif opcion == "2":
            configurar_autenticacion()
        elif opcion == "3":
            if os.path.exists("login_method.txt"):
                with open("login_method.txt", "r") as f:
                    metodo = f.read().strip()
                if metodo == "termux-fingerprint":
                    rprint("\n[bold yellow]Probando autenticación...[/bold yellow]")
                    try:
                        subprocess.run(['termux-fingerprint'], check=True)
                        exito("Autenticación exitosa")
                    except subprocess.CalledProcessError:
                        error("Autenticación fallida")
                    Prompt.ask("[yellow]Presione Enter para continuar...[/yellow]")
                else:
                    error("Método de huella no configurado")
                    time.sleep(1.5)
            else:
                error("No tiene método de autenticación configurado")
                time.sleep(1.5)
        elif opcion == "4":
            rprint("\n[bold green]Saliendo del sistema...[/bold green]")
            exit(0)

def inicio():
    rprint(Panel.fit(
        "[bold white]Inicio del sistema de Stellar[/bold white]",
        style="bold white on magenta",
        subtitle="[yellow]Bienvenido[/yellow]"
    ))

    if not os.path.exists("user.txt"):
        error("No tiene usuario configurado")
        configurar_usuario()

    if not os.path.exists("login_method.txt"):
        error("No tiene método de autenticación configurado")
        configurar_autenticacion()

    time.sleep(1.2)
    menu_principal()

if __name__ == "__main__":
    inicio()