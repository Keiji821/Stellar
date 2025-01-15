import phonenumbers
from phonenumbers import carrier, geocoder, number_type
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn
import requests

console = Console()

while True:
    phone_number = console.input("[bold green]Ingrese un número de celular: [/bold green]")
    try:
        response1 = requests.get(f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey=num_live_z5WCcECRDEQ1YL9H5smWU8fhwH3NoOjf9oj3QVEp")
        data1 = response1.json()
        response2 = requests.get(f"http://phone-number-api.com/json/?number={phone_number}")
        data2 = response2.json()

        location = data1.get("location")
        if location is not None:
            localización = location
            if location is None:
                localización = "No disponible"

        regionName = data2.get("regionName")

        city = data2.get("city")

        zip = data2.get("zip")

        lon = data2.get("lon")

        lat = data2.get("lat")
        
        
        
        parse_result = phonenumbers.parse(phone_number, None)
        country_name = geocoder.description_for_number(parse_result, "es")
        carrier_name = carrier.name_for_number(parse_result, "es")
        is_valid = "Sí" if phonenumbers.is_valid_number(parse_result) else "No"
        country_code = parse_result.country_code
        national_number = parse_result.national_number
        extension = parse_result.extension if parse_result.extension else "No disponible"
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
        }.get(phonenumbers.number_type(parse_result), "Desconocido")

        
        print(" ")
        table = Table(title="Información del número de teléfono", title_justify="center", title_style="bold green")
        table.add_column("[green]Información", style="code", no_wrap=False)
        table.add_column("[green]Valor", style="code")

        table.add_row("[underline][bold green]Información geográfica[/bold green]")
        table.add_row("País/dirección 1", country_name)
        table.add_row("Dirección 2", localización)
        table.add_row("Región", )
        table.add_row("Ciudad", ) 
        table.add_row("Código postal", )
        table.add_row("Longitud", )
        table.add_row("Latitud", )


        table.add_row(" ", " ")
        table.add_row("[underline][bold green]Información técnica[/bold green]")
        table.add_row("Empresa de teléfono 1", str(data1.get("carrier")))
        table.add_row("Empresa de teléfono 2", str(carrier_name))
        table.add_row("Número de teléfono válido", is_valid)
        table.add_row("El número es válido en la región", str(data2.get("numberValidForRegion")))
        table.add_row("Tipo de número", number_type_name)
        table.add_row(" ", " ")
        table.add_row("[underline][bold green]Información adicional[/bold green]")
        table.add_row("Código de país", str(country_code))
        table.add_row("Número nacional", str(national_number))
        table.add_row("Extensión", extension)

        console.print(table)
        print(" ")
        break
    except phonenumbers.phonenumberutil.NumberParseException:
        console.print("[bold red]Error: El número de teléfono ingresado no es válido. Por favor, inténtalo de nuevo.[/bold red]")
