from stellar_translate import translate
from rich.console import Console
from datetime import datetime
from rich.table import Table
import requests
import time
import re

console = Console()

def http(IpQuery):
    try:
        response = requests.get(f"https://api.ipapi.is/?ip={IpQuery}")
        if response.status_code == 200:
            data = response.json()
            
            ip = str(data.get("ip"))
            rir = str(data.get("rir"))
            
            is_bogon = str(data.get("is_bogon"))
            if is_bogon == "True":
                is_bogon = translate(category="ipinfo", type="yes_message")
            elif is_bogon == "False":
                is_bogon = translate(category="ipinfo", type="not_message")

            is_mobile = str(data.get("is_mobile"))
            if is_mobile == "True":
                is_mobile = translate(category="ipinfo", type="yes_message")
            elif is_mobile == "False":
                is_mobile = translate(category="ipinfo", type="not_message")

            is_crawler = str(data.get("is_crawler"))
            if is_crawler == "True":
                is_crawler = translate(category="ipinfo", type="yes_message")
            elif is_crawler == "False":
                is_crawler = translate(category="ipinfo", type="not_message")

            is_datacenter = str(data.get("is_datacenter"))
            if is_datacenter == "True":
                is_datacenter = translate(category="ipinfo", type="yes_message")
            elif is_datacenter == "False":
                is_datacenter = translate(category="ipinfo", type="not_message")

            is_tor = str(data.get("is_tor"))
            if is_tor == "True":
                is_tor = translate(category="ipinfo", type="yes_message")
            elif is_tor == "False":
                is_tor = translate(category="ipinfo", type="not_message")

            is_proxy = str(data.get("is_proxy"))
            if is_proxy == "True":
                is_proxy = translate(category="ipinfo", type="yes_message")
            elif is_proxy == "False":
                is_proxy = translate(category="ipinfo", type="not_message")

            is_vpn = str(data.get("is_vpn"))
            if is_vpn == "True":
                is_vpn = translate(category="ipinfo", type="yes_message")
            elif is_vpn == "False":
                is_vpn = translate(category="ipinfo", type="not_message")

            is_abuser = str(data.get("is_abuser"))
            if is_abuser == "True":
                is_abuser = translate(category="ipinfo", type="yes_message")
            elif is_abuser == "False":
                is_abuser = translate(category="ipinfo", type="not_message")
                
            is_satellite = str(data.get("is_satellite"))
            if is_satellite == "True":
                is_satellite = translate(category="ipinfo", type="yes_message")
            elif is_satellite == "False":
                is_satellite = translate(category="ipinfo", type="not_message")


            company_name = str(data.get("company", {}).get("name"))
            abuser_score = str(data.get("company", {}).get("abuser_score"))
            domain = str(data.get("company", {}).get("domain"))
            type = str(data.get("company", {}).get("type"))
            network = str(data.get("company", {}).get("network"))
            abuse_name = str(data.get("abuse", {}).get("name"))
            address = str(data.get("abuse", {}).get("address"))
            phone = str(data.get("abuse", {}).get("phone"))
            asn = str(data.get("asn", {}).get("asn"))
            abuser_score2 = str(data.get("asn", {}).get("abuser_score"))
            route = str(data.get("asn", {}).get("route"))
            descr = str(data.get("asn", {}).get("descr"))
            
            active = str(data.get("asn", {}).get("active"))
            if active == "True":
                active = translate(category="ipinfo", type="yes_message")
            if active == "False":
                active = translate(category="ipinfo", type="not_message")

            org = str(data.get("asn", {}).get("org"))
            asn_domain = str(data.get("asn", {}).get("domain"))
            abuse = str(data.get("asn", {}).get("abuse"))
            asn_type = str(data.get("asn", {}).get("type"))
            created = str(data.get("asn", {}).get("created"))
            updated = str(data.get("asn", {}).get("updated"))
            asn_rir = str(data.get("asn", {}).get("rir"))
            calling_code = str(data.get("location", {}).get("calling_code"))
            continent = data.get('location', {}).get('continent')
            continent_tr = {
                'SA': translate(category="phoneinfo", type="south_america_message"),
                'EU': translate(category="phoneinfo", type="europe_message"),
                'NA': translate(category="phoneinfo", type="north_america_message"),
                'AS': translate(category="phoneinfo", type="asia_message"),
                'AF': translate(category="phoneinfo", type="africa_message"),
                'OC': translate(category="phoneinfo", type="oceania_message"),
                'AN': translate(category="phoneinfo", type="antarctica_message")
            }
            continentes = continent_tr.get(continent)
            country = str(data.get("location", {}).get("country"))
            state = str(data.get("location", {}).get("state"))
            city = str(data.get("location", {}).get("city"))
            latitude = str(data.get("location", {}).get("latitude"))
            longitude = str(data.get("location", {}).get("longitude"))
            zip = str(data.get("location", {}).get("zip"))
            timezone = str(data.get("location", {}).get("timezone"))
            
            return ip, rir, is_bogon, is_mobile, is_crawler, is_datacenter, is_tor, is_proxy, is_vpn, is_abuser, is_satellite, company_name, abuser_score, domain, type, network, abuse_name, address, phone, asn, abuser_score2, route, descr, active, org, asn_domain, abuse, asn_type, created, updated, asn_rir, calling_code, continentes, country, state, city, latitude, longitude, zip, timezone
        
        elif response.status_code != 200:
            console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")}")
            exit()
    
    except requests.exceptions.RequestException as e:
        exit()
    except requests.exceptions.ConnectionError:
        exit()
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return


