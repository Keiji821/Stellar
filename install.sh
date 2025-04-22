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

PROGRESS_BAR_WIDTH=50
current_line=2

user_config() {
    while true; do
        clear
        echo -e "${amarillo}Configuración de usuario${blanco}"
        echo -e "${amarillo}-----------------------${blanco}"

        read -p "Nombre de usuario (4-15 caracteres): " usuario

        if [[ -z "$usuario" ]]; then
            echo -e "${rojo}El campo no puede estar vacío${blanco}"
            sleep 1
            continue
        fi

        if [[ "${#usuario}" -lt 4 || "${#usuario}" -gt 15 ]]; then
            echo -e "${rojo}Debe tener entre 4 y 15 caracteres${blanco}"
            sleep 1
            continue
        fi

        if [[ ! "$usuario" =~ ^[a-zA-Z0-9_]+$ ]]; then
            echo -e "${rojo}Solo se permiten letras, números y _${blanco}"
            sleep 1
            continue
        fi

        echo "$usuario" > config/system/user.txt && break
        echo -e "${verde}Usuario configurado correctamente!${blanco}"
        sleep 2
    done
    progress 20
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
    
    printf "\r${amarillo}┌${blanco}[${bar_color}"
    printf "%${filled}s" | tr ' ' '█'
    printf "%${empty}s" | tr ' ' '░'
    printf "${blanco}]${amarillo}┐"
    printf "\n${amarillo}└${blanco} Progreso: ${bar_color}%3d%% ${amarillo}┘${reset}" "${percentage}"
}

show_package() {
    printf "\033[${current_line}H\033[2K${amarillo}[${verde}+${amarillo}]${blanco} %s" "$1"
    printf "\033[$((${current_line} + 2))H"
}

install_packages() {
    progress 0
    echo -e "\n\n"

    show_package "Actualizando paquetes..."
    apt update -y > /dev/null 2>&1 && apt upgrade -y > /dev/null 2>&1
    progress 30

    local apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils)
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
    echo -e "\n\n"
    current_line=2
    install_packages
    progress 100
    echo -e "\n\n${amarillo}[${verde}+${amarillo}]${blanco} ¡Instalación completada!\n"
}

if [[ ! -d config/system ]]; then
    handle_error "Directorio system no encontrado en ~/"
fi

user_config
main