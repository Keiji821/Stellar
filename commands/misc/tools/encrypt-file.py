import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import Progress
import getpass

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
            return False, str(error)

    def decrypt_file(self, file_path, passphrase):
        try:
            with open(file_path, 'rb') as file:
                salt = file.read(self.salt_length)
                nonce = file.read(self.nonce_length)
                tag = file.read(self.tag_length)
                ciphertext = file.read()

            key, _ = self._derive_key(passphrase, salt)
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

            decrypted_path = file_path.replace('.milenc', '')
            with open(decrypted_path, 'wb') as file:
                file.write(decrypted_data)

            return True, decrypted_path
        except Exception as error:
            return False, str(error)

def show_menu():
    console.print("\n[bold cyan]🔐 CIFRADOR DE SEGURIDAD NIVEL BLOCKCHAIN[/]", justify="center")
    table = Table(show_header=False, box=None)
    table.add_column("Opciones", style="bold green")
    table.add_row("1. Cifrar archivo")
    table.add_row("2. Descifrar archivo")
    table.add_row("3. Salir")
    console.print(table)

def get_passphrase():
    while True:
        passphrase = getpass.getpass("🔑 Frase secreta (mínimo 16 caracteres): ")
        if len(passphrase) >= 16:
            confirm = getpass.getpass("🔑 Confirmar frase secreta: ")
            if passphrase == confirm:
                return passphrase
            console.print("[red]Las frases no coinciden[/]")
        else:
            console.print("[red]La frase debe tener al menos 16 caracteres[/]")

def main():
    encryptor = MilitaryGradeEncryptor()
    
    while True:
        show_menu()
        option = Prompt.ask("Seleccione una opción", choices=["1", "2", "3"])

        if option == "1":
            file_path = Prompt.ask("📄 Ruta del archivo a cifrar")
            if not os.path.exists(file_path):
                console.print("[red]El archivo no existe[/]")
                continue
                
            passphrase = get_passphrase()
            success, result = encryptor.encrypt_file(file_path, passphrase)
            
            if success:
                console.print(f"[green]✓ Archivo cifrado: {result}[/]")
                console.print("[yellow]⚠️ GUARDE SU FRASE SECRETA. SIN ELLA, SUS ARCHIVOS SON IRRECUPERABLES.[/]")
            else:
                console.print(f"[red]✗ Error: {result}[/]")

        elif option == "2":
            file_path = Prompt.ask("📄 Ruta del archivo cifrado")
            if not file_path.endswith('.milenc'):
                file_path += '.milenc'
                
            if not os.path.exists(file_path):
                console.print("[red]El archivo cifrado no existe[/]")
                continue
                
            passphrase = getpass.getpass("🔑 Frase secreta: ")
            success, result = encryptor.decrypt_file(file_path, passphrase)
            
            if success:
                console.print(f"[green]✓ Archivo descifrado: {result}[/]")
            else:
                console.print(f"[red]✗ Error: {result}[/]")

        elif option == "3":
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Operación cancelada[/]")
    except Exception as error:
        console.print(f"[red]Error crítico: {str(error)}[/]")