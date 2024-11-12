import datetime
import os
from os import system
import platform
import random
import time
import requests
import pyfiglet
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

console.print(pyfiglet.figlet_format("Stellar", font="cosmic"))
spinner = Spinner("dots", text="Presiona [code][Enter][/code] para continuar", style="yellow")
with console.status(spinner):
    input("")

os.system("clear")

colores = random.choice(["red", "magenta", "yellow", "blue", "cyan"])

response =
requests.get(f'https://ipapi.co/ /json/')
data = response.json()

ip = data.get("network")

console.print(
f"""[bold green]OS: [/bold green][bold white]{os_version}[/bold white]
[bold green]Sistema: [/bold green][bold white]{system_info}[/bold white]
[bold green]Fecha: [/bold green][bold white]{date_string}[/bold white]
[bold green]Hora: [/bold green][bold white]{hour_string}[/bold white]
[bold green]Tu IP tor actual: [/bold green][bold white]{ip}[/bold white]""", justify="center")

console.print(f"[bold {colores}]{banners}[/bold {colores}]", justify="center")


console.print("[bold red]Stellar V1.0.0[/bold red]", justify="center")

console.print("""
[code][bold green]
Para ver comandos utilice [/bold green] [bold white]menu [/bold white][/code]

[code][bold green]Hecho por [/bold green] [bold white]Keiji821 [/bold white][/code]
""", justify="center")