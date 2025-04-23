from instaloader import Instaloader, Profile
from rich.console import Console

L = Instaloader()
console = Console()

usuario = console.input("[bold green]Ingrese un nombre de usuario: [bold green]")

profile = Profile.from_username(L.context, usuario)

console.print("[bold green]Usuario: [/bold green]", usuario)
console.print("[bold green]Bio: [/bold green]", {profile.biography})
console.print("[bold green]Seguidores: [/bold green]", {profile.followers})
