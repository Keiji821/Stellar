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

clear

sleep 0.1

termux-toast -c green -b black "Iniciando instalación"

printf "$gris[$verde2+$gris]${blanco} Actualizando paquetes...$SECONDS\n"

sleep 1

echo
pkg update && apt upgrade &

sleep 10

clear

# Instalar dependencias bash necesarias

clear

sleep 0.1

printf "$gris[$verde2+$gris]${blanco} Instalando termux-api...$SECONDS\n"

sleep 1

echo
pkg install termux-api &

sleep 1

clear

printf "$gris[$verde2+$gris]${blanco} Instalando python...$SECONDS\n"

sleep 1

expect -c "
spawn pkg install python
expect "Do you want to continue? [Y/n] "
send "y"
expect eof
"

sleep 1

clear

printf "$gris[$verde2+$gris]${blanco} Instalando tor...$SECONDS\n"

sleep 1

echo
pkg install tor &                                                                                                                   sleep 1                                                                          
clear

printf "$gris[$verde2+$gris]${blanco} Instalando cloudflared...$SECONDS\n"

sleep 1

echo
pkg install cloudflared &                                                                                                                         sleep 1                                                                          
clear

printf "$gris[$verde2+$gris]${blanco} Instalando exiftool...$SECONDS\n"

sleep 1

echo
pkg install exiftool &                                                                                                                      sleep 1                                                                          
clear

# Instalar dependencias python necesarias

printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"

sleep 1

clear

printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install beautifulsoup4 &
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install bs4 &
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install colorama &
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install phonenumbers &
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install psutil &
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install PySocks &
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install requests &
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install tabulate &
clear
printf "$gris[$verde2+$gris]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install tqdm &
clear
sleep 5
echo
printf "$gris[$verde2✔$gris]${blanco} Instalación completada.\n"
sleep 1
clear
python banner.py
sleep 0.1
termux-toast -c green -b black "✔ Stellar instalado correctamente"
