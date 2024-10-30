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

cp ~/Stellar/.bash_profile ~/.
cp ~/Stellar/.bashrc ~/.

# Actualizar paquetes

printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando termux-api."
 echo
 pkg install -y termux-api
 sleep 5

termux-toast -c green -b black "Iniciando instalación"

printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Actualizando paquetes."
 echo
 pkg update -y && pkg upgrade -y
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"

# Instalar dependencias bash necesarias

printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando python."
 echo
 pkg install -y python 
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando tor."
 echo
 pkg install -y tor
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando cloudflared."
 echo
 pkg install -y cloudflared 
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando exiftool."
 echo
 pkg install -y exiftool
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"

# Instalar dependencias python necesarias

echo
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
sleep 1
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install beautifulsoup4
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install bs4
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install colorama
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install phonenumbers
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install psutil
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install PySocks
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install requests
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install tabulate
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install tqdm
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install yattag
clear
sleep 5
printf "$gris[$verde2✔$gris]${blanco} Instalación completada.\n"
sleep 15
bash
termux-toast -c green -b black "✔ Stellar instalado correctamente"
