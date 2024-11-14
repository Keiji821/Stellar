import datetime
import os
from os import system
import platform
import random
import time
import requests
import figlet
import pylolcat
from pyfiglet import Figlet
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Spinner

console = Console()

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")
hour_string = now.strftime("%I:%M%p")

os_version = os.sys.platform
system_info = platform.machine() + " - " + platform.processor()

chica1 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⠚⢉⣩⣭⡭⠛⠓⠲⠦⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⠃⢀⡴⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆
⠀⠀⠀⠀⡾⠁⣠⠋⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
⠀⠀⠀⣸⠁⢰⠃⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇
⠀⠀⠀⡇⠀⡾⡀⠀⠀⠀⠀⣀⣹⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹
⠀⠀⢸⠃⢀⣇⡈⠀⠀⠀⠀⠀⠀⢀⡑⢄⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⢸⠀⢻⡟⡻⢶⡆⠀⠀⠀⠀⡼⠟⡳⢿⣦⡑⢄⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⣸⠀⢸⠃⡇⢀⠇⠀⠀⠀⠀⠀⡼⠀⠀⠈⣿⡗⠂⠀⠀⠀⠀⠀⠀⠀⢸⠁
⠀⠀⡏⠀⣼⠀⢳⠊⠀⠀⠀⠀⠀⠀⠱⣀⣀⠔⣸⠁⠀⠀⠀⠀⠀⠀⠀⢠⡟
⠀⠀⡇⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀
⠀⢸⠃⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⢀⠀⠀⠀⠀⠀⣾
⠀⣸⠀⠀⠹⡄⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠸⠀⠀⠀⠀⠀⡇
⠀⡏⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⢀⣠⢶⡇⠀⠀⢰⡀⠀⠀⠀⠀⠀⡇
⢰⠇⡄⠀⠀⠀⡿⢣⣀⣀⣀⡤⠴⡞⠉⠀⢸⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣧
⣸⠀⡇⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢹⠀⠀⢸⠀⠀⢀⣿⠇⠀⠀⠀⠁⠀⢸
⣿⠀⡇⠀⠀⠀⠀⠀⢀⡤⠤⠶⠶⠾⠤⠄⢸⠀⡀⠸⣿⣀⠀⠀⠀⠀⠀⠈⣇
⡇⠀⡇⠀⠀⡀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠸⡌⣵⡀⢳⡇⠀⠀⠀⠀⠀⠀⢹⡀
⡇⠀⠇⠀⠀⡇⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠮⢧⣀⣻⢂⠀⠀⠀⠀⠀⠀⢧
⣇⠀⢠⠀⠀⢳⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡎⣆⠀⠀⠀⠀⠀⠘
⢻⠀⠈⠰⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠘⢮⣧⡀
⠸⡆⠀⠀⠇⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠆⠀⠀⠀⠀⠀⠀⠀⠙⠳⣄⡀⢢⡀
"""

chica2 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠳⠶⣤⡄⠀⠀⠀⠀⠀⢀⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⣸⠃⠀⠀⠀⠀⣴⠟⠁⠈⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢠⡟⠀⠀⠀⢠⡾⠃⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠓⠾⠁⠀⠀⣰⠟⠀⠀⢀⡾⠋⠀⠀⠀⢀⣴⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠙⠳⣦⣴⠟⠁⠀⠀⣠⡴⠋⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⡿⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠻⢿⣿⣿⣶⣄⡀⠀⠀⠀⠺⣏⠀⠀⣀⡴⠟⠁⢀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⠿⠋⠁⠀⢀⣴⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣬⡙⠿⣿⣿⣶⣄⠀⠀⠙⢷⡾⠋⢀⣤⠾⠋⠙⢷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠋⠁⠀⠀⠀⢠⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣦⣠⣤⠽⣿⣦⠈⠙⢿⣿⣷⣄⠀⠀⠀⠺⣏⠁⠀⠀⣀⣼⠿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⡿⠋⠀⠀⠀⠀⠀⣰⣿⠟⠀⠀⠀⢠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⣿⣧⠀⠀⠈⢿⣷⣄⠀⠙⢿⣿⣷⣄⠀⠀⠙⣧⡴⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⢷⣿⡟⠀⣰⡆⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⣿⣿⡀⠀⠀⠈⢿⣿⣦⠀⠀⠙⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠁⠀⠦⣤⣀⠀⠀⢀⣿⣿⡇⢰⣿⠇⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⢸⣿⣿⣆⠀⠀⠈⣿⣿⣧⣠⣤⠾⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣵⣿⠀⠀⠀⠉⠀⠀⣼⣿⢿⡇⣾⣿⠀⠀⣾⣿⡇⢸⠀⠀⠀⠀⠀⠀⣿⡇⠀⣼⣿⢻⣿⣦⠴⠶⢿⣿⣿⣇⠀⠀⠀⢻⣿⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⢠⣿⡟⡌⣼⣿⣿⠉⢁⣿⣿⣷⣿⡗⠒⠚⠛⠛⢛⣿⣯⣯⣿⣿⠀⢻⣿⣧⠀⢸⣿⣿⣿⡄⠀⠀⠀⠙⢿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⢸⣿⡇⣼⣿⣿⣿⣶⣾⣿⣿⢿⣿⡇⠀⠀⠀⠀⢸⣿⠟⢻⣿⣿⣿⣶⣿⣿⣧⢸⣿⣿⣿⣧⠀⠀⠀⢰⣷⡈⠛⢿⣿⣿⣶⣦⣤⣤⣀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⢫⡄⠀⠀⠀⠀⠀⠀⣿⣿⣹⣿⠏⢹⣿⣿⣿⣿⣿⣼⣿⠃⠀⠀⠀⢀⣿⡿⢀⣿⣿⠟⠀⠀⠀⠹⣿⣿⣿⠇⢿⣿⡄⠀⠀⠈⢿⣿⣷⣶⣶⣿⣿⣿⣿⣿⡿
⣴⣶⣶⣿⣿⣿⣿⣋⣴⣿⣇⠀⠀⠀⠀⠀⢀⣿⣿⣿⣟⣴⠟⢿⣿⠟⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⠿⣫⣤⣶⡆⠀⠀⣻⣿⣿⣶⣸⣿⣷⡀⠀⠀⠸⣿⣿⣿⡟⠛⠛⠛⠉⠁⠀
⠻⣿⣿⣿⣿⣿⣿⡿⢿⣿⠋⠀⢠⠀⠀⠀⢸⣿⣿⣿⣿⣁⣀⣀⣁⠀⠀⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠸⢟⣫⣥⣶⣿⣿⣿⠿⠟⠋⢻⣿⡟⣇⣠⡤⠀⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⢹⣿⡇⣾⣿⠀⠀⢸⡆⠀⠀⢸⣿⣿⡟⠿⠿⠿⠿⣿⣿⣿⣿⣷⣦⡄⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣯⣥⣤⣄⣀⡀⢸⣿⠇⢿⢸⡇⠀⢹⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⡇⣿⣿⠀⠀⠸⣧⠀⠀⢸⣿⣿⠀⢀⣀⣤⣤⣶⣾⣿⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⢛⣛⠛⠛⠛⠃⠸⣿⣆⢸⣿⣇⠀⢸⣿⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣿⡇⢻⣿⡄⠀⠀⣿⡄⠀⢸⣿⡷⢾⣿⠿⠟⠛⠉⠉⠀⠀⠀⢠⣶⣾⣿⣿⣿⣿⣿⣶⣶⠀⠀⢀⡾⠋⠁⢠⡄⠀⣤⠀⢹⣿⣦⣿⡇⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣇⢸⣿⡇⠀⠀⣿⣧⠀⠈⣿⣷⠀⠀⢀⣀⠀⢙⣧⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⢀⣿⡏⠀⠀⠸⣇⠀⠀⠘⠛⠘⠛⠀⢀⣿⣿⣿⡇⠀⣼⣿⢻⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⣿⣸⣿⣿⠀⠀⣿⣿⣆⠀⢿⣿⡀⠀⠸⠟⠀⠛⣿⠃⠀⠀⢸⣿⡇⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠙⠷⣦⣄⡀⠀⢀⣴⣿⡿⣱⣾⠁⠀⣿⣿⣾⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣇⠀⢿⢹⣿⣆⢸⣿⣧⣀⠀⠀⠴⠞⠁⠀⠀⠀⠸⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⢀⣨⣽⣾⣿⣿⡏⢀⣿⣿⠀⣸⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣆⢸⡏⠻⣿⣦⣿⣿⣿⣿⣶⣦⣤⣀⣀⣀⣀⠀⣿⣷⠀⠀⠀⣸⣿⣏⣀⣤⣤⣶⣾⣿⣿⣿⠿⠛⢹⣿⣧⣼⣿⣿⣰⣿⣿⠛⠛⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠙⣿⣿⣦⣷⠀⢻⣿⣿⣿⣿⡝⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠉⠁⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣄⢸⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠟⠻⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡌⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

chica3 = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⠧⡿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⡏⣼⣿⣿⠿⠛⢘⣩⣵⠶⡆⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠻⢟⣛⣑⡤⠀⠀⢸⠀⢹⣛⡿⠼⠀⢸⣿⣿⣿
⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡿⢿⡟⠁⠀⠀⠈⠦⡀⠁⠀⠀⠀⠸⣿⣿⣿
⣿⣿⢡⢼⣿⣿⣿⣿⣿⣿⠁⠙⠂⠛⠉⠁⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⣿⣿⣿
⣿⣿⢸⠅⢿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⣿⣿⣿
⣿⣿⣧⣌⣚⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠀⠀⠀⠀⢠⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠐⠶⠦⠉⠐⠁⠀⠀⠀⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠈⠛⠷⣶⣤⣄⣀⡠⠊⡙⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠉⢹⠋⡀⠴⠧⠬⢿⣿⣿⣿⣿⣿
⠟⠛⢛⠯⡛⠻⠿⡿⡏⠻⣿⣿⢿⢧⣀⠀⠀⢠⠁⠀⠀⠈⠩⠭⠭⠽⣿⣿⣿⣿
⣀⣀⣀⡀⠻⣦⣀⣈⠈⢢⣻⣿⣆⣁⣀⣝⡆⣘⣀⡀⠀⢀⣀⢀⣤⣠⡛⢉⠛⣿
"""

