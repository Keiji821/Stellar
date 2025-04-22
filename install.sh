#!/bin/bash

gris="\033[1;30m"
blanco="\033[0m"
blanco2="\033[1;37m"
rojo="\033[1;31m"
rojo2="\033[31m"
azul="\033[1;34m"
azul2="\033[34m"
azul_agua="\e[1;36m"
azul_agua2="\e[36m"
verde="\033[1;32m"
verde2="\033[32m"
morado="\033[1;35m"
morado2="\033[35m"
amarillo="\033[1;33m"
amarillo2="\033;33m"
cyan="\033[38;2;23;147;209m"

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

if [[ ! -d config/system ]]; then
    handle_error "Directorio system no encontrado en ~/"
fi

user_config

progress() {
    local percentage=$1
    local filled=$((${PROGRESS_BAR_WIDTH} * ${percentage} / 100))
    local empty=$((${PROGRESS_BAR_WIDTH} - ${filled}))
    printf "\r${amarillo}[${cyan}"
    printf "%${filled}s" | tr ' ' '■'
    printf "%${empty}s" | tr ' ' '·'
    printf "${amarillo}] ${verde}%3d%%${blanco}" "${percentage}"
}

show_package() {
    printf "\033[${current_line}H\033[2K${amarillo}[${verde}+${amarillo}]${blanco} %s" "$1"
    printf "\033[$((${current_line} + 1))H"
}

install_packages() {
    progress 0
    echo -e "\n\n"
    
    show_package "Actualizando paquetes..."
    apt update -y && apt upgrade -y
    progress 30

    local apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils)
    local total=${#apt_packages[@]}
    local step=$((40 / total))
    
    for ((i=0; i<total; i++)); do
        show_package "Instalando ${apt_packages[$i]}"
        apt install -y "${apt_packages[$i]}" 
        progress=$((30 + (step * (i + 1))))
        progress $progress
    done

    local pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    total=${#pip_packages[@]}
    step=$((30 / total))
    
    for ((i=0; i<total; i++)); do
        show_package "Instalando ${pip_packages[$i]}"
        pip install "${pip_packages[$i]}" 
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
    echo -e "\n${amarillo}[${verde}+${amarillo}]${blanco} ¡Instalación completada!\n"
}

main