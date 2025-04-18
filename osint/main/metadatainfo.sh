#!/bin/bash

b="\033[1m"
gris="${b}\033[1;30m"
blanco="\033[0m"
blanco2="${b}\033[1;37m"
rojo="${b}\033[1;31m"
rojo2="${b}\033[31m"
azul="${b}\033[1;34m"
azul2="${b}\033[34m"
azul_agua="${b}\e[1;36m"
azul_agua2="${b}\e[36m"
verde="${b}\033[1;32m"
verde2="${b}\033[32m"
morado="${b}\033[1;35m"
morado2="${b}\033[35m"
amarillo="${b}\033[1;33m"
amarillo2="${b}\033[33m"
cyan="${b}\033[38;2;23;147;209m"

termux-setup-storage &>/dev/null &
sleep 5

cd
cd storage
echo
printf "${verde}Directorios ⤵\n"
echo
ls
printf "${verde}\n"
read -p 'Directorio: ' directorio

if [ -d "$directorio" ]; then
    cd "$directorio"
else
    printf "${rojo}¡Directorio no encontrado!${blanco}\n"
    exit 1
fi

echo
printf "${amarillo}Recuerda escribir el nombre de las carpetas sin las comillas.\n"
printf "${verde}Carpetas ⤵\n"
echo
ls
printf "${verde}\n"
read -p 'Carpeta: ' carpeta

if [ -d "$carpeta" ]; then
    cd "$carpeta"
else
    printf "${rojo}¡Carpeta no encontrada!${blanco}\n"
    exit 1
fi

echo
printf "${verde}Archivos ⤵\n"
echo
ls
printf "${verde}\n"
read -p 'Archivo: ' imagen

if [ -f "$imagen" ]; then
    echo
    printf "${rojo}                           Datos del archivo\n"
    printf "${amarillo}╭──────────────────────────────────┳──────────────────────────────────\n"
    exiftool "${imagen}" | while IFS= read -r line; do
        campo=$(echo "$line" | cut -d: -f1)
        valor=$(echo "$line" | cut -d: -f2-)
        printf "│ ${campo} │ ${valor}\n"
    done
    printf "${amarillo}╰──────────────────────────────────┴─────────────────────────────────\n"
else
    printf "${rojo}¡Archivo no encontrado!${blanco}\n"
    exit 1
fi