chica4 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⣟⣿⢭⡭⠉⣠⣤⣷⡶⢆⡠⢤⣽⠯⣒⢭⣂⠀⠈⠙⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠞⢋⠝⠋⠀⠀⠀⠀⠀⠉⠐⠊⠑⠈⠑⠢⣤⢜⡟⠲⡀⠀⠙⠻⡿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠛⠁⢠⡖⠡⠀⠀⠀⠀⠀⠀⠀⠐⠢⢄⠀⠀⠀⠀⠈⠑⢭⠤⣿⢲⣄⠑⢌⢿⡛⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣼⠟⠁⠀⡰⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣝⢦⠀⠀⠀⠀⠈⠱⣬⡘⣮⣆⠀⠫⡻⣆⠈⢷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⡿⠀⠀⡜⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡻⣷⡀⠀⠀⠀⠀⢸⣿⢇⢹⢣⠀⠑⡙⣧⠀⠙⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⡟⠀⠀⡰⠀⡇⠀⠀⠀⠀⠀⠀⠀⢠⠈⡆⠀⡀⠀⠀⡈⢚⢿⡄⠀⠀⠀⠀⢹⣾⣭⣧⣃⠀⠐⡌⣧⠀⠘⢇⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠻⠀⠀⢠⠃⢸⡅⠀⠀⠀⠀⠀⠀⠀⠈⣴⢱⠐⡕⡀⢺⢷⠄⠪⢻⡀⠀⠀⠀⠀⠟⣎⢹⠙⡆⠀⠐⠘⣇⠀⠘⣆⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠈⠀⢸⣷⡀⠀⠀⠀⠀⡆⠀⠀⠘⢸⡆⠘⡀⠀⠁⠱⡀⠈⣷⠀⠀⠀⠀⠸⣸⣬⡘⢷⠀⠀⢣⠘⡆⠀⠹⡄⠀⠀
⠀⠀⢀⡟⡀⠀⠀⠀⠂⠀⣾⡇⠃⡄⠀⠀⠀⢰⠀⠀⡀⢸⡿⣆⠘⣄⠀⠀⠘⠔⡌⡄⠀⠀⠀⠀⠀⣯⠓⣼⡀⠀⡄⠇⣿⡄⠀⢇⠀⠀
⠀⠀⢸⢡⠁⠀⠀⠀⠀⣸⠇⡇⡄⢠⠀⠐⡄⠀⣧⠀⠁⢸⡃⠈⢣⡈⢷⡀⠀⠈⢮⡇⠀⠀⠀⠀⠀⢸⣷⡈⣇⠀⢱⠈⡘⣇⠀⢸⠀⠀
⠀⠀⡆⡿⠀⠀⠀⠀⠀⣿⣀⣱⣼⣬⣆⠀⢡⠀⠸⡄⢸⢻⠉⠉⠉⠙⢯⣿⣦⡄⣀⣻⠀⠀⠀⠀⠀⠀⣷⢧⣿⠀⠀⡇⢣⢹⡀⠸⡇⠀
⠀⢠⠹⡇⠀⠀⡀⡄⣿⡿⠀⠈⢎⣧⡸⣄⠀⣆⠀⢿⡌⣾⢀⡠⢤⣤⡤⣌⣻⣿⣶⣍⠀⠀⠀⠀⠀⠀⠻⣞⣻⡄⠀⠀⠈⡞⡇⠀⡇⠀
⠀⡌⡆⡇⠀⠀⢠⣧⢸⣗⣤⣿⣯⣽⣿⣿⠕⠼⠷⠌⠟⠿⣊⣺⣻⣿⣛⣻⣿⣿⣷⣿⡤⠀⠀⠀⠀⠀⠀⡇⢛⢣⠀⠀⠀⢰⢹⠀⡇⠀
⠀⢷⠃⡇⡇⢰⠀⢻⣔⣻⣿⡤⢿⡦⣬⣿⣄⠀⠀⢠⡖⠛⠉⠋⠹⡏⠻⠏⢿⣿⣿⡏⠁⠀⠀⠀⠀⠀⢸⢸⠸⣸⠀⠀⡄⠀⢏⣇⡇⠀
⢀⣼⠀⡇⢷⠀⡀⠀⢿⣯⡙⢧⣈⢣⣙⣹⣿⠿⠻⢿⣷⡄⠀⠀⠀⠘⠒⠚⢫⡿⠃⢇⠀⠀⠀⠀⠀⠀⢸⢸⣶⠃⠀⠀⡇⠀⠘⣿⠃⠀
⢸⡇⢸⡇⠈⢧⢡⠀⢸⣿⣷⡀⠉⢀⣀⣰⡿⠀⠀⠀⠹⢦⣤⣀⣤⣤⠤⠶⠟⠃⣼⢏⠀⠀⠀⠀⠀⠀⢸⣼⢹⠀⠀⠀⢰⠀⠀⢹⡀⠀
⢸⡇⢸⠇⠀⠈⢪⣷⣄⣻⡹⡟⠛⠋⠉⠁⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣫⡎⠀⠀⠀⠀⠀⠀⣼⢹⠸⠀⠀⠀⢸⠀⠀⠘⣇⠀
⠸⢣⢸⠀⡇⠀⠀⠉⣎⠹⣹⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠲⠿⠛⠁⡇⡀⠀⠀⠀⢸⢠⣿⢸⠁⠀⠀⠀⠈⠀⠀⠀⢻⠀
⠀⡼⣸⡄⣇⠀⠀⠀⢹⡄⢻⣾⣻⡄⠀⠀⠀⠀⠀⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢁⠇⠀⠀⠀⡀⣼⣄⡿⠀⠀⡀⠀⠀⡀⠀⠀⠸⡄
⠀⠱⣻⡇⡿⡄⠀⠀⠀⢻⡄⢻⠻⢿⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⡞⡟⣜⠆⠀⠀⣰⢣⣿⣿⠃⠀⢠⠀⢠⢠⡇⠀⠀⠀⡇
⠀⠀⠹⣷⡇⡷⡰⡄⠀⠈⢿⡜⡆⠀⡇⠈⠙⡦⣄⠀⠀⠀⠀⠀⣠⡴⢚⡽⠋⣸⣽⡟⠀⠀⣰⣏⣾⢟⡎⢀⡾⠃⢀⠆⢿⡇⠀⠀⠀⡇
⠀⠀⠀⡿⡿⡽⠳⣝⣦⡀⠀⢳⣽⣤⣇⠇⣴⡗⣿⠗⣦⣤⣶⠋⣁⠕⠋⣀⣼⠟⣽⠀⢀⣴⣿⠟⣽⡞⢠⡾⠁⢠⠊⡜⣾⠃⢠⠀⠀⠇
⠀⠀⢀⣷⣟⢁⠜⢉⠛⠿⣶⣤⣙⢿⣼⢰⢧⣽⡽⣰⠟⠋⢹⡞⠁⠀⠉⠉⣀⣼⣥⠖⣩⣿⣃⣸⠟⡱⠋⠀⠄⣡⠞⣽⣿⣴⢃⠄⣼⣶
⠈⠒⠋⠉⣿⠎⣠⠃⡰⢠⣢⡶⢉⠏⡽⢯⢞⣿⣽⣷⠀⢀⡼⣗⠒⠒⠈⠉⠉⠉⠀⡰⡿⣹⡏⢯⠞⢀⣴⡼⠚⣡⣾⣿⣽⠖⣡⡾⠟⠁
⠀⠀⠀⢠⡏⡜⠏⣰⣷⠟⢉⡴⡫⢚⣨⣿⣿⣿⣻⣿⣧⡞⣹⠿⡇⠀⠀⠀⠀⠀⢠⡿⢠⢻⣿⣫⠞⣋⣥⣲⢿⣿⣯⡭⣖⢺⡍⢷⣦⡀
⠀⠀⠀⢸⡟⢸⡴⠋⣠⣔⡽⣪⡴⣻⢿⡿⣿⢟⡟⠋⠙⢾⣀⠕⢹⡀⠀⠀⣠⣔⣺⠁⣿⡼⢛⡽⠟⠉⣠⢆⡾⠉⠒⢝⢾⣏⠟⣎⢪⠳
⠀⠀⢠⡿⡇⣾⣵⣻⣿⣿⣫⣔⡩⠋⢁⠞⠁⣼⠀⠀⠀⠀⠙⡶⠉⢧⠀⣼⣿⠿⣿⣼⣡⠞⢁⡤⣲⣾⣷⡽⠉⠑⢤⣀⣑⢛⣦⡸⣣⣇
⠀⠀⢿⣇⣿⢟⡽⢋⣿⡿⠟⠁⣀⠔⠁⠀⠀⠗⣒⢤⣀⡠⠊⠀⠀⠈⣿⢿⠏⡇⢻⣯⡶⠿⠟⠛⢉⢜⠝⠀⣠⠔⠉⠀⠀⠀⠀⠙⢿⡇
⠀⢠⣿⣿⣽⣫⣞⠿⠉⠀⣠⡞⠁⠀⢀⣼⠟⠸⠊⣰⡛⠀⡀⠀⠀⣴⡟⠸⢸⡷⣫⠗⢉⡠⢀⣴⡳⠋⣠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇
⢀⣼⣿⣿⣿⠝⠁⠀⣠⣾⠋⠀⠀⣠⡾⠁⢀⢞⠼⠤⠒⠁⠀⠀⣼⡱⢧⢠⡾⣏⠥⣊⣡⣶⠟⠉⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⢾⡿⣹⡻⠃⠀⢠⠞⡱⢁⠀⢀⡾⠋⠀⡴⡣⠃⠀⠀⠀⠀⡠⠋⡼⣇⢸⣼⣿⡿⠋⡝⣽⠃⢰⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘
⣼⡾⡛⠀⢀⠔⠃⢠⠁⠀⠑⣿⡁⢀⢾⠯⠀⠀⠀⠀⡠⠊⠀⢸⢱⣿⣾⠽⠋⣠⣞⣽⠟⠀⡎⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢷⡱⠁⢀⠊⠸⠀⢸⠀⠀⡞⣎⢇⡷⠃⠀⠀⠀⢀⠞⠁⢀⣼⢿⣾⣼⣡⣴⣭⠾⠿⠋⠀⠀⡟⢀⠀⠀⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰
⡟⠁⢰⠃⠀⠇⠀⢸⠀⠐⠃⠋⡸⠃⠀⠀⠀⡴⠁⠀⡴⠃⣸⣌⣿⢿⣫⡿⠛⠀⠀⠘⡄⣰⡇⡌⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⠀⠂⠀⠀⠀⠀⢸⠀⠐⠀⠀⡇⠀⠀⢠⠊⠀⢠⠎⢰⣿⣿⠟⡾⣿⡄⠀⠀⠀⠀⠀⠸⣻⢰⠀⢀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿
⣧⠀⠀⠀⠀⢰⠀⠀⡄⢸⠊⣶⠁⠀⡠⠁⠀⡠⠃⠀⠀⢩⡇⠸⠁⢿⣿⠀⠀⠀⠀⠀⢀⣿⠇⢠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⢸⢠⠀⠀⠀⠀⡆⠀⢧⠈⠘⢻⠀⡰⠁⠀⡰⠁⠀⠀⡠⢺⢀⠀⠁⢸⠁⠀⠀⠀⠀⠀⠀⡏⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠀
⠀⣏⡄⠀⠀⠀⠰⠀⠘⣆⠀⢸⡴⠁⠀⡰⠁⠀⢀⠚⠁⠈⣿⣄⠀⠸⡞⠀⠀⠀⠀⠀⠀⡷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿
"""

chica5 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠖⠋⠁⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⢶⡆⠀⠀⠀⠀⠀⢠⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠒⢉⣴⠟⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⢸⡇⠀⠀⣀⣸⡇⢸⣿
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠋⠀⡴⢻⡇⣴⡏⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣀⣤⣴⣿⣾⣿⠿⢿⣇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⢠⡎⣠⣿⣿⣿⣷⡀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⢻⠁⠀⠀⠀⠿⠀⠁
⠀⠀⠀⠀⠀⠀⢠⠁⠀⢠⡿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣴⣾⡿⠿⠛⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⣼⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡿⣿⠇⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠉⠘⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠀⢸⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣾⢿⣋⣾⠟⣡⣏⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠡⡀⢿⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⣿⣿⣿⣿⣿⣿⣿⣿⠟⠲⠿⠗⣾⠛⠁⠀⠋⠉⠉⠉⠙⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣆⢱⣸⣷⣶⠀⠀⠀⢰
⠀⠀⠀⠀⠀⠀⠀⠀⡷⣄⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣲⣤⣤⣸⡿⣿⣿⣿⣿⣿⣿⣿⣼⣿⡀⢿⣷⡆⠀⣿
⣄⠀⠀⠀⠀⠀⠀⠀⣧⣴⣿⣿⣿⣿⣿⣿⡿⣿⡛⢻⣿⣷⡶⠀⡄⠀⠀⠈⢉⡉⣿⣿⡿⢿⠁⢻⣿⣿⣿⣿⣿⣿⣿⡿⠧⠈⠉⠀⠀⢿
⣿⣷⣦⡀⠀⠀⠀⢠⣾⣿⣿⣿⣿⡟⢉⣿⡇⣿⡍⠉⠉⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⣸⠟⠼⣿⣿⣿⣿⣿⣷⣀⣠⣤⣤⣤⣤
⣿⣿⣿⣿⣿⡦⣰⠟⢡⣿⣿⣿⣿⡇⠀⢿⡇⠸⣷⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢀⡇⢠⠯⡅⢰⣿⣿⣿⣿⡿⢿⠟⠛⠉⣉⣉⣉
⣿⣿⣿⡿⠋⢠⠏⠀⣼⣿⣿⣿⣿⣿⣄⠸⣷⡀⠈⢣⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠈⣇⠤⠒⣡⣾⣿⣿⣿⣿⣶⣾⣶⣿⠿⠿⠛⠛
⣿⣿⣿⣧⠀⣎⠀⠀⡟⣿⣿⣿⣿⣿⣿⣷⣼⣷⠀⠈⣧⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⣿⣴⣾⣿⣿⣿⣿⣟⠛⣿⡁⣿⡟⠀⠀⢀⡀
⣿⣿⣿⣿⣧⢯⠑⠤⠱⣜⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⣿⣇⠀⠀⠀⠄⠈⠁⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⡿⣯⠉⠀⠈⢹⡇⢀⣼⣿⠁
⣿⣿⣿⣿⣿⣿⢆⠀⠀⡠⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡀⠀⠀⠀⠀⠀⢀⣤⠞⠉⣿⣿⣿⣿⣿⣿⣿⣧⠙⣧⡄⠀⠸⣿⠾⠟⢻⣇
⣿⣿⣿⣿⣿⣿⠆⢳⡜⢁⣾⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣠⣴⣾⡿⠃⠀⠀⣿⣿⣿⣿⠻⣿⣿⣿⡷⣌⣿⡆⠀⢠⣤⣤⡈⠻
⣿⣿⣿⣿⣿⠇⣀⠾⠀⣾⠃⣿⣿⣿⣧⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⣿⣿⣿⣿⣀⣿⣿⣿⠇⣸⡟⢳⣶⣿⣿⣿⣇⣼
⣿⣿⣿⢿⣿⣿⣤⣤⡑⣿⡠⠛⣿⣿⣿⣦⣿⣿⣿⣿⣿⠉⠉⠉⠛⠛⠁⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⢃⡴⡻⠀⢸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠏⠉⢣⣴⣿⣑⡿⣿⠿⣿⣿⣿⡹⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣧⣜⣿⣿⡉⠢⣇⠀⠘⠻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⣏⣀⣤⣴⣿⣿⣿⣿⣖⠛⠉⠉⠉⠉⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣉⡉⠉⠉⠁⠈⢒⣀⣠⣬⡻⣿⣿⣿
⣿⡿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢉⣶⣾⣿⣿⣿⣿⣿⠙⣿⣿
⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠤⠤⠤⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⡇⠙⣿
⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙
⠃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣀⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

craneo1 = """
⠀⠀⠀⠀⠀⠀⠀⢀⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⠀⠀⠀⠀⢀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣧⡀⠀⠀⣼⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⢀⣴⡶⠀⠀⠀⠀⠀
⠀⢸⣿⣧⠀⣰⡏⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣈⣧⠈⠻⣿⣦⣀⣀⠀⠀⠀⣸⣿⣿⣿⣆⠀⠀⠀⣴⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠘⡏⢿⣧⣿⠀⢀⣿⠁⠀⢀⣾⡇⠀⠀⠀⣀⠤⠖⠂⠉⠉⠀⠀⠀⠀⠀⠸⡏⣀⣀⣭⣷⣄⠉⠉⠒⢻⣿⣿⣿⣿⡆⢀⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⣤⣇⠘⣿⠇⠀⢸⡇⠀⢠⣾⣿⣀⡤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢻⣽⣿⣿⣿⣧⡀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⢸⣿⣿⡀⢻⡇⢠⡿⠀⣰⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣷⡀⢸⣿⣿⣿⣿⠏⠙⢿⣿⣿⣇⠀⠀⠀⠀⢀⣶
⢸⣿⣿⣧⣈⣧⡿⠁⢠⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣧⠈⣿⣿⣿⡏⠀⠀⣼⢹⣿⣿⠀⠀⠀⢀⣾⣿
⣿⡟⢿⣿⣿⣿⠁⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠳⡀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡆⢹⣿⣿⠁⠀⢀⢛⣼⣿⣿⠳⣄⢀⣾⣿⣿
⢻⡇⠀⢻⣿⣇⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠘⢦⣀⡀⠀⠀⠈⠻⣿⣿⣿⣇⠀⣿⡟⠀⠀⡞⣿⣿⣿⣿⠀⠘⣿⡗⣿⣿
⠈⣧⠀⠈⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠈⠙⡓⠶⣤⣄⡈⠻⣿⣿⣧⣸⡇⡆⠀⢳⣿⣿⣿⡇⠀⣸⣏⠁⣿⣿
⠀⠹⡆⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠉⠳⢦⡈⠛⠷⣿⣿⣿⣿⣅⠁⠀⣿⣿⣿⡟⠀⢰⣿⠃⠀⣼⣿
⠀⠀⢻⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⣄⣌⣲⣄⠸⣿⡿⣿⣿⣷⣴⣿⣿⠟⠀⠀⣿⡿⠀⠀⣸⡟
⠀⠀⠘⣿⡏⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⣿⣿⢿⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣷⣿⣧⠈⠻⢿⣿⣿⠋⠀⠀⢸⣿⠇⠀⣼⡿⣇
⠀⣀⡴⢋⣴⣿⣿⣿⣿⣿⡷⠿⣿⣿⣿⢣⣾⣿⣿⣿⣿⣷⣭⣙⠶⡄⠀⠀⢰⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣧⠀⠘⠛⣿⣆⠀⠀⣿⡇⠀⢀⣿⠇⢸
⠀⢻⠀⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠈⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⡄⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣇⠀⠀⠈⢻⡆⢸⠃⠀⠀⣾⠏⠀⢸
⠀⠈⡇⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⡀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣾⡄⠀⠀⢿⡟⠀⣠⣼⣿⠇⠀⢼
⠀⠸⣅⢷⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⡇⠀⠀⢧⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⢠⣿⣿⣿⡿⣿⣿⠀⠀⡟
⠀⣀⡿⠈⢿⣿⣿⡇⢻⣿⡗⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣸⠁⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⠿⠋⣴⣿⣿⠀⢀⡟
⠀⡿⠁⠀⠼⠛⢹⣯⣸⣿⣷⡄⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⡿⠛⠁⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠞⠉⢿⡿⠿⠟⣻⡟⠁⢠⡾⠛⢩⣿⣰⡿⠀
⠸⡇⠀⠀⠀⠀⢸⠇⠿⠋⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⠁⠀⠀⣠⡴⢻⣿⣿⣶⣶⣶⣾⡿⠀⡖⢸⡇⠀⢠⡟⣠⡾⣋⣴⣴⠟⣽⣿⠃⠀
⠀⢷⠀⢀⡾⣤⣼⣶⡖⠶⣿⠃⠀⠀⠀⠀⠀⢲⣷⣶⡶⠶⠆⣀⣀⣠⣴⠟⡟⠀⠀⠻⣿⣿⣿⣿⣿⠁⢨⠃⣸⣿⣦⣿⣟⣩⣾⡿⠋⣡⣾⣿⠃⠀⠀
⠀⠀⠉⠉⠀⢰⠏⠈⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣏⣴⣾⣿⡟⠁⠀⠀⣸⡇⠀⠀⠀⢿⠻⠿⢫⠏⠀⠀⠀⣿⣿⣿⣿⣿⠿⠁⣶⣴⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⢀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⣿⠏⣿⡇⠀⢀⣾⣿⠧⠀⠀⠀⢸⡄⣰⠟⠀⠀⠀⢠⣿⣿⣿⣯⣁⣠⣾⣿⣿⠟⠋⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠘⠋⢰⣿⣿⣶⡾⣿⣿⠇⠀⣠⠞⢉⠜⠁⡴⠀⢀⣴⡟⠉⠀⠉⠛⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣹⣶⡦⣴⢲⣴⢦⡤⣤⣤⣄⣤⣤⣤⣤⣤⣴⡿⠋⠙⢿⣯⣿⣿⠀⡰⠃⠀⠋⠀⡼⠁⠀⡞⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡏⣿⢰⡇⢰⠇⢸⡇⣸⣨⣇⣸⣏⣸⢇⣾⣿⣀⣠⠤⠤⠵⣫⠏⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣟⢿⢿⣿⣷⣿⣹⣇⣿⣸⣧⠥⠿⠴⠜⠋⠁⠀⠀⡴⠞⠁⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⢀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠛⠉⠉⠙⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣴⣶⠾⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⣠⣾⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⢀⣀⡀⣀⡀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⠶⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢷⣂⣀⣀⣀⣍⣳⣶⣾⣿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠛⠻⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

