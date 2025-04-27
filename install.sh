#!/bin/bash

rojo='\033[0;31m'
verde='\033[0;32m'
amarillo='\033[0;33m'
azul='\033[0;34m'
magenta='\033[0;35m'
cyan='\033[0;36m'
blanco='\033[0m'
reset='\033[0m'

PROGRESS_BAR_WIDTH=50

user_config() {
    local valid_username=''
    while [[ -z "$valid_username" ]]; do
        username=$(dialog --title "Configuración de Usuario" --inputbox "Ingrese un nombre de usuario (4-15 caracteres, letras/números/_):" 10 60 3>&1 1>&2 2>&3)
        dialog_return=$?

        if [[ $dialog_return -ne 0 ]]; then
            clear
            echo "Instalación cancelada."
            exit 1
        fi

        if [[ -z "$username" ]]; then
            dialog --msgbox "Error: El campo no puede estar vacío." 6 40
            continue
        fi

        if [[ ${#username} -lt 4 || ${#username} -gt 15 ]]; then
            dialog --msgbox "Error: El nombre de usuario debe tener entre 4 y 15 caracteres." 6 40
            continue
        fi

        if ! [[ "$username" =~ ^[a-zA-Z0-9_]+$ ]]; then
            dialog --msgbox "Error: Solo se permiten letras, números y guiones bajos (_)." 6 40
            continue
        fi

        valid_username=$username
    done

    echo "$valid_username" > ~/Stellar/config/system/user.txt

    dialog --msgbox "Nombre de usuario configurado correctamente: $valid_username" 6 40
}

progress() {
    local percentage=$1
    local filled=$((${PROGRESS_BAR_WIDTH} * ${percentage} / 100))
    local empty=$((${PROGRESS_BAR_WIDTH} - ${filled}))

    if [ $percentage -lt 25 ]; then
        bar_color="${rojo}"
    elif [ $percentage -lt 75 ]; then
        bar_color="${amarillo}"
    else
        bar_color="${verde}"
    fi

    printf "\r[${bar_color}$(printf '#%.0s' $(seq 1 $filled))${reset}$(printf '.%.0s' $(seq 1 $empty))]"
    printf " ${bar_color}%3d%%${reset}" "${percentage}"
    printf "\n"
}

show_package() {
    printf "\r${azul}[${verde}+${azul}]${blanco} %s\n" "$1"
}

install_packages() {
    progress 0

    show_package "Actualizando paquetes..."
    apt update -y > /dev/null 2>&1 && apt upgrade -y > /dev/null 2>&1
    progress 30

    local apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    local total=${#apt_packages[@]}
    local step=$((40 / total))

    for ((i=0; i<total; i++)); do
        show_package "Instalando ${apt_packages[$i]}"
        apt install -y "${apt_packages[$i]}" > /dev/null 2>&1
        progress=$((30 + (step * (i + 1))))
        progress $progress
    done

    local pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    total=${#pip_packages[@]}
    step=$((30 / total))

    for ((i=0; i<total; i++)); do
        show_package "Instalando ${pip_packages[$i]}"
        pip install "${pip_packages[$i]}" > /dev/null 2>&1
        progress=$((70 + (step * (i + 1))))
        progress $progress
    done
}

main() {
    clear
    install_packages
    progress 100
    echo -e "\n${verde}[+] Instalación completada con éxito.\n"
}

if [[ ! -d ~/Stellar/config/system ]]; then
    dialog --title "Error" --msgbox "Directorio system no encontrado en ~/." 6 40
    exit 1
fi

user_config
main
