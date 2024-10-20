import requests
from colorama import init, Fore, Back, Style
import textwrap
import os

init()

api_key = "Kastg_fKlIk2c1LRc8969in2g9_free"

while True:
    user_input = input(Fore.GREEN + Style.BRIGHT + "> ")
    url = f"https://api.kastg.xyz/api/ai/llamaV3-large?key={api_key}&prompt={user_input}"
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()['result'][0]['response']
        block_size = 50
        blocks = [Style.BRIGHT + result[i:i+block_size] for i in range(0, len(result), block_size)]
        print(Fore.RED + Style.BRIGHT + "Stellar IA" + Style.RESET_ALL)
        for block in blocks:
            print(block)


        if "ejecutar " in result:
            command = result.split("ejecutar ")[1]
            print(f"Ejecutando comando: {command}")
            os.system(command)

    else:
        print(Fore.RED + "Error: " + str(response.status_code) + Style.RESET_ALL)
