#!/bin/bash

Negro="\033[0;30m"
Rojo="\033[0;31m"
Verde="\033[0;32m"
Amarillo="\033[0;33m"
Azul="\033[0;34m"
Magenta="\033[0;35m"
Cian="\033[0;36m"
Blanco="\033[0;37m"

Negro_Brillante="\033[1;30m"
Rojo_Brillante="\033[1;31m"
Verde_Brillante="\033[1;32m"
Amarillo_Brillante="\033[1;33m"
Azul_Brillante="\033[1;34m"
Magenta_Brillante="\033[1;35m"
Cian_Brillante="\033[1;36m"
Blanco_Brillante="\033[1;37m"

Fondo_Negro="\033[40m"
Fondo_Rojo="\033[41m"
Fondo_Verde="\033[42m"
Fondo_Amarillo="\033[43m"
Fondo_Azul="\033[44m"
Fondo_Magenta="\033[45m"
Fondo_Cian="\033[46m"
Fondo_Blanco="\033[47m"

Fondo_Negro_Brillante="\033[0;100m"
Fondo_Rojo_Brillante="\033[0;101m"
Fondo_Verde_Brillante="\033[0;102m"
Fondo_Amarillo_Brillante="\033[0;103m"
Fondo_Azul_Brillante="\033[0;104m"
Fondo_Magenta_Brillante="\033[0;105m"
Fondo_Cian_Brillante="\033[0;106m"
Fondo_Blanco_Brillante="\033[0;107m"

Reset="\033[0m"
Negrita="\033[1m"
Atenuado="\033[2m"
Italico="\033[3m"
Subrayado="\033[4m"
Parpadeo="\033[5m"
Invertido="\033[7m"
Oculto="\033[8m"
Tachado="\033[9m"

termux-setup-storage &>/dev/null &
sleep 5

cd
cd storage
echo
printf "${Verde_Brillante}Directorios ⤵\n"
echo
ls
printf "${Verde_Brillante}\n"
read -p 'Directorio: ' directorio

if [ -d "$directorio" ]; then
    cd "$directorio"
else
    printf "${Rojo_Brillante}¡Directorio no encontrado!${Blanco_Brillante}\n"
    exit 1
fi

echo
printf "${Amarillo_Brillante}Recuerda escribir el nombre de las carpetas sin las comillas.\n"
printf "${Verde_Brillante}Carpetas ⤵\n"
echo
ls
printf "${Verde_Brillante}\n"
read -p 'Carpeta: ' carpeta

if [ -d "$carpeta" ]; then
    cd "$carpeta"
else
    printf "${Rojo_Brillante}¡Carpeta no encontrada!${Blanco_Brillante}\n"
    echo
    exit 1
fi

echo
printf "${Verde_Brillante}Archivos ⤵\n"
echo
ls
printf "${Verde_Brillante}\n"
read -p 'Archivo: ' imagen

if [ -f "$imagen" ]; then
    echo
    printf "${Rojo_Brillante}                           Datos del archivo\n"
    printf "${Amarillo_Brillante}╭──────────────────────────────────┬──────────────────────────────────╮\n"
    exiftool "${imagen}" | while IFS= read -r line; do
        campo=$(echo "$line" | cut -d':' -f1 | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
        valor=$(echo "$line" | cut -d':' -f2- | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
        printf "${Amarillo_Brillante}│ ${Blanco_Brillante}%-30s ${Amarillo_Brillante}│ ${Blanco}%-30s ${Amarillo_Brillante}│\n" "$campo" "$valor"
    done
    printf "${Amarillo_Brillante}╰──────────────────────────────────┴──────────────────────────────────╯\n"
else
    printf "${Rojo_Brillante}¡Archivo no encontrado!${Blanco_Brillante}\n"
    echo
    exit 1
fi