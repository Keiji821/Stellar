import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from colorama import init, Fore, Back, Style
import socket

init()

def analyze_url(url):
    try:
        session = requests.session()
        session.proxies = {}
        session.proxies['http'] = 'socks5://127.0.0.1:9050'
        session.proxies['https'] = 'socks5://127.0.0.1:9050'
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        forms_peligrosos = False
        enlaces_externos = False

        forms = soup.find_all('form')
        for form in forms:
            if form.get('action').startswith(('http://', 'https://')):
                forms_peligrosos = True
                break

        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and href.startswith(('http://', 'https://')):
                enlaces_externos = True
                break

        title = soup.find('title').text

        # Obtener la dirección IP de la página
        ip_address = socket.gethostbyname(url.split("//")[-1].split('/')[0])

        url_data = [
            ["URL", url],
            ["Título de la página", title],
            ["Formularios peligrosos", "Sí" if forms_peligrosos else "No"],
            ["Enlaces externos", "Sí" if enlaces_externos else "No"],
            ["Dirección IP", ip_address],
        ]

        print(Fore.GREEN + Back.BLACK + tabulate(url_data, headers=["Información", "Valor"], tablefmt="fancy_grid"), Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def main():
    url = input(Fore.GREEN + Style.BRIGHT + "Ingrese la URL: ")
    analyze_url(url)

if __name__ == "__main__":
    main()
