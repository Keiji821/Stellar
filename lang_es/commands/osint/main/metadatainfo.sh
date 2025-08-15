#!/bin/bash

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