craneo2 = """
⠈⠈⠀⠁⠁⠈⠈⠁⠀⠐⠃⠈⠀⠀⠀⠀⠘⢚⠂⠁⠁⠈⠔⠐⠐⢋⠉⠃⠑⠋⢉⠊⠂⠙⠉⢍⠈⠈⠙⠐⠈⠁⠝⠉⠀⠚⠀⠋⠨⠁⠁⠀⠀⠙⠁⠆⠂⠈⠀⠀⠀⠀⠀⠀⠀
⡀⠀⠀⠀⠀⢀⠀⠀⡄⢀⡐⠐⣄⡒⡨⣀⣐⢀⡀⠂⠀⠐⠨⡀⠀⡀⠐⡰⠂⢀⠐⣀⠀⢊⡊⢀⠐⢀⢠⠀⠀⠀⢄⠐⠠⠀⠐⡗⡀⢂⡀⠸⠔⡲⡂⢒⠁⢀⢀⣠⣴⣾⠗⠀⠀
⠦⠀⠠⠄⠤⡀⠀⠀⠀⠄⣀⠀⡀⠀⠀⠀⠢⠀⠀⠢⠄⠀⠀⠐⠀⠘⠀⠀⢄⠀⠀⠀⠀⠀⠐⠆⠠⢀⠀⠀⡀⡀⠀⠄⠀⠦⠀⠺⢀⠀⠀⠠⠀⠀⠀⠀⠀⣴⣿⣿⠟⠁⠀⠁⣀
⣉⠀⠀⠀⠀⠀⠀⠠⠆⠂⠀⠀⠀⡀⠀⠐⠊⠰⠀⠀⡍⠀⠰⠄⠃⠴⠸⢀⠀⠀⠀⠈⠀⠀⠈⠈⢀⠀⢀⠀⠁⠁⠀⠀⡀⠐⠘⠀⠉⠖⠐⠂⠀⠂⡀⢧⣿⣿⣿⠃⢀⣠⣾⣶⡿
⠀⠀⠂⠄⠀⠀⠡⠒⠀⢠⠀⡀⠀⠀⠀⠀⠐⠀⠒⡆⢰⡄⠀⠀⠀⠐⠰⠀⣄⠁⢰⠀⠀⠁⠈⢠⠁⠉⡍⡌⠀⠀⢀⡀⠀⠀⠄⠁⠀⠂⠀⢠⡀⠀⢰⣿⣿⣿⠁⣠⣿⣿⠟⠋⠀
⠀⠠⠀⠀⠀⠀⠀⠀⠀⠅⠀⠊⠉⢀⣁⣦⣈⣀⣤⣤⣶⣦⣇⠀⠀⠀⠢⠀⠙⢧⡅⠀⠀⠀⠤⠠⠠⠁⠰⠀⢀⠈⠢⠠⠁⠀⠠⠁⠀⠁⠀⠠⠀⠂⢀⣿⣿⣿⣾⣿⣟⣁⣠⣴⣤
⠀⢀⠀⠐⠀⢀⠂⠑⠂⠠⠄⣠⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡷⣐⠰⠀⡂⠈⠳⢘⠀⠀⠰⠂⠆⠀⠂⠀⠂⢸⣦⣶⣿⣶⣦⣬⣈⡐⠀⠐⠂⣂⣴⣿⣿⣿⣿⣿⣿⣟⡛⠛⢉
⠀⠐⠀⢀⠂⠀⡣⢀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠠⢸⠠⠐⠀⢤⡋⠂⠄⠀⠃⢌⠊⡂⠈⠻⠿⠿⠿⠿⣿⣿⣯⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠿
⠀⠀⠀⠁⠀⣀⠨⠄⠀⢀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡁⠁⢃⢇⣀⠈⠓⣔⠀⠀⡐⠄⢀⠈⠀⠒⠒⠐⠀⡀⢙⠛⠻⠟⢋⣹⣿⣿⣿⣿⣽⡏⠿⠿⠋⠉⠀⠀
⠀⠈⠀⠀⢀⠐⠁⡀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠠⠨⠈⠘⣿⣆⠀⠘⡏⠀⠥⠽⠀⠐⠀⠌⠨⠤⠦⠀⢀⠀⠀⢄⣴⣾⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣐⠀⠁⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢸⠸⠀⠈⠻⣧⢀⠀⢸⣰⠀⢀⠀⣅⠀⠒⢈⠉⣁⠀⠦⢈⣤⣿⣿⣿⣿⢟⣿⣿⡆⡀⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠂⠀⠳⢿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⢳⣿⠆⠂⠰⡟⣷⣤⡐⢻⡆⢰⠀⠀⠀⡔⢐⠀⠄⠀⣦⣾⣿⣿⣿⡿⢃⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠊⠀⠐⠀⠈⠀⠸⠁⣶⣿⣿⣿⣸⡿⠿⠿⣿⣿⣿⣿⣥⣴⣿⡏⠾⣯⡹⢦⣄⣁⠄⡈⠀⣾⣏⢹⡆⠀⠀⠠⠉⠈⠀⠐⠿⣿⣿⣿⠟⢁⣾⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠢⠀⠀⠄⠀⠘⣿⣿⣯⣟⣷⣶⣾⣿⡿⢿⣿⣿⣿⣿⠇⠀⢼⣥⣾⣿⡏⡅⣠⢘⣿⣿⡾⣻⣗⠂⠂⠐⠀⣁⣥⣤⣿⣿⣯⣾⣿⣿⣿⣿⣿⠯⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠠⠀⠁⠀⠀⠀⠌⠈⠛⠿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡇⠄⠀⣼⣿⣿⣿⣿⣷⣥⣬⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡏⠃⠀⠀⠀⠀⠂⠀⠀⠀
⠀⠀⠀⣀⠀⠀⠀⠀⠈⠂⠀⡀⠑⣀⢀⣸⣿⣿⢿⣿⣿⣿⣿⢻⣿⣋⡓⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⡀⠀⠐⠀⠀⠠⠀⠀⠀⠀
⠀⡀⠀⠀⠉⠀⠀⢀⡀⠱⡄⠀⡀⠘⢽⣿⣿⣿⣷⣿⣿⣿⣿⣿⡿⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠛⠛⢻⠿⣿⣿⠿⠟⠿⠻⠿⠿⣿⣿⡿⣯⠄⠀⠀⠀⠁⠄⠀⠀⠀⢐⠀
⠀⠀⠀⠠⠂⠀⠈⡀⠀⠀⠉⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⢰⣿⣿⠟⠛⠿⣿⣿⣿⣿⣧⠠⠀⣦⣰⠽⠓⠉⠉⠚⡀⠒⠂⠀⠂⡈⢹⠷⡆⡀⠀⠀⠀⠀⠀⠀⠐⠀⠈⠀
⠀⠀⠀⠀⠌⠀⠀⠀⠀⠄⠸⡃⠀⠨⠀⢸⣿⣿⣿⣿⣽⣽⣿⣷⣶⣿⣿⢏⣴⣿⣿⣿⣿⣿⣽⣿⣆⡀⢉⡇⠓⠄⠘⠷⠄⠁⠁⢰⠈⢠⠡⠰⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀
⠀⠀⠀⣰⣴⡷⣺⣶⣧⡴⠿⣿⣀⣈⣥⣼⣿⣿⣿⣿⣿⣿⣿⣽⣛⣿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠩⠈⠀⠀⠁⠀⠅⠨⠀⠤⠀⠆⠀⠀⣤⣁⡀⠀⠀⠒⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢛⡃⣠⣿⣿⣿⣶⣾⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣯⠇⠠⠀⡀⠀⠐⡢⠁⡒⠃⠈⠦⡀⡀⢃⠂⠀⠙⢓⠀⠀⠀⠀⠀⠀⠀⠐⠀
⠀⢄⡀⢈⣱⣿⣿⣿⣿⡁⠀⠀⠀⠀⢠⣿⣟⣥⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣧⡀⠈⠁⠈⢈⠉⠀⠀⡋⠐⠈⠀⠁⡈⠀⠀⠈⠂⠀⠆⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀
⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣼⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⢟⣽⣿⣿⣿⣿⣿⣿⣷⣌⡈⠁⣀⠐⠀⡈⡁⠀⠐⠀⠈⡰⠀⠐⠆⠀⡀⢃⠀⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣁⣤⣾⣿⣿⣿⣫⣿⣿⣿⣿⣿⡿⢋⣠⣿⣿⣈⣻⣿⣿⡎⠥⣄⠱⠁⠁⠉⠠⠅⢀⢀⡉⡀⠁⢁⠄⡠⡁⠀⠀⠀⠀⠦⠀⠀⠀⠀⠀
⢚⣿⣿⣿⣿⣿⣿⡟⠛⢿⣿⣿⣿⣿⣿⣿⠿⠟⣋⣵⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⠿⢿⣿⣿⣿⣄⠀⢸⣂⠐⠃⠀⠈⠢⠆⢠⢂⠀⠀⡘⠀⠀⢌⡅⠀⠀⠐⠀⠀⡀⠀⠀⠀
⠀⠙⢙⣿⣿⣿⣿⡁⠀⠈⣿⣿⣿⣿⣿⣿⣯⣾⣿⠟⢛⣩⣿⣿⣿⣿⣿⣿⣯⣥⣴⣶⣶⣶⣮⣝⣿⣿⣷⣮⠿⠠⠤⠀⡀⠂⠈⠂⠄⠄⠀⠀⠈⠠⠄⡀⠀⠀⠁⠀⠀⠤⠀⠀⠀
⠀⢠⣾⣿⣿⣿⣿⠇⠄⠂⠙⠻⢻⣿⣿⣿⣿⣿⣧⣠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣛⠻⣿⣿⣿⡿⣿⡄⠐⠅⠠⠁⠀⠐⠑⠐⠀⠀⠐⠀⠂⠀⠂⠀⠀⠠⠀⠂⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⠀⠐⠃⠀⠀⢸⣿⣿⡟⣿⣿⣿⡿⢟⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡛⢿⣿⣿⢿⡗⠅⠀⠈⠠⠂⠀⠂⠌⠑⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⡛⠀⡀⠀⠄⣤⣾⣿⣟⣼⣿⣿⣿⣴⣿⣿⢯⣿⣿⣿⣿⢿⣿⡟⠻⠿⣿⣿⣿⣿⣿⣦⣹⣿⠀⠀⠔⣦⢄⠀⠀⢀⠄⠂⠈⠀⠀⡁⠀⠤⠀⠀⠀⡀⠀⠀⠀⢀⠀
⠀⣸⣿⣿⣿⣿⣷⡇⠀⠁⣶⣿⣿⡿⣾⣿⠟⠋⣿⣿⡟⣱⣿⡿⣿⣿⣿⣿⣿⣿⣆⠠⠆⠹⠿⠿⠛⠻⣿⣿⠐⠀⠠⢀⡀⠔⠀⢀⠈⠠⠀⠀⠔⠀⠀⢠⠀⠀⠀⠀⡀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⠹⡇⠀⠄⠸⣿⢿⣾⣿⡏⣰⢸⣿⣿⣹⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⡿⢀⣼⣿⣿⣦⠈⠂⣀⠄⠀⠀⠁⠐⢀⠂⠀⠂⢀⠆⠠⠀⠠⢀⠀⠀⠀⠀⢀⠀
⠀⢿⣿⣿⣿⣿⠀⠃⠂⠀⠀⠄⣘⣿⣿⡆⢱⣿⣿⡿⣿⣿⣷⣿⣿⠟⣼⣿⣿⣿⣿⣿⡉⠉⠤⣼⣿⣿⣿⡿⠿⠃⠂⠀⠐⠐⠑⠆⢠⠄⠒⠀⠈⠀⠑⠂⠂⠀⠀⠀⠀⠀⠀⠐⠀
⠀⣼⣿⣿⣿⡏⠰⠈⠀⠁⠀⠄⠀⠙⠻⠏⣿⣿⠟⠁⣿⣿⣿⣿⣡⣾⣿⢿⣿⣿⣿⣿⣿⠿⠶⠶⢀⣤⠀⠀⢀⡀⡄⢠⠀⠐⠀⠠⠠⡤⠂⠀⠄⠀⠂⠀⠀⠔⠢⠢⠧⡔⠔⠿⠄
"""

