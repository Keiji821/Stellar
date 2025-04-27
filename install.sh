#!/bin/bash

gris="\033[1;30m"
blanco="\033[0m"
rojo="\033[1;31m"
verde="\033[1;32m"
amarillo="\033[1;33m"
azul="\033[1;34m"
magenta="\033[1;35m"
cyan="\033[1;36m"
reset="\033[0m"

cp ~/Stellar/config/.bash_profile ~/.
cp ~/Stellar/config/.bashrc ~/.

PROGRESS_BAR_WIDTH=50
current_line=2

user_config() {
    while true; do
        dialog --title "Configuración de usuario" --backtitle "Stellar OS Installer" --inputbox "Por favor, ingresa un nombre de usuario (4-15 caracteres):" 10 50 2>/tmp/username.txt

        usuario=$(cat /tmp/username.txt)

        if [[ -z "$usuario" ]]; then
            dialog --title "Error" --msgbox "El campo no puede estar vacío" 6 30
            continue
        fi

        if [[ "${#usuario}" -lt 4 || "${#usuario}" -gt 15 ]]; then
            dialog --title "Error" --msgbox "Debe tener entre 4 y 15 caracteres" 6 30
            continue
        fi

        if [[ ! "$usuario" =~ ^[a-zA-Z0-9_]+$ ]]; then
            dialog --title "Error" --msgbox "Solo se permiten letras, números y _" 6 30
            continue
        fi

        echo "$usuario" > config/system/user.txt
        dialog --title "Éxito" --msgbox "Usuario configurado correctamente!" 6 30
        break
    done
}

progress() {
    dialog --title "Instalación en progreso" --backtitle "Stellar OS Installer" --gauge "Instalando... Por favor espere." 10 70 $1
}

show_package() {
    dialog --title "Instalando paquetes" --msgbox "$1" 6 50
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
        progress $((30 + (step * (i + 1))))
    done

    local pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    total=${#pip_packages[@]}
    step=$((30 / total))

    for ((i=0; i<total; i++)); do
        show_package "Instalando ${pip_packages[$i]}"
        pip install "${pip_packages[$i]}" > /dev/null 2>&1
        progress $((70 + (step * (i + 1))))
    done
}

main() {
    clear
    current_line=2
    install_packages
    progress 100
    dialog --title "Instalación completa" --msgbox "¡Instalación completada exitosamente!" 6 50
}

if [[ ! -d config/system ]]; then
    dialog --title "Error" --msgbox "Directorio system no encontrado en ~/" 6 50
    exit 1
fi

user_config
main