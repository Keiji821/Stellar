import requests
from bs4 import BeautifulSoup
import subprocess
from colorama import init, Fore, Back, Style
import socket
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

init()

def analyze_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('title').text

        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})

        ip_address = socket.gethostbyname(url.split("//")[-1].split('/')[0])

        server_info = response.headers.get('Server')

        nmap_output = subprocess.check_output(['nmap', '-v', '-A', ip_address])

        open_ports = []
        for line in nmap_output.decode('utf-8').splitlines():
            if 'open' in line:
                open_ports.append(line.split()[0])

        table = Table(title="Información del sitio web", title_justify="center", title_style="bold magenta")

        table.add_column("Información", style="cyan", no_wrap=True)
        table.add_column("Valor", style="magenta", no_wrap=True)

        table.add_row("URL", url, style="green")
        table.add_row("Título", title, style="yellow")
        table.add_row("Meta Description", meta_description['content'] if meta_description else '', style="blue")
        table.add_row("Meta Keywords", meta_keywords['content'] if meta_keywords else '', style="blue")
        table.add_row("Puertos abiertos", ', '.join(open_ports), style="red")
        table.add_row("Dirección IP", ip_address, style="green")
        table.add_row("Servidor", server_info, style="yellow")

        Console.print(table)

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def main():
    url = input(Fore.GREEN + Style.BRIGHT + "Ingrese la URL: ")
    analyze_url(url)

if __name__ == "__main__":
    main()