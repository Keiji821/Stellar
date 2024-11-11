import datetime
import os
from os import system
import platform
import random
import time
import pyfiglet
from pyfiglet import Figlet
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Spinner

console = Console()

def get_current_time():
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    hour_string = now.strftime("%I:%M%p")
    return date_string, hour_string

def get_system_info():
    os_version = os.sys.platform
    system_info = platform.machine() + " - " + platform.processor()
    return os_version, system_info

blackhole1 = """
⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢠⢀⡐⢄⢢⡐⢢⢁⠂⠄⠠⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⣌⠰⣘⣆⢧⡜⣮⣱⣎⠷⣌⡞⣌⡒⠤⣈⠠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⠱⡜⣞⣳⠝⣘⣭⣼⣾⣷⣶⣶⣮⣬⣥⣙⠲⢡⢂⠡.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⣑⢣⠝⣪⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣯⣻⢦⣍⠢⢅⢂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢆⡱⠌⣡⢞⣵⣿⣿⣿⠿⠛⠛⠉⠉⠛⠛⠿⢷⣽⣻⣦⣎⢳⣌⠆⡱.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠠⠌⢢⢃⡾⣱⣿⢿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣏⠻⣷⣬⡳⣤⡂⠜⢠⡀⣀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠂⣌⢃⡾⢡⣿⢣⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⡊⣿⣿⣾⣽⣛⠶⣶⣬⣭⣥⣙⣚⢷⣶⠦⡤.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠂⠰⡌⡼⠡⣼⢃⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⠿⣛⣯⡴⢏⠳⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠑⡌⠀⣉⣾⣩⣼⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣿⣿⣿⣿⡿⢛⣛⣯⣭⠶⣞⠻⣉⠒⠀⠂
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡶⢝⣢⣾⣿⣼⣿⣿⣿⣿⣿⣀⣼⣀⣀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⠿⡛⠏⠍⠂⠁⢠⠁
⠀⠀⠀⠠⢀⢥⣰⣾⣿⣯⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣽⠟⣿⠐⠨⠑⡀⠈
⠀⠀⡐⢢⣟⣾⣿⣿⣟⣛⣿⣿⣿⣿⣿⢿⣝⠻⠿⢿⣯⣛⢿⣿⣿⣿⡛⠻⠿⣛⠻⠛⡛⠩⢁⣴⡾⢃⣾⠇⢀⠡⠂
⠀⠀⠈⠁⠊⠙⠉⠩⠌⠉⠢⠉⠐⠈⠂⠈⠁⠉⠂⠐⠉⣻⣷⣭⠛⠿⣶⣦⣤⣤⣴⣴⡾⠟⣫⣾⣿⡏⠀⠂⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⢿⢶⣤⣬⣉⣉⣭⣤⣴⣿⣿⡿⠃⠄⡈⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠘⢊⠳⠭⡽⣿⠿⠿⠟⠛⠉⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠈⠐⠀⠘⠀⠈⠀⠈
"""

