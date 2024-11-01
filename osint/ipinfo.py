import requests
from tabulate import tabulate
from colorama import init, Fore, Back, Style
from rich import print
from rich.console import Console
from rich.markdown import Markdown
import os
import datetime

init()


# Función principal

IpQuery = input(Fore.GREEN + Style.BRIGHT + "Ingrese la IP: ")

try:
    response1 = requests.get('https://ipapi.co/' + IpQuery + '/json/')
    response1.raise_for_status()
    data1 = response1.json()

    response2 = requests.get('https://api.ipapi.is/?ip=' + IpQuery + '')
    response2.raise_for_status()
    data2 = response2.json()
except requests.exceptions.RequestException as e:
    print(Fore.RED + "Error: " + str(e), Style.RESET_ALL)
except ValueError as e:
    print(Fore.RED + "Error: " + str(e), Style.RESET_ALL)
except Exception as e:
    print(Fore.RED + "Error: " + str(e), Style.RESET_ALL)


table_data1 = [
            ["Red", data1["network"]],
            ["Tipo de IP", data1["version"]],
            ["TLD", data1["country_tld"]],
            ["ASN", data1["asn"]],
            ["Empresa", data1["org"]],
            ["RIR", data2["rir"]],
            ["Es una IP no autorizada", data2["is_bogon"]],
            ["Es un móvil", data2["is_mobile"]],
            ["Es un rastreador", data2["is_crawler"]],
            ["Es un centro de datos", data2["is_datacenter"]],
            ["Es una red tor", data2["is_tor"]],
            ["Es un proxy", data2["is_proxy"]],
            ["Es una vpn", data2["is_vpn"]],
            ["Es una IP sospechosa", data2["is_abuser"]],
        ]

table_data2 = [
            ["Pais", data1["country"]],
            ["Capital", data1["country_capital"]],
            ["Ciudad", data1["city"]],
            ["Région", data1["region"]],
            ["Código de región", data1["region_code"]],
            ["Nombre de país", data1["country_name"]],
            ["Código de país", data1["country_code"]],
            ["SO3", data1["country_code_iso3"]],
            ["Código de continente", data1["continent_code"]],
            ["En europa", data1["in_eu"]],
            ["Código postal", data1["postal"]],
            ["Latitud", data1["latitude"]],
            ["Longitud", data1["longitude"]],
            ["Zona horaria", data1["timezone"]],
            ["UTC Offset", data1["utc_offset"]],
            ["Código de llamada", data1["country_calling_code"]],
            ["Moneda", data1["currency"]],
            ["Nombre de moneda", data1["currency_name"]],
            ["Idioma", data1["languages"]],
            ["Area del país", data1["country_area"]],
            ["Población del país", data1["country_population"]],
        ]


print(Fore.GREEN + Style.BRIGHT + Back.BLACK + tabulate(table_data1, headers=["Información de red", "Valor"], tablefmt="fancy_grid"), Style.RESET_ALL)
print(Fore.GREEN + Style.BRIGHT + Back.BLACK + tabulate(table_data2, headers=["Información Geográfica", "Valor"], tablefmt="fancy_grid"), Style.RESET_ALL)
