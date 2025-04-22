#!/usr/bin/env bash

move() {
cd
cd Stellar/config/system
mv user.txt $HOME
cd
cd Stellar/config/themes
mv banner.txt $HOME
mv banner_color.txt $HOME
mv banner_background.txt $HOME
mv banner_background_color.txt $HOME
git stash
cd
cd Stellar
}

copy() {
cd
mv user.txt ~/Stellar/config/system
mv banner.txt ~/Stellar/config/themes/
mv banner_color.txt ~/Stellar/config/themes/
mv banner_background.txt ~/Stellar/config/themes/
mv banner_background_color.txt ~/Stellar/config/themes/
}

move
copy

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

copy

printf "¡Todo en orden!" | lolcat -a -d 20
echo