banners = random.choice([craneo1, craneo2, chica1, chica2, chica3, chica4, chica5])

lolcat_args = ["--animate", "-8"]
print(lolcat.lolcat(figlet.figlet_format("Stellar", font="cosmic"), args=lolcat_args))
spinner = Spinner("dots", text="Presiona [code][Enter][/code] para continuar", style="yellow")
with console.status(spinner):
    input("")

os.system("clear")

colores = random.choice(["red", "magenta", "yellow", "blue", "cyan"])

response = requests.get('https://ipapi.co//json/')
data = response.json()

if data is not None:
    ip = data.get("network")
    if ip is None:
        ip = "[bold red]La conexión de red es inestable.[/bold red]"
else:
    ip = "Ha ocurrido un error de red, posible fallo al iniciar Stellar."

console.print(
f"""[bold green]OS: [/bold green][bold white]{os_version}[/bold white]
[bold green]Sistema: [/bold green][bold white]{system_info}[/bold white]
[bold green]Fecha: [/bold green][bold white]{date_string}[/bold white]
[bold green]Hora: [/bold green][bold white]{hour_string}[/bold white]
[bold green]Tu ip anónima[bold red]/[/bold red]tu ip visible en el internet: [/bold green][bold white]{ip}[/bold white]""", justify="center")

console.print(f"[code]{banners}[/code]", justify="center", style=f"bold {colores}")


console.print("[bold red]Stellar V1.0.0[/bold red]", justify="center")

console.print("""
[code][bold green]
Para ver comandos utilice [/bold green] [bold white]menu [/bold white][/code]

[code][bold green]Hecho por [/bold green] [bold white]Keiji821 [/bold white][/code]
""", justify="center")