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

class MilitaryGradeEncryptor:
    def __init__(self):
        self.iterations = 1048576
        self.salt_length = 32
        self.key_length = 32
        self.nonce_length = 16
        self.tag_length = 16

    def _derive_key(self, passphrase, salt=None):
        salt = get_random_bytes(self.salt_length) if salt is None else salt
        return scrypt(
            passphrase.encode(),
            salt=salt,
            key_len=self.key_length,
            N=self.iterations,
            r=8,
            p=1
        ), salt

    def encrypt_file(self, file_path, passphrase):
        try:
            if not os.path.exists(file_path):
                return False, "El archivo no existe"
            
            if os.path.getsize(file_path) > 1073741824:
                return False, "Archivo demasiado grande (máximo 1GB)"

            with open(file_path, 'rb') as file:
                file_data = file.read()

            key, salt = self._derive_key(passphrase)
            cipher = AES.new(key, AES.MODE_GCM)
            ciphertext, tag = cipher.encrypt_and_digest(file_data)

            encrypted_path = file_path + '.milenc'
            with open(encrypted_path, 'wb') as file:
                file.write(salt)
                file.write(cipher.nonce)
                file.write(tag)
                file.write(ciphertext)

            os.remove(file_path)
            return True, encrypted_path
        except Exception as error:
            return False, f"Error al cifrar: {str(error)}"

    def decrypt_file(self, file_path, passphrase):
        try:
            if not os.path.exists(file_path):
                return False, "El archivo cifrado no existe"
            
            if not file_path.endswith('.milenc'):
                return False, "El archivo debe tener extensión .milenc"
            
            file_size = os.path.getsize(file_path)
            min_size = self.salt_length + self.nonce_length + self.tag_length + 1
            if file_size < min_size:
                return False, "Archivo cifrado corrupto o inválido"

            with open(file_path, 'rb') as file:
                salt = file.read(self.salt_length)
                nonce = file.read(self.nonce_length)
                tag = file.read(self.tag_length)
                ciphertext = file.read()

            key, _ = self._derive_key(passphrase, salt)
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

            decrypted_path = file_path.replace('.milenc', '')
            if os.path.exists(decrypted_path):
                return False, "El archivo original ya existe"

            with open(decrypted_path, 'wb') as file:
                file.write(decrypted_data)

            return True, decrypted_path
        except ValueError as error:
            return False, "Frase secreta incorrecta o archivo corrupto"
        except Exception as error:
            return False, f"Error al descifrar: {str(error)}"

def mostrar_menu():
    tabla = Table(show_header=False, box=None)
    tabla.add_column("Opciones", style="bold green")
    tabla.add_row("1. Cifrar archivo")
    tabla.add_row("2. Descifrar archivo")
    tabla.add_row("3. Salir")
    console.print(tabla)

def obtener_frase_secreta():
    while True:
        passphrase = getpass.getpass("🔑 Frase secreta (mínimo 16 caracteres): ")
        if len(passphrase) >= 16:
            confirm = getpass.getpass("🔑 Confirmar frase secreta: ")
            if passphrase == confirm:
                return passphrase
            console.print("[red]Error: Las frases no coinciden[/]")
        else:
            console.print("[red]Error: La frase debe tener al menos 16 caracteres[/]")

def main():
    encryptor = MilitaryGradeEncryptor()
    
    while True:
        console.print("\n[bold cyan]MENÚ PRINCIPAL[/]", justify="center")
        mostrar_menu()
        
        while True:
            opcion = Prompt.ask("Seleccione una opción")
            if opcion in ["1", "2", "3"]:
                break
            console.print("[red]Por favor seleccione una de las opciones disponibles: 1, 2 o 3[/]")

        if opcion == "1":
            ruta_archivo = Prompt.ask("📄 Ruta del archivo a cifrar")
            resultado = encryptor.encrypt_file(ruta_archivo, obtener_frase_secreta())
            
            if resultado[0]:
                console.print(f"[green]✓ Archivo cifrado con éxito: {resultado[1]}[/]")
                console.print("[yellow]⚠️ ¡ADVERTENCIA! GUARDE SU FRASE SECRETA EN UN LUGAR SEGURO. SIN ELLA, SUS ARCHIVOS SON IRRECUPERABLES.[/]")
            else:
                console.print(f"[red]✗ Error: {resultado[1]}[/]")

        elif opcion == "2":
            ruta_archivo = Prompt.ask("📄 Ruta del archivo cifrado")
            if not ruta_archivo.endswith('.milenc'):
                ruta_archivo += '.milenc'
                
            resultado = encryptor.decrypt_file(ruta_archivo, getpass.getpass("🔑 Frase secreta: "))
            
            if resultado[0]:
                console.print(f"[green]✓ Archivo descifrado con éxito: {resultado[1]}[/]")
            else:
                console.print(f"[red]✗ Error: {resultado[1]}[/]")

        elif opcion == "3":
            console.print("[bold green]Saliendo del sistema...[/]")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Operación cancelada por el usuario[/]")
        sys.exit(0)
    except Exception as error:
        console.print(f"[red]Error crítico: {str(error)}[/]")
        sys.exit(1)