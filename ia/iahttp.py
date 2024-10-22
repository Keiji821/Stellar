import requests
from colorama import init, Fore, Back, Style
import textwrap
import os
from tabulate import tabulate

init()

API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"

def get_ai_response(user_input):
    try:
        url = f"https://api.kastg.xyz/api/ai/llamaV3-large?key={API_KEY}&prompt={user_input}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["result"][0]["response"]
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error: " + str(e) + Style.RESET_ALL)
        return None

def print_ai_response(response):
    wrapped_response = textwrap.fill(response, width=50)
    response_table = [[wrapped_response]]
    print(Style.RESET_ALL)
    print(tabulate(response_table, headers=["Stellar IA"], tablefmt="fancy_grid"))
    print(" ")

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
