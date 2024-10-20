from colorama import init, Fore, Back, Style
import sqlite3
from tabulate import tabulate

init()

conn = sqlite3.connect('/data/data/com.termux/files/home/Stellar/database/ips_info_history.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM ips_info_history')

results = cursor.fetchall()

headers = ['Posición', 'IP', 'Fecha']
print(Fore.GREEN + Back.BLACK + tabulate(results, headers, tablefmt='fancy_grid'), Style.RESET_ALL)


