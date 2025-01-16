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
        response1 = requests.get(f"http://phone-number-api.com/json/?number={phone_number}")
        data1 = response1.json()  
         
        parse_result = phonenumbers.parse(phone_number, None)
        country_name = geocoder.description_for_number(parse_result, "es")
        if country_name == "":
            country_name = "No disponible"

        carrier_name = carrier.name_for_number(parse_result, "es")
        if carrier_name == "":
            carrier_name = "No disponible"

        is_valid = "Sí" if phonenumbers.is_valid_number(parse_result) else "No es válido"
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
        
        regionName = data1.get("regionName")
        if regionName is None:
            regionName = "No disponible"

        city = data1.get("city")
        if city is None:
            city = "No disponible"

        zip = data1.get("zip")
        if zip is None:
            zip = "No disponible"

        lon = data1.get("lon")
        if lon is None:
            lon = "No disponible"

        lat = data1.get("lat")
        if lat is None:
            lat = "No disponible"

        numberValidForRegion = data1.get("numberValidForRegion")
        if numberValidForRegion is not None:
            numberValidForRegion = "Sí"
        if numberValidForRegion is None:
            numberValidForRegion = "No es válido"

        continent = data1.get("continent")
        if continent is None:
            continent = "No disponible"
        isDisposible = str(data1.get("isDisposible"))
        if isDisposible == "True":
            isDisposible = "Sí"
        if isDisposible == "False":
            isDisposible = "No"
        if isDisposible == "None":
            isDisposible = "No disponible"
        
        country = data1.get("country")
        paises = {
'AR': '🇦🇷',
'BO': '🇧🇴',
'BR': '🇧🇷',
'CL': '🇨🇱',
'CO': '🇨🇴',
'CR': '🇨🇷',
'CU': '🇨🇺',
'DO': '🇩🇴',
'ES': '🇪🇸',
'GT': '🇬🇹',
'HN': '🇭🇳',
'MX': '🇲🇽',
'PA': '🇵🇦',
'PE': '🇵🇪',
'PY': '🇵🇾',
'SV': '🇸🇻',
}
        pais_emoji = paises.get(country)

        print(" ")
        table = Table(title="Información del número de teléfono", title_justify="center", title_style="bold green")
        table.add_column("[green]Información", style="code", no_wrap=False)
        table.add_column("[green]Valor", style="bold white")

        table.add_row("[underline][bold green]Información geográfica[/bold green]")
        table.add_row("País/dirección", country_name + pais_emoji)
        table.add_row("Continente", continent)
        table.add_row("Región", regionName)
        table.add_row("Ciudad", city) 
        table.add_row("Código postal", zip)
        table.add_row("Longitud", str(lon))
        table.add_row("Latitud", str(lat))
        table.add_row(" ", " ")
        table.add_row("[underline][bold green]Información técnica[/bold green]")
        table.add_row("Empresa de teléfono", carrier_name)
        table.add_row("Es desechable", isDisposible)
        table.add_row("Número de teléfono válido", is_valid)
        table.add_row("El número es válido en la región", str(numberValidForRegion))
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
