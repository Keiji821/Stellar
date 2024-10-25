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

mv .bashrc ~/

# Actualizar paquetes

clear

sleep 0.1

termux-toast -c green -b black "❕️ Iniciando instalación"

printf "$gris[$verde2+$gris]${blanco} Actualizando paquetes...$SECONDS\n"

sleep 1

printf "${verde2}"
pkg update && pkg upgrade --wait &>> /dev/null

sleep 1

clear

# Instalar dependencias bash necesarias

clear

sleep 0.1

printf "$gris[$verde2+$gris]${blanco} Instalando termux-api...$SECONDS\n"

sleep 1

printf "${verde2}"
pkg install termux-api --wait &>> /dev/null

sleep 1

clear

printf "$gris[$verde2+$gris]${blanco} Instalando python...$SECONDS\n"

sleep 1

pkg install python &>> /dev/null

sleep 1

clear

printf "$gris[$verde2+$gris]${blanco} Instalando tor...$SECONDS\n"

sleep 1

pkg install tor &>> /dev/null                                                                                                                                  sleep 1                                                                          
clear

printf "$gris[$verde2+$gris]${blanco} Instalando cloudflared...$SECONDS\n"

sleep 1

pkg install cloudflared &>> /dev/null                                                                                                                                  sleep 1                                                                          
clear

# Instalar dependencias python necesarias

printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"

sleep 1

clear

printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
pip install beautifulsoup4 &>> /dev/null
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
pip install bs4 &>> /dev/null
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
pip install colorama &>> /dev/null
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
pip install phonenumbers &>> /dev/null
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
pip install psutil &>> /dev/null
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
pip install PySocks &>> /dev/null
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
pip install requests &>> /dev/null
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
pip install tabulate &>> /dev/null
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
pip install tqdm &>> /dev/null
clear
printf "$gris[$verde2✔$gris]${blanco} Instalación completada.\n"
<<<<<<< HEAD
reload
sleep 1
termux-toast ✅️ Stellar Instalado correctamente
=======
clear
python Stellar/banner.py
sleep 0.1
termux-toast -c green -b black "✔ Stellar instalado correctamente"
>>>>>>> 2086317 (Stellar V1.0)
