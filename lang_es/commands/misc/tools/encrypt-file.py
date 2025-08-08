import os
import sys
import getpass
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

class FileEncryptor:
    def __init__(self):
        self.iterations = 1048576
        self.salt_length = 32
        self.key_length = 32
        self.nonce_length = 12
        self.tag_length = 16
        self.max_file_size = 1073741824

    def _derive_key(self, password, salt=None):
        salt = salt if salt is not None else get_random_bytes(self.salt_length)
        key = scrypt(
            password=password.encode('utf-8'),
            salt=salt,
            key_len=self.key_length,
            N=self.iterations,
            r=8,
            p=1
        )
        return key, salt

    def encrypt_file(self, input_path, password):
        try:
            if not os.path.isfile(input_path):
                return False, f"El archivo {input_path} no existe"

            file_size = os.path.getsize(input_path)
            if file_size > self.max_file_size:
                return False, f"Archivo demasiado grande (máximo {self.max_file_size//1024//1024}MB)"

            with open(input_path, 'rb') as f:
                plaintext = f.read()

            key, salt = self._derive_key(password)
            cipher = AES.new(key, AES.MODE_GCM)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext)

            output_path = input_path + '.enc'
            with open(output_path, 'wb') as f:
                f.write(salt)
                f.write(cipher.nonce)
                f.write(tag)
                f.write(ciphertext)

            os.remove(input_path)
            return True, output_path

        except Exception as e:
            return False, f"Error al cifrar: {str(e)}"

    def decrypt_file(self, input_path, password):
        try:
            if not os.path.isfile(input_path):
                return False, f"El archivo {input_path} no existe"

            if not input_path.endswith('.enc'):
                return False, "El archivo debe tener extensión .enc"

            min_size = self.salt_length + self.nonce_length + self.tag_length + 1
            if os.path.getsize(input_path) < min_size:
                return False, "Archivo cifrado corrupto o inválido"

            with open(input_path, 'rb') as f:
                salt = f.read(self.salt_length)
                nonce = f.read(self.nonce_length)
                tag = f.read(self.tag_length)
                ciphertext = f.read()

            key, _ = self._derive_key(password, salt)
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)

            output_path = input_path[:-4]
            if os.path.exists(output_path):
                return False, "El archivo original ya existe"

            with open(output_path, 'wb') as f:
                f.write(plaintext)

            return True, output_path

        except ValueError:
            return False, "Contraseña incorrecta o archivo corrupto"
        except Exception as e:
            return False, f"Error al descifrar: {str(e)}"

def show_menu():
    table = Table(show_header=False, box=None)
    table.add_column("Opciones", style="bold green")
    table.add_row("1. Cifrar archivo")
    table.add_row("2. Descifrar archivo")
    table.add_row("3. Salir")
    console.print(table)

def get_password():
    while True:
        password = getpass.getpass("🔑 Contraseña (mínimo 12 caracteres): ")
        if len(password) >= 12:
            confirm = getpass.getpass("🔑 Confirmar contraseña: ")
            if password == confirm:
                return password
            console.print("[red]Error: Las contraseñas no coinciden[/]")
        else:
            console.print("[red]Error: La contraseña debe tener al menos 12 caracteres[/]")

def main():
    encryptor = FileEncryptor()

    while True:
        console.print("\n[bold cyan]MENÚ PRINCIPAL[/]", justify="center")
        show_menu()

        option = Prompt.ask("Seleccione una opción", choices=["1", "2", "3"])

        if option == "1":
            file_path = Prompt.ask("📄 Ruta del archivo a cifrar")
            result = encryptor.encrypt_file(file_path, get_password())

            if result[0]:
                console.print(f"[green]✓ Archivo cifrado: {result[1]}[/]")
                console.print("[yellow]⚠️ Guarde su contraseña en un lugar seguro[/]")
            else:
                console.print(f"[red]✗ {result[1]}[/]")

        elif option == "2":
            file_path = Prompt.ask("📄 Ruta del archivo cifrado")
            if not file_path.endswith('.enc'):
                file_path += '.enc'

            result = encryptor.decrypt_file(file_path, getpass.getpass("🔑 Contraseña: "))

            if result[0]:
                console.print(f"[green]✓ Archivo descifrado: {result[1]}[/]")
            else:
                console.print(f"[red]✗ {result[1]}[/]")

        elif option == "3":
            console.print("[bold green]Saliendo...[/]")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Operación cancelada[/]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/]")
        sys.exit(1)