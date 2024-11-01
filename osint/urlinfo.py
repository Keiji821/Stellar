import requests
from bs4 import BeautifulSoup
import subprocess
from colorama import init, Fore, Back, Style
import socket
from rich import print
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

        print("URL", url)
        print("Título", title)
        print("Meta Description", meta_description['content'] if meta_description else '')
        print("Meta Keywords", meta_keywords['content'] if meta_keywords else '')
        print("Puertos abiertos", ', '.join(open_ports))
        print("Dirección IP", ip_address)
        print("Servidor", server_info)
        grid = Table.grid(expand=True)
        grid.add_column()
        grid.add_column(justify="right")
        grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")
        print(grid)

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def main():
    url = input(Fore.GREEN + Style.BRIGHT + "Ingrese la URL: ")
    analyze_url(url)

if __name__ == "__main__":
    main()