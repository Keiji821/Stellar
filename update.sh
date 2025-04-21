#!/usr/bin/env bash

cd config/themes
BANNER=(cat "banner.txt")
BANNER_COLOR=(cat "banner_color.txt")
BANNER_BACKGROUND=(cat "banner_background.txt")
BANNER_BACKGROUND_COLOR=(cat "banner_background_color.txt")
cd
cd Stellar

update_repo() {
    if ! git pull --force; then
        echo "Error al actualizar el repositorio" >&2
        exit 1
    fi
}

show_lolcat_message() {
    local message="$1"
    local delay="${2:-20}"
    echo "$message" | lolcat -a -d "$delay"
}

show_lolcat_message "Iniciando actualización..."
if update_repo; then
    show_lolcat_message "¡Repositorio actualizado con éxito!"
else
    show_lolcat_message "Falló la actualización" 5
    exit 1
fi

cd config/themes
echo $BANNER > banner.txt
echo $BANNER_COLOR > banner_color.txt
echo $BANNER_BACKGROUND > banner_background.txt
echo $BANNER_BACKGROUND_COLOR > banner_background_color.txt
printf "¡Todo en orden!" | lolcat -a -d 20
echo