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
}

show_progress() {
    local percentage=$1
    local message=$2

    if [ $percentage -lt 25 ]; then
        bar_color="${rojo}"
    elif [ $percentage -lt 75 ]; then
        bar_color="${amarillo}"
    else
        bar_color="${verde}"
    fi

    dialog --gauge "$message" 10 60 $percentage
}

install_packages() {
    dialog --infobox "Actualizando paquetes..." 6 40
    apt update -y > /dev/null 2>&1 && apt upgrade -y > /dev/null 2>&1

    local apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    local total=${#apt_packages[@]}
    local step=$((70 / total))

    for ((i=0; i<total; i++)); do
        show_progress $((20 + (step * (i + 1)) / 2)) "Instalando ${apt_packages[$i]}..."
        apt install -y "${apt_packages[$i]}" > /dev/null 2>&1
    done

    local pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    total=${#pip_packages[@]}
    step=$((50 / total))

    for ((i=0; i<total; i++)); do
        show_progress $((70 + (step * (i + 1)) / 2)) "Instalando ${pip_packages[$i]}..."
        pip install "${pip_packages[$i]}" > /dev/null 2>&1
    done

    show_progress 100 "Instalación completada con éxito."
    sleep 2
}

main() {
    user_config
    install_packages
}

if [[ ! -d ~/Stellar/config/system ]]; then
    dialog --title "Error" --msgbox "Directorio system no encontrado en ~/." 6 40
    exit 1
fi

main