planet1 = """
 ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠃
⠀⠀⠀⠀⠀⠀⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀
⠀⠀⠀⠀⠀⠀⠀⠘⠏⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠈⠙⠦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⣶⣒⣶⠦⣤⣀
⠀⠀⠀⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠲⡌⠙⢦⠈⢧
⠀⠀⠀⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡴⢃⡠⠋⣠⠋
⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⢖⣋⡥⢖⣫⠔⠋
⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣩⠭⢵⣒⣻⠭⢖⠏⠁⢀⣀⠀⠀⠀⠀
⠠⠀⠈⠓⠒⠦⠭⠭⠭⣭⠭⠭⠭⠭⠿⠓⠒⠛⠉⠉⠀⠀⣠⠏⠀⠀⠘⠞
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆⠀
⠀⠀⠀⠀⠀⠘⠿⠀⠀⠀⠀⠀⠈⠉⠙⠒⠒⠛⠉⠁⠀⠀⠀⠉⢳⡞⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

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
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡠⠂⣵⡿⡉⡠⢔⠂⢉⠑⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣮⠋⢠⡟⡉⠀⢱⡐⡅⠘⢷⡀⠱⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⢡⣆⡳⢡⣼⢀⣿⢷⣼⣔⣌⢷⢠⢿⡄⠀⠀⠀⠀
⠀⠀⠀⢸⣿⢸⢸⣵⡿⠿⠿⠋⠀⠟⠉⠻⣾⡇⣾⣷⠀⠀⠀⠀
⠀⠀⠀⢸⡇⢸⡼⢃⣠⣤⠀⠀⠀⠤⠤⠤⠨⢣⢸⡿⣇⠀⠀⠀
⠀⠀⠀⠀⡇⢸⣯⠁⠀⢠⡀⠀⠀⠀⣤⣀⣤⢼⠄⣷⢹⠀⠀⠀
⠀⠀⠀⣿⣷⢸⣧⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⣼⠀⣿⢸⡇⠀⠀
⠀⠀⠀⣿⣿⠈⣿⣦⠀⠀⠀⠀⠀⡀⠀⢀⠔⣽⠀⡏⣼⡇⠀⠀
⠀⠀⠀⢹⣟⡀⣿⣯⢢⡀⠀⠈⠁⠀⠀⣠⣜⣿⡆⣷⣿⠃⠀⠀
⠀⠀⠀⢸⡻⣷⣸⣿⢿⠹⣱⣶⣤⣴⡾⣿⣚⣿⣷⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠈⢻⣿⣷⣺⡟⠈⠉⠁⠀⢻⣷⣞⡁⠀⠀⠀⠀⠀
⠀⠀⢠⡖⠺⣇⠀⠈⠉⠈⡆⠐⠢⠀⠤⡴⠀⠈⠙⠒⠤⣀⡀⠀
⠀⠀⡇⢃⠀⡝⢷⣄⠀⠀⢹⠛⠛⠻⡶⠁⠀⠀⣀⣴⠟⠁⢹⡄
⠀⢰⠃⠸⡄⡜⠀⠙⢷⢤⣌⣆⠀⣴⣀⣤⣴⡾⠛⡅⢠⢠⠃⡅
⠀⢸⠀⠀⢳⠞⠀⠀⠀⡱⢐⣿⣛⡟⢡⠐⠁⠀⠘⢀⢸⠃⠀⡇
⠀⠀⠀⠀⢸⠀⠀⠀⠰⠁⡾⢹⢸⠈⡇⠡⠀⠀⠀⢸⡏⠀⠀⢳
⠀⢸⠀⠀⢸⡀⠀⠀⡆⠀⠠⡃⠈⢪⠉⠀⡇⠀⠀⠈⡇⠀⠀⡏
⠀⢸⠀⠀⢸⢱⠀⠀⡇⡔⠅⢧⠀⠀⠣⡀⡇⠀⠀⡄⡇⠀⠀⡇
⠀⢸⡄⠀⢸⠈⡆⠀⠛⠀⠠⠈⠀⠀⠀⠘⠇⠀⠈⡄⡇⠀⢰⠀
⠀⡇⢀⣀⢸⡄⠘⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀
⢰⣇⠀⠙⢫⠀⠀⠣⠀⠀⠀⠀⠁⠀⠀⠀⠀⡆⠀⠐⡇⠀⢸⣦
⢸⣿⣿⢶⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⣯⣤⣾⣟
⠈⠟⠻⠿⢿⡟⠛⠒⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣿⣾⣿⠟
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
⠀⠀⠀⠀⠀⣶⡆⠀⠀⠀⢀⣴⢦⠀⠀⠀⠀⣖⡶⠀⠀⠀⠀⡏⡧
⠀⠀⠀⠀⠀⢹⣷⡀⠀⠀⢀⣿⣧⡀⠀⠀⢠⣾⣧⠀⠀⠀⣠⣾⡇
⠀⠀⠀⠀⠀⢸⣿⣿⣦⡀⣼⣿⣿⣷⡀⢠⣿⣿⣿⡆⢀⣾⣿⣿⡇
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠋⠙⢿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠠⣤⣉⣙⠛⠛⠛⠿⠿⠁⣴⣦⡈⠻⠛⠛⠛⢛⣉⣁⡤
⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠶⣶⣆⠈⢿⡿⠃⣠⣶⡿⠿⠟⠛⠉
⠀⠀⠀⠀⠀⢠⣿⣿⣶⣶⣤⣤⣤⣤⡀⢁⣠⣤⣤⣤⣶⣶⣿⣿⡀
⠀⠀⠀⠀⠀⣸⣿⡏⠉⠙⠛⠿⢿⣿⣿⣾⣿⡿⠿⠛⠋⠉⠹⣿⡇
⠀⠀⠀⠀⠀⠻⢿⣧⣀⠀⠀⣀⣀⣼⡿⣿⣯⣀⣀⠀⠀⣀⣼⡿⠗
⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⠁⠘⣿⣿⣿⣿⣿⠟⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣇⣀⣀⣹⣿⣿⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠿⣿⡿⢿⣿⠿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⢀⣿⡇⢸⣿⡀⢸⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠈⠉⠁
"""

craneo2 = """
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

craneo3 = """
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

banners = random.choice([craneo1, blackhole1, craneo2, planet1, craneo3, chica1, chica2, chica3, chica4, chica5])

console.print(pyfiglet.figlet_format("Stellar", font="cosmic"))
spinner = Spinner("dots", text="Presiona [Enter] para continuar", style="yellow")
with console.status(spinner):
    input("")

os.system("clear")

colores = random.choice(["red", "magenta", "yellow", "blue", "cyan"])

console.print(f"[{colores}]{banners}[/colores]")

console.print("")
MARKDOWN = "> **Stellar V1.0**"
md = Markdown(MARKDOWN)
console.print(md, justify="center")  # Centrar el texto

console.print("""
[code][bold green]
Para ver comandos utilice [/bold green] [bold white]menu [/bold white][/code]

[code][bold green]Hecho por [/bold green] [bold white]Keiji821 [/bold white][/code]
""", justify="center")