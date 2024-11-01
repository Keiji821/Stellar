import datetime
import phonenumbers
from tabulate import tabulate
from phonenumbers import carrier, geocoder, number_type
from phonenumbers.phonenumberutil import NumberParseException
from colorama import init, Fore, Back, Style
from rich import print
from rich.console import Console
from rich.markdown import Markdown

init()

while True:
    phone_number = input(Fore.GREEN + Style.BRIGHT + "Ingrese un número de celular: ")
    try:
        parse_result = phonenumbers.parse(phone_number, None)
        country_name = geocoder.description_for_number(parse_result, "es")
        carrier_name = carrier.name_for_number(parse_result, "es")
        is_valid = "Sí" if phonenumbers.is_valid_number(parse_result) else "No"
        country_code = parse_result.country_code
        national_number = parse_result.national_number
        extension = parse_result.extension
        number_type_name = {
    0: "Desconocido",
    1: "Línea fija",
    2: "Móvil",
    3: "Número gratuito",
    4: "Tarifa premium",
    5: "Costo compartido",
    6: "VoIP",
    7: "Número personal",
    8: "Busca personas",
    9: "UAN",
    10: "Buzón de voz"
}[number_type(parse_result)]

        table_data = [
            ["País", country_name],
            ["Empresa de teléfono", carrier_name],
            ["Número de teléfono válido", is_valid],
            ["Código de país", country_code],
            ["Número nacional", national_number],
            ["Extensión", extension],
            ["Tipo de número", number_type_name],
        ]

        print(Fore.GREEN + Back.BLACK + tabulate(table_data, headers=["Información", "Valor"], tablefmt="fancy_grid"), Style.RESET_ALL)
        break
    except phonenumbers.phonenumberutil.NumberParseException:
        print(Fore.RED + "Error: El número de teléfono ingresado no es válido. Por favor, inténtalo de nuevo." + Fore.RESET)
