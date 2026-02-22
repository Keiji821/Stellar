from stellar_translate import translate
import phonenumbers
from phonenumbers import carrier, geocoder, number_type
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn
import requests
import re

console = Console()

def http(phone_number=None):
    try:
        parse_result = phonenumbers.parse(phone_number, None)
        
        country_name = geocoder.description_for_number(parse_result, "es")
        if country_name == "":
            country_name = translate(category="user-config", type="unknown_message")
        elif not country_name:
            country_name = translate(category="user-config", type="unknown_message")

        carrier_name = carrier.name_for_number(parse_result, "es")
        if carrier_name == "":
            carrier_name = translate(category="user-config", type="unknown_message")
        elif not carrier_name:
            carrier_name = translate(category="user-config", type="unknown_message")

        is_valid = phonenumbers.is_valid_number(parse_result)
        if is_valid:
            is_valid = translate(category="ipinfo", type="yes_message")
        elif not is_valid:
            is_valid = translate(category="ipinfo", type="not_message")
        
        extension = parse_result.extension
        if extension == "":
            extension = translate(category="user-config", type="unknown_message")
        elif not extension:
            extension = translate(category="user-config", type="unknown_message")
        
        country_code = str(parse_result.country_code)
        national_number = str(parse_result.national_number)
        number_type_name = {
            0: translate(category="phoneinfo", type="number_type_0_message"),
            1: translate(category="phoneinfo", type="number_type_1_message"),
            2: translate(category="phoneinfo", type="number_type_2_message"),
            3: translate(category="phoneinfo", type="number_type_3_message"),
            4: translate(category="phoneinfo", type="number_type_4_message"),
            5: translate(category="phoneinfo", type="number_type_5_message"),
            6: translate(category="phoneinfo", type="number_type_6_message"),
            7: translate(category="phoneinfo", type="number_type_7_message"),
            8: translate(category="phoneinfo", type="number_type_8_message"),
            9: translate(category="phoneinfo", type="number_type_9_message"),
            10: translate(category="phoneinfo", type="number_type_10_message")
        }.get(phonenumbers.number_type(parse_result), translate(category="user-config", type="unknown_message"))
        
        
        response = requests.get(f"http://phone-number-api.com/json/?number={phone_number}")
        data = response.json()
        if response.status_code == 200:
            
            regionName = data.get("regionName")
            if regionName is None:
                regionName = translate(category="user-config", type="unknown_message")
                
            city = data.get("city")
            if city is None:
                city = translate(category="user-config", type="unknown_message")
                
            zip = data.get("zip")
            if zip is None:
                zip = translate(category="user-config", type="unknown_message")
                
            lon = str(data.get("lon"))
            if lon is None:
                lon = translate(category="user-config", type="unknown_message")
                
            lat = str(data.get("lat"))
            if lat is None:
                lat = translate(category="user-config", type="unknown_message")
                
            numberValidForRegion = str(data.get("numberValidForRegion"))
            if numberValidForRegion is not None:
                numberValidForRegion = translate(category="ipinfo", type="yes_message")
            elif numberValidForRegion is None:
                numberValidForRegion = translate(category="ipinfo", type="not_message")
                
            isDisposible = str(data.get("isDisposible"))
            if isDisposible == "True":
                isDisposible = translate(category="ipinfo", type="yes_message")
            elif isDisposible == "False":
                isDisposible = translate(category="ipinfo", type="not_message")
            elif isDisposible == "None":
                isDisposible = translate(category="user-config", type="unknown_message")
            
            continent = data.get("continent")
            if continent is None:
                continent = translate(category="user-config", type="unknown_message")
            continentname = {
                'South America': translate(category="phoneinfo", type="south_america_message"),
                'Europe': translate(category="phoneinfo", type="europe_message"), 
                'North America': translate(category="phoneinfo", type="north_america_message"),
                'Asia': translate(category="phoneinfo", type="asia_message"),
                'Africa': translate(category="phoneinfo", type="africa_message"),
                'Oceania': translate(category="phoneinfo", type="oceania_message"),
                'Antarctica': translate(category="phoneinfo", type="antarctica_message")
            }
            continent_es = continentname.get(continent)
        
        return country_name, continent_es, regionName, city, zip, lon, lat, carrier_name,isDisposible, is_valid, numberValidForRegion, number_type_name, country_code, national_number, extension

    except requests.exceptions.RequestException as e:
        exit()
    except requests.exceptions.ConnectionError:
        exit()
    except phonenumbers.phonenumberutil.NumberParseException as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")} > {e}")
        return
        

def table(phone_number=None):
    try:
        result = http(phone_number)
        country_name, continent_es, regionName, city, zip, lon, lat, carrier_name,isDisposible, is_valid, numberValidForRegion, number_type_name, country_code, national_number, extension = result
        
        console.print(" ")
        table = Table(title=translate(category="phoneinfo", type="phone_message"), title_justify="center", title_style="bold green")
        table.add_column(translate(category="ipinfo", type="information_message"), style="code", no_wrap=False)
        table.add_column(translate(category="ipinfo", type="value_message"), style="code")

        table.add_row(f"[underline][bold green]{translate(category="ipinfo", type="information_geo_message")}[/bold green][/underline]")
        table.add_row(translate(category="phoneinfo", type="country_and_address_message"), country_name)
        table.add_row(translate(category="ipinfo", type="continent_message"), continent_es)
        table.add_row(translate(category="phoneinfo", type="region_message"), regionName)
        table.add_row(translate(category="ipinfo", type="city_message"), city) 
        table.add_row(translate(category="ipinfo", type="zip_code_message"), zip)
        table.add_row(translate(category="ipinfo", type="longitude_message"), lon)
        table.add_row(translate(category="ipinfo", type="latitude_message"), lat)
        table.add_row(" ", " ")
        table.add_row(f"[underline][bold green]{translate(category="phoneinfo", type="information_technique_message")}[/bold green][/underline]")
        table.add_row(translate(category="phoneinfo", type="company_phone_name_message"), carrier_name)
        table.add_row(translate(category="phoneinfo", type="is_disposible_message"), isDisposible)
        table.add_row(translate(category="phoneinfo", type="is_valid_phone_message"), is_valid)
        table.add_row(translate(category="phoneinfo", type="is_valid_phone_in_region_message"), numberValidForRegion)
        table.add_row(translate(category="phoneinfo", type="number_type_message"), number_type_name)
        table.add_row(" ", " ")
        table.add_row(f"[underline][bold green]{translate(category="phoneinfo", type="information_extra_message")}[/bold green][/underline]")
        table.add_row(translate(category="phoneinfo", type="country_code_message"), country_code)
        table.add_row(translate(category="phoneinfo", type="national_number_message"), national_number)
        table.add_row(translate(category="phoneinfo", type="extension_message"), extension)

        console.print(table)
        console.print(" ")
        exit()
        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return
    
def phoneinfo():
    try:
        phone_pattern = r'(?:\+?\d{1,3}[-.\s]?)?(?:\(\d{1,4}\)|\d{1,4})[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{0,9}'
        while True:
            phone = console.input(f"[bold green]➤  {translate(category="user-config", type="enter_message")} [/bold green]")
            if not phone:
                console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                continue
            elif phone:
                if not re.search(phone_pattern, phone):
                    console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                    continue
                else:
                    table(phone_number=phone)
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return
    
phoneinfo()