# Definir colores 

gris="${b}\033[1;30m"
blanco="\033[0m"
blanco2="$b\033[1;37m"
rojo="${b}\033[1;31m"
rojo2="${b}\033[31m"
azul="${b}\033[1;34m"
azul2="${b}\033[34m"
azul_agua="${b}\e[1;36m"
azul_agua2="${b}\e[36m"
verde="${b}\033[1;32m"
verde2="${b}\033[32m"
morado="$b\033[1;35m"
morado2="$b\033[35m"
amarillo="$b\033[1;33m"
amarillo2="$b\033[33m"
cyan="$b\033[38;2;23;147;209m"

# Configurar .bashrc a home

clear

cp ~/Stellar/config/.bash_profile ~/.
cp ~/Stellar/config/.bashrc ~/.

# Configurar archivos necesarios

cd
mkdir .configs_stellar
cd .configs_stellar
mkdir themes
cd themes

cat <<EOF > banner.py
import datetime
import os
from os import system
import platform
import random
import time
import requests
import subprocess
from pyfiglet import Figlet
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Spinner
from rich.text import Text

console = Console()

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")
hour_string = now.strftime("%I:%M%p")

os_version = os.sys.platform
system_info = platform.machine() + " - " + platform.processor()

with open("banner.txt", "r") as f:
    text_banner = f.read().strip()
with open("banner_font.txt", "r") as f:
    font = f.read().strip()

f = Figlet(font="cosmic")
text = f.renderText("Stellar")
console.print(text)
spinner = Spinner("dots", text="Presiona [code][Enter][/code] para continuar", style="yellow")
with console.status(spinner):
    input("")

os.system("clear")

colores = random.choice(["red", "magenta", "yellow", "blue", "cyan"])

response = requests.get('https://ipapi.co//json/')
data = response.json()

if data is not None:
    active = "[bold green]●[/bold green]"
    ip = data.get("network")
    if ip is None:
        ip = "El anonimizador no se ha iniciado"
        active = "[bold red]●[/bold red]"
else:
    active = "[bold red]●[/bold red]"
    ip = "Error de red"

console.print(
f"""[bold green]OS: [/bold green][bold white]{os_version}[/bold white]
[bold green]Sistema: [/bold green][bold white]{system_info}[/bold white]
[bold green]Fecha: [/bold green][bold white]{date_string}[/bold white]
[bold green]Hora: [/bold green][bold white]{hour_string}[/bold white]
[bold green]Tu IP tor/cloudflared: [/bold green][bold white]{active} {ip}[/bold white]""", justify="center")
console.print(" ")
f = Figlet(font=f"{font}")
banner_text = f.renderText(text_banner)

terminal_width = os.get_terminal_size().columns

centered_banner = "\n".join(
    line.center(terminal_width) for line in banner_text.splitlines()
)

process = subprocess.Popen(['lolcat'], stdin=subprocess.PIPE)
process.communicate(input=centered_banner.encode())
console.print(" ")
console.print("[underline][bold red]Stellar V1.0.0[/bold red][/underline]", justify="center")

console.print("""
[code][bold green]
Para ver comandos escriba [/bold green] [bold white]menu [/bold white][/code]

[code][bold green]Hecho por [/bold green] [bold white]Keiji821 [/bold white][/code]
""", justify="center")

os.system("""
cd
cd Stellar/config
git pull --force
cd
""")
EOF

cat <<EOF > ui_config.sh
# Definir colores

gris="\033[1;30m"
blanco="\033[0m"
blanco2="\033[1;37m"
rojo="\033[1;31m"
rojo2="\033[31m"
azul="\033[1;34m"
azul2="\033[34m"
azul_agua="\e[1;36m"
azul_agua2="\e[36m"
verde="\033[1;32m"
verde2="\033[32m"
morado="\033[1;35m"
morado2="\033[35m"
amarillo="\033[1;33m"
amarillo2="\033[33m"
cyan="\033[38;2;23;147;209m"

# ui_config.sh

printf "${verde}Ingrese el texto personalizado para su banner de inicio.\n"
read -p "Ingrese el contenido: " banner
echo "${banner}" > banner.txt
printf "${verde}Elija la fuente para su banner"
echo " "
printf "${amarillo}

1. 1row


2. 3-d


3. 3x5


4. 5lineoblique


5. acrobatic


6. alligator


7. alligator2


8. alphabet


9. avatar


10. banner


11. banner3-D


12. banner3


13. banner4


