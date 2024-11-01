import requests
from bs4 import BeautifulSoup
import subprocess
from tabulate import tabulate
from colorama import init, Fore, Back, Style
import socket

init()

def analyze_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('title').text

        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})

        nmap_output = subprocess.check_output(['nmap', '-p', '1-1000', '-sT', '-sU', url])

        open_ports = []
        for line in nmap_output.decode('utf-8').splitlines():
            if 'open' in line:
                open_ports.append(line.split()[0])

        ip_address = socket.gethostbyname(url.split("//")[-1].split('/')[0])

        server_info = response.headers.get('Server')

        data = [
            ['URL', url],
            ['Título', title],
            ['Meta Description', meta_description['content'] if meta_description else ''],
            ['Meta Keywords', meta_keywords['content'] if meta_keywords else ''],
            ['Puertos abiertos', ', '.join(open_ports)],
            ['Dirección IP, ip_address],
            ['Servidor', server_info],
        ]

        print(Fore.GREEN + Back.BLACK + tabulate(data, headers=["Información", "Valor"], tablefmt="fancy_grid") + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def main():
    url = input(Fore.GREEN + Style.BRIGHT + "Ingrese la URL: ")
    analyze_url(url)

if __name__ == "__main__":
    main()