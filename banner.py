from colorama import init, Fore, Back, Style
import datetime
import os
import platform
from tabulate import tabulate

init()

os_version = os.sys.platform

system_info = platform.machine() + " - " + platform.processor()

# Mostrar fecha y hora

now = datetime.datetime.now()

date_string = now.strftime("%Y-%m-%d")

hour_string = now.strftime("%I:%M%p")

# Definir banners

banner = """
....    .........                     ......     .  .
.  ...    .....  ..     .... ........     .....  . .  .
.  ..    ...     . .....;ldk0kd0o00kxo,'........      .
.  ..           .. .'cdxO0xl;'.'.,cdOdO00x:......     .
.  .          . .,lkOOkd,. .:lool:...okkdxxkd:....    .
..          ...:k000k0x. ,x00kddxOkoolck0kO0Ok:...    .
 .          .;O000OO0O. ;0ko....;cxOl  xk0kkx:.....  ..
  .      ...dOkkkkxkko  o0d,....'oO0: .Oxl;........  ..
        ..'O000000000k..;okklcox000c............... ...
   .     .xkxO00Oxxxodx; .:dkOOkdc'....................
         .okkxkkOOkO000xc:;,. .........................
           'oO00000kxxlxOxc,...........................
.      ........:locll,;,...............................
...   .................................................
 ....  ................................................
"""

# Mostra banner

table_data = [

[banner],

]

print(Fore.RED + Back.BLACK + tabulate(table_data + tablefmt="fancy_grid") + Style.RESET_ALL)
print(Style.BRIGHT + Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "]", Fore.WHITE + "Stellar [V1.0]" + Style.RESET_ALL)
print(Style.BRIGHT + Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "]", Fore.WHITE + "Comandos: menu", Style.RESET_ALL)
print(Style.BRIGHT + Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "]", Fore.WHITE + "Hora actual: " + hour_string + " │ Fecha: " + date_string + Style.RESET_ALL)
