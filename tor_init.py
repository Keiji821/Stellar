from colorama import init, Fore, Back, Style
import os
from os import system
from tqdm import tqdm
import subprocess
import threading
import time

init()


print(Style.BRIGHT + Fore.RED)

time.sleep(1)

for i in tqdm(range(10), desc="Iniciando Tor"):
        time.sleep(0.1)
        FNULL = open(os.devnull, 'w')
        subprocess.call(['tor', '--wait'], stdout=FNULL, stderr=subprocess.STDOUT)
        FNULL.close()

time.sleep(1)

os.system('clear')
print(Style.BRIGHT + Fore.GREEN + Back.WHITE + " ✔", Style.RESET_ALL, Style.BRIGHT + Fore.RED + "Tor iniciado.", Style.RESET_ALL)

time.sleep(1)
