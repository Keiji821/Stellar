import os
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich import print

console = Console()

def error(mensaje):
    console.print(f"✖ {mensaje}", style="bold white on red")

def exito(mensaje):
    console.print(f"✓ {mensaje}", style="bold white on green")

def pregunta(mensaje):
    console.print(f"? {mensaje}", style="bold yellow")

def informacion(mensaje):
    console.print(f"→ {mensaje}", style="bold cyan")

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
            pregunta(f"Usuario actual: {usuario_actual}")
            if Confirm.ask("¿Reemplazar usuario?", default=False):
                configurar_nuevo_usuario()
            else:
                informacion("Usuario no modificado")
    else:
        error("No tiene un usuario configurado")
        configurar_nuevo_usuario()

def configurar_nuevo_usuario():
    while True:
        nuevo_usuario = Prompt.ask("Ingrese nuevo usuario", default="").strip()
        if not nuevo_usuario:
            error("Nombre vacío no permitido")
            continue
        
        try:
            with open("user.txt", "w") as f:
                f.write(nuevo_usuario)
            exito("Usuario configurado")
            break
        except Exception as e:
            error(f"Error al guardar: {str(e)}")

def configurar_autenticacion():
    if os.path.exists("login_method.txt"):
        with open("login_method.txt", "r") as f:
            metodo_actual = f.read().strip()
        
        if metodo_actual == "no":
            error("No tiene método de desbloqueo")
            configurar_nuevo_metodo()
        else:
            metodo = "Huella digital" if metodo_actual == "termux-fingerprint" else "Desconocido"
            pregunta(f"Método actual: {metodo}")
            if Confirm.ask("¿Reemplazar método?", default=False):
                configurar_nuevo_metodo()
            else:
                informacion("Método no modificado")
    else:
        error("No tiene método de desbloqueo")
        configurar_nuevo_metodo()

def configurar_nuevo_metodo():
    while True:
        print("\n[bold cyan]Opciones:[/bold cyan]")
        print(" [bold green]1) Huella digital[/bold green]")
        print(" [bold green]2) Desactivar protección[/bold green]")
        
        opcion = Prompt.ask("Seleccione [1-2]", choices=["1", "2"], default="1")
        
        if opcion == "1":
            if verificar_termux_api():
                with open("login_method.txt", "w") as f:
                    f.write("termux-fingerprint")
                exito("Huella activada")
                break
            else:
                error("Termux-API no está instalado")
                informacion("Instale con: pkg install termux-api")
        elif opcion == "2":
            with open("login_method.txt", "w") as f:
                f.write("no")
            exito("Protección desactivada")
            break

def menu_principal():
    while True:
        console.clear()
        print(Panel("Configuración de Stellar", style="bold white on blue"))
        
        # Mostrar configuración actual
        if os.path.exists("user.txt"):
            with open("user.txt", "r") as f:
                usuario = f.read().strip()
            print(f"[bold magenta]Usuario:[/bold magenta] [bold white]{usuario}[/bold white]")
        
        if os.path.exists("login_method.txt"):
            with open("login_method.txt", "r") as f:
                metodo = f.read().strip()
            estado = "[bold green]Huella activada" if metodo == "termux-fingerprint" else "[bold yellow]Protección desactivada"
            print(f"[bold magenta]Seguridad:[/bold magenta] {estado}")
        
        print("\n[bold cyan]Menú:[/bold cyan]")
        print(" [bold green]1) Configurar usuario[/bold green]")
        print(" [bold green]2) Configurar seguridad[/bold green]")
        print(" [bold green]3) Probar sistema[/bold green]")
        print(" [bold green]4) Salir[/bold green]")
        
        opcion = Prompt.ask("\nSeleccione opción [1-4]", choices=["1", "2", "3", "4"])
        
        if opcion == "1":
            configurar_usuario()
        elif opcion == "2":
            configurar_autenticacion()
        elif opcion == "3":
            if os.path.exists("login_method.txt"):
                with open("login_method.txt", "r") as f:
                    metodo = f.read().strip()
                if metodo == "termux-fingerprint":
                    print("\n[bold yellow]Probando autenticación...[/bold yellow]")
                    try:
                        subprocess.run(['termux-fingerprint'], check=True)
                        exito("Autenticación exitosa")
                    except subprocess.CalledProcessError:
                        error("Autenticación fallida")
                    Prompt.ask("[bold yellow]Presione Enter para continuar...[/bold yellow]")
                else:
                    error("Método de huella no configurado")
                    time.sleep(1.5)
            else:
                error("No tiene método de autenticación configurado")
                time.sleep(1.5)
        elif opcion == "4":
            print("\n[bold green]Saliendo del sistema...[/bold green]")
            exit(0)

def inicio():
    console.clear()
    print(Panel("Inicio del sistema de Stellar", style="bold white on magenta"))
    
    if not os.path.exists("user.txt"):
        error("No tiene usuario configurado")
        configurar_usuario()
    
    if not os.path.exists("login_method.txt"):
        error("No tiene método de autenticación")
        configurar_autenticacion()
    
    time.sleep(1.2)
    menu_principal()

if __name__ == "__main__":
    inicio()