import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from colorama import init, Fore, Back, Style
import socket
import whois
import dns.resolver
import tldextract

init()

def analyze_url(url):
    try:
        session = requests.session()
        session.proxies = {}
        session.proxies['http'] = 'socks5://127.0.0.1:9050'
        session.proxies['https'] = 'socks5://127.0.0.1:9050'
        response = session.get(url, timeout=5)
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

        # Obtener la información de Whois
        whois_info = whois.whois(url)
        whois_domain = whois_info.domain
        whois_registrar = whois_info.registrar
        whois_creation_date = whois_info.creation_date
        whois_expiration_date = whois_info.expiration_date

        # Obtener la información de DNS
        dns_info = dns.resolver.resolve(url, 'A')
        dns_ip_address = dns_info[0].to_text()

        # Obtener la información de la extensión de dominio
        tld_info = tldextract.extract(url)
        tld_domain = tld_info.domain
        tld_suffix = tld_info.suffix

        url_data = [
            ["URL", url],
            ["Título de la página", title],
            ["Formularios peligrosos", "Sí" if forms_peligrosos else "No"],
            ["Enlaces externos", "Sí" if enlaces_externos else "No"],
            ["Dirección IP", ip_address],
            ["Whois Domain", whois_domain],
            ["Whois Registrar", whois_registrar],
            ["Whois Creation Date", whois_creation_date],
            ["Whois Expiration Date", whois_expiration_date],
            ["DNS IP Address", dns_ip_address],
            ["TLD Domain", tld_domain],
            ["TLD Suffix", tld_suffix],
        ]

        print(Fore.GREEN + Back.BLACK + tabulate(url_data, headers=["Información", "Valor"], tablefmt="fancy_grid"), Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

def main():
    url = input(Fore.GREEN + Style.BRIGHT + "Ingrese la URL: ")
    analyze_url(url)

if __name__ == "__main__":
    main()