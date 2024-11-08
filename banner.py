import datetime
import os
from os import system
import platform
import random
import time
import sys
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
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⢿⣶⢶⣶⣶⣦⣄⣤⠖⠒⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣼⣭⣿⣿⣯⣷⣿⣿⠛⠀⣀⠘⣆⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⢿⡽⣻⣿⣿⣯⣿⣿⣷⣄⣀⣨⠖⠻⣄⠀⠀⠀
⠀⠀⠀⣾⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⣿⣿⣿⣄⡠⢏⠉⠓⢄
⠀⠀⣸⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣷⣿⣿⣿⣿⣿⣿⡆⠀⠀⣠⠔
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣷⣤⣾⡏⠀
⠀⢰⣿⡿⣿⣿⣻⣿⣿⣿⣿⡿⢿⣿⣿⡿⠁⢹⣿⣮⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⢷⣿⣿⣿⣿⡿⢿⣙⢦⣿⣿⠏⠀⡰⣎⡽⠿⣿⣿⣿⣿⣿⣿⣧⠀
⢀⡞⠤⣀⢹⣿⡟⣹⣷⢶⣏⠉⡿⠋⠀⠀⠈⣿⡿⣿⡮⢻⣿⣿⣥⠖⠘⡇
⠈⢇⠘⠈⠻⣿⡇⠙⠿⠿⠃⠀⠀⠀⠀⠀⠀⠘⠻⠟⠁⢸⣿⣿⠋⠃⢀⡏
⠀⠘⢦⣤⣠⣿⡗⠁⠒⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠛⠋⢹⣿⣿⣤⣶⡟⠀
⠀⠀⣼⣿⣿⣿⣿⣄⠀⠀⠀⠀⢤⡀⠀⠀⣠⠄⠀⠀⣠⣿⣿⣿⣿⣿⡇⠀
⠀⢠⣿⣿⣿⣿⣿⣽⣷⣤⡀⠀⠀⠉⠛⠉⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣿⣟⣏⣿⣿⣿⣿⣷⣶⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠰⣿⣿⢻⣯⣿⣿⣿⣿⣿⡧⠉⠉⠉⠉⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⠀⠀⣿⣿⣾⣿⣿⡿⢿⠛⠉⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣻⣿⣿⣿⠀
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣖⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣄⣀⣠⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀
⠠⣾⣿⢿⣿⣿⣿⣿⡿⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠉⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡿⠑⠊⣿⣿⡿⠿⠛⠛⠙⠛⣻⣿⣿⣄⡻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡗⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠟⠛⠻⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠀⠀⠀⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢶⡋⠳⢸⣿⣿⣿⣿⣿⣇⠀
⠀⠂⠀⠀⠘⣿⣿⣿⡀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡗⠚⢁⣠⣾⣿⣿⣿⣿⣿⣿⠀
⠀⠉⠀⠀⠀⠈⣻⣿⣿⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⠀⢺⣿⠤⠿⢿⣿⣿⣿⣿⣿⣿⣷⣶⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⣀⡠⠜⠋⠁⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡿⠛⣠⣟⣁⠤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠀⠀⠀⠀⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢸⠿⠃⠀
⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦
⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆
"""

banners = random.choice([blackhole1, planet1, chica1, chica2, chica3, chica4, chica5])

spinner = Spinner("dots", text="Presiona [Enter] para continuar", style="yellow")
with console.status(spinner):
    input("")

os.system("clear")

def animate_banner(banner_text, delay=0.001):
    colors = random.choice(["blue", "yellow", "cyan", "white", "red", "green"])
    for char in banner_text:
        color = random.choice(colors)
        console.print(char, end="", style=f"bold {color}")
        sys.stdout.flush()
        time.sleep(delay)
    console.print()

animate_banner(banners)

print("")
MARKDOWN = """
> **Stellar V1.0**
"""
md = Markdown(MARKDOWN)
console.print(md)
console.print("""[bold green]
Para ver comandos utilice:[/bold green][bold white] menu[/bold white]                        
[bold green]Hecho por: [/bold green][bold white]Keiji821
[/bold white]""")
print(" ")