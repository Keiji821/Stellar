#!/bin/bash

gris="\033[1;30m"
blanco="\033[0m"
blanco2="\033[1;37m"
rojo="\033[1;31m"
rojo2="\033[31m"
azul="\033[1;34m"
azul2="\033[34m"
azul_agua="\033[1;36m"
azul_agua2="\033[36m"
verde="\033[1;32m"
verde2="\033[32m"
morado="\033[1;35m"
morado2="\033[35m"
amarillo="\033[1;33m"
amarillo2="\033[33m"
cyan="\033[38;2;23;147;209m"

user_file="user.txt"

echo -ne "${azul}¿Desea configurar un nombre de usuario? (y/n) ${blanco}"
read respuesta

if [ "$respuesta" = "y" ] || [ "$respuesta" = "Y" ]; then
    echo -ne "${verde}Introduce tu nombre de usuario: ${blanco}"
    read username
    echo "$username" > "$user_file"
    echo -e "${verde}Usuario guardado en $user_file${blanco}"
elif [ "$respuesta" = "n" ] || [ "$respuesta" = "N" ]; then
    if [ -f "$user_file" ]; then
        username=$(cat "$user_file")
        echo -e "${azul}Usuario actual: ${cyan}$username${blanco}"
    else
        echo -e "${rojo}No hay usuario configurado${blanco}"
    fi
else
    echo -e "${rojo}Opción no válida${blanco}"
fi