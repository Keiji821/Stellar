import requests
from colorama import init, Fore, Back, Style
import textwrap
import os
from rich.console import Console
from rich.table import Table

init()

API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"

def get_ai_response(user_input):
    try:
        url = f"https://api.kastg.xyz/api/ai/fast-llamaV3-large?key={API_KEY}&prompt={user_input}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["result"][0]["response"]
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error: " + str(e) + Style.RESET_ALL)
        return None

def print_ai_response(response):
    wrapped_response = textwrap.fill(response, width=50)
    table = Table(title="Llama IA", title_justify="center", title_style="bold magenta")
    table.add_column("Respuesta", style="cyan", no_wrap=False)
    table.add_row(wrapped_response)
    console = Console()
    console.print(table)

def execute_command(command):
    print(f"Ejecutando comando: {command}")
    os.system(command)

while True:
    user_input = input(Fore.GREEN + Style.BRIGHT + "> ")
    response = get_ai_response(user_input)
    if response:
        print_ai_response(response)
        if "ejecutar " in response:
            command = response.split("ejecutar ")[1]
            execute_command(command)
    else:
        print(Fore.RED + "Error" + Style.RESET_ALL)