14. barbwire


15. basic


16. bell


17. big


18. bigchief


19. binary


20. block


21. bubble


22. bulbhead


23. calgphy2


24. caligraphy


25. catwalk


26. chunky


27. coinstak


28. colossal


29. computer


30. contessa


31. contrast


32. cosmic


33. cosmike


34. crawford


35. crazy


36. cricket


37. cursive


38. cyberlarge


39. cybermedium


40. cybersmall


41. diamond


42. digital


43. doh


44. doom


45. dotmatrix


46. drpepper


47. eftichess


48. eftifont


49. eftipiti


50. eftirobot


51. eftitalic


52. eftiwall


53. eftiwater


54. epic


55. fender


56. fourtops


57. fraktur


58. funface


59. funfaces


60. fuzzy


61. georgi16


62. ghost


63. ghoulish


64. glenyn


65. goofy


66. gothic


67. graffiti


68. hex


69. hollywood


70. invita


71. isometric1


72. isometric2


73. isometric3


74. isometric4


75. italic


76. ivrit


77. jazmine


78. jerusalem


79. katakana


80. kban


81. lcd


82. lean


83. letters


84. linux


85. lockergnome


86. madrid


87. marquee


88. maxfour


89. merlin1


90. merlin2


91. mike


92. mini


93. mirror


94. mnemonic


95. morse


96. moscow


97. nipples


98. ntgreek


99. o8


100. octal


101. ogre


102. pawp


103. pebbles


104. pepper


105. poison


106. puffy


107. pyramid


108. rectangles


109. relief


110. relief2


111. rev


112. roman


113. rot13


114. rounded


115. rowancap


116. rozzo


117. runic


118. runyc


119. sblood


120. script


121. serifcap


122. shadow


123. shimrod


124. short


125. slant


126. slide


127. slscript


128. small


129. smisome1


130. smkeyboard


131. smscript


132. smshadow


133. smslant


134. smtengwar


135. soft


136. speed


137. spliff


138. stacey


139. stampatello


140. standard


141. starstrips


142. starwars


143. stellar


144. stforek


145. stop


146. straight


147. striped


148. sub-zero


149. swampland


150. swan


151. sweet


152. threepoint


153. ticks


154. ticksslant


155. tinker-toy


156. tombstone


157. trek


158. tsalagi


159. twopoint


160. univers


161. usaflag


162. wavy


163. weird

"
echo " "
printf "${verde}"
read -p 'Fuente: ' font
echo "${font}" > banner_font.txt
echo " "
printf "${verde}Configure el texto de la input"
echo " "
printf "${verde}"
read -p 'Ingrese el contenido: ' input
echo "${input}" > input.txt
echo " "
printf "${gris}[$verde2✔$gris]${blanco2} Su banner personalizado se ha configurado correctamente!"
echo " "
echo " "
printf "${gris}[${verde}+${gris}] ${blanco2}Escriba ${verde}reload ${blanco2}para aplicar los cambios del banner."
echo " "
echo " "
printf "${gris}[${verde}+${gris}] ${blanco2}Escriba ${verde}bash ${blanco2}para aplicar correctamente el texto personalizado de la input."
echo " "
echo " "
cd
EOF

echo Stellar > banner.txt
echo standard > banner_font.txt
echo Stellar > input.txt
cd

# Actualizar paquetes

printf "${amarillo}[${verde}+${amarillo}] ${blanco2} Iniciando instalación"
echo
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Actualizando paquetes"
 echo
 apt-get upgrade -y && apt-get update -y
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"

# Instalar dependencias bash necesarias

printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando python"
 echo
 apt-get install -y python 
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando tor"
 echo
 apt-get install -y tor
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando cloudflared"
 echo
 apt-get install -y cloudflared 
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando exiftool"
 echo
 apt-get install -y exiftool
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando nmap"
 echo
 apt-get install -y nmap
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando dnsutils"
 echo
 apt-get install -y dnsutils
 sleep 5

# Instalar dependencias python necesarias

echo
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
sleep 1
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install beautifulsoup4
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install bs4
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install pyfiglet
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install phonenumbers
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install psutil
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install PySocks
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install requests
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install rich
pip install "rich[jupyter]"
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
pip install lolcat
echo
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
pip install discord
echo
clear
printf "${gris}[${verde}✔${gris}]${blanco} Instalación completada.\n"
sleep 5
cd Stellar/config
bash ui_config.sh
bash
reload
bash
