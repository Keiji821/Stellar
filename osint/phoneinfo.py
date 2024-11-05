import phonenumbers
from phonenumbers import carrier, geocoder, number_type
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn

console = Console()

while True:
    phone_number = console.input("[bold green]Ingrese un número de celular: [/bold green]")
    try:
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
        table = Table(title="Información del número de teléfono", title_justify="center", title_style="bold red")
        table.add_column("Información", style="green", no_wrap=False)
        table.add_column("Valor", style="white")

        table.add_row("País", country_name)
        table.add_row("Empresa de teléfono", carrier_name)
        table.add_row("Número de teléfono válido", is_valid)
        table.add_row("Código de país", str(country_code))
        table.add_row("Número nacional", str(national_number))
        table.add_row("Extensión", extension)
        table.add_row("Tipo de número", number_type_name)

        console.print(table)
        print(" ")
        break
    except phonenumbers.phonenumberutil.NumberParseException:
        console.print("[bold red]Error: El número de teléfono ingresado no es válido. Por favor, inténtalo de nuevo.[/bold red]")