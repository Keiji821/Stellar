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

printf "${verde}"
 read -p 'Ingrese el contenido: ' banner
 echo "${banner}" > banner.txt
 echo
 printf "${gris}[$verde2✔$gris]${blanco2} Su banner personalizado se ha configurado correctamente!"
 echo " "
 echo " "
 printf "${gris}[${verde}+${gris}] ${blanco2}Escriba ${verde}reload ${blanco2}para aplicar los cambios."
 echo " " 
 echo " "