def table(IpQuery=None):
    try:
        result = http(IpQuery)
        ip, rir, is_bogon, is_mobile, is_crawler, is_datacenter, is_tor, is_proxy, is_vpn, is_abuser, is_satellite, company_name, abuser_score, domain, type, network, abuse_name, address, phone, asn, abuser_score2, route, descr, active, org, asn_domain, abuse, asn_type, created, updated, asn_rir, calling_code, continentes, country, state, city, latitude, longitude, zip, timezone = result
        
        console.print(" ")
        table = Table(title=translate(category="ipinfo", type="ip_message"), title_justify="center", title_style="bold green")
        table.add_column(translate(category="ipinfo", type="information_message"), style="code", no_wrap=False)
        table.add_column(translate(category="ipinfo", type="value_message"), style="code")
        
        table.add_row(f"[bold underline][code][bold green]{translate(category="ipinfo", type="information_red_message")}[/bold underline][/bold green][/code]", "")
        table.add_row(translate(category="ipinfo", type="ip_message"), ip)
        table.add_row(translate(category="ipinfo", type="rir_message"), rir)
        table.add_row(translate(category="ipinfo", type="not_assigned_ip_message"), is_bogon)
        table.add_row(translate(category="ipinfo", type="is_mobil_message"), is_mobile)
        table.add_row(translate(category="ipinfo", type="is_crawler_message"), is_crawler)
        table.add_row(translate(category="ipinfo", type="is_datacenter_message"), is_datacenter)
        table.add_row(translate(category="ipinfo", type="is_tor_message"), is_tor)
        table.add_row(translate(category="ipinfo", type="is_proxy_message"), is_proxy)
        table.add_row(translate(category="ipinfo", type="is_vpn_message"), is_vpn)
        table.add_row(translate(category="ipinfo", type="is_abuser_message"), is_abuser)
        table.add_row(translate(category="ipinfo", type="is_satellite_message"), is_satellite)
        table.add_row("", "")
        table.add_row(f"[bold underline][code][bold green]{translate(category="ipinfo", type="information_company_message")}[/bold underline][/bold green][/code]", "")
        table.add_row(translate(category="ipinfo", type="network_message"), network)
        table.add_row(translate(category="ipinfo", type="company_name_message"), company_name)
        table.add_row(translate(category="ipinfo", type="abuser_score_message"), abuser_score)
        table.add_row(translate(category="ipinfo", type="domain_message"), domain)
        table.add_row(translate(category="ipinfo", type="abuser_type_message"), type)
        table.add_row("", "")
        table.add_row(f"[bold underline][code][bold green]{translate(category="ipinfo", type="information_abuser_message")}[/bold underline][/bold green][/code]", "")
        table.add_row(translate(category="ipinfo", type="abuser_name_message"), abuse_name)
        table.add_row(translate(category="ipinfo", type="address_message"), address)
        table.add_row(translate(category="ipinfo", type="phone_message"), phone)
        table.add_row("", "")
        table.add_row(f"[bold underline][code][bold green]{translate(category="ipinfo", type="information_asn_message")}[/bold underline][/bold green][/code]", "")
        table.add_row(translate(category="ipinfo", type="asn_message"), asn)
        table.add_row(translate(category="ipinfo", type="abuser_score_message"), abuser_score2)
        table.add_row(translate(category="ipinfo", type="route_message"), route)
        table.add_row(translate(category="ipinfo", type="description_message"), descr)
        table.add_row(translate(category="ipinfo", type="active_message"), active)
        table.add_row(translate(category="ipinfo", type="org_message"), org)
        table.add_row(translate(category="ipinfo", type="asn_domain_message"), asn_domain)
        table.add_row(translate(category="ipinfo", type="abuse_message"), abuse)
        table.add_row(translate(category="ipinfo", type="asn_type_message"), asn_type)
        table.add_row(translate(category="ipinfo", type="created_message"), created)
        table.add_row(translate(category="ipinfo", type="updated_message"), updated)
        table.add_row(translate(category="ipinfo", type="asn_rir_message"), asn_rir)
        table.add_row("", "")
        table.add_row(f"[bold underline][code][bold green]{translate(category="ipinfo", type="information_geo_message")}[/bold underline][/bold green][/code]", "")
        table.add_row(translate(category="ipinfo", type="continent_message"), continentes)
        table.add_row(translate(category="ipinfo", type="country_message"), country)
        table.add_row(translate(category="ipinfo", type="state_message"), state)
        table.add_row(translate(category="ipinfo", type="city_message"), city)
        table.add_row(translate(category="ipinfo", type="zip_code_message"), zip)
        table.add_row(translate(category="ipinfo", type="latitude_message"), latitude)
        table.add_row(translate(category="ipinfo", type="longitude_message"), longitude)
        table.add_row(translate(category="ipinfo", type="timezone_message"), timezone)
        table.add_row(translate(category="ipinfo", type="calling_code_message"), calling_code)

        console.print(table)
        console.print(" ")
        exit()
        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return
                
def ipinfo():
    try:
        ip_pattern = r'\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b'
        while True:
            ip = console.input(f"[bold green]➤  {translate(category="user-config", type="enter_message")} [/bold green]")
            if not ip:
                console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                continue
            elif ip:
                if not re.search(ip_pattern, ip):
                    console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                    continue
                else:
                    table(IpQuery=ip)
                    
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return
        
ipinfo()