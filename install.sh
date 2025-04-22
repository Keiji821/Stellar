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
progress() {
    local percentage=$1
    local filled=$(($PROGRESS_BAR_WIDTH * $percentage / 100))
    local empty=$(($PROGRESS_BAR_WIDTH - $filled))
    printf "${amarillo}[${cyan}"
    printf "%${filled}s" | tr ' ' '█'
    printf "${gris}%${empty}s" | tr ' ' ' '
    printf "${amarillo}] ${verde}%3d%%${blanco}\r" "$percentage"
}

spinner() {
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf "${amarillo} [%c]  ${blanco}" "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

clear

status_msg() {
    echo -e "${amarillo}[${verde}+${amarillo}]${blanco} $1"
}

handle_error() {
    echo -e "${rojo}[ERROR]${blanco} $1"
    exit 1
}

copy_config() {
    status_msg "Copiando archivos de configuración..."
    if [[ -f ~/Stellar/config/.bash_profile && -f ~/Stellar/config/.bashrc ]]; then
        cp ~/Stellar/config/.bash_profile ~/ & spinner
        cp ~/Stellar/config/.bashrc ~/ & spinner
    else
        handle_error "Archivos de configuración no encontrados en ~/Stellar/config/"
    fi
    progress 10
}

copy_config

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

        echo "$usuario" > ~/system/user.txt && break
        echo -e "${verde}Usuario configurado correctamente!${blanco}"
        sleep 2
    done
    progress 20
}

if [[ ! -d ~/system ]]; then
    handle_error "Directorio system no encontrado en ~/"
fi

user_config

install_packages() {
    status_msg "Actualizando paquetes..."
    apt update -y && apt upgrade -y & spinner
    progress 30
    
    status_msg "Instalando dependencias principales..."
    local apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils)
    for pkg in "${apt_packages[@]}"; do
        apt install -y $pkg & spinner
        progress=$((30 + (40 * (++i)/${#apt_packages[@]}))
        progress $progress
    done
    
    status_msg "Instalando dependencias de Python..."
    local pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks 
                      requests rich "rich[jupyter]" lolcat discord)
    i=0
    for pkg in "${pip_packages[@]}"; do
        pip install $pkg & spinner
        progress=$((70 + (30 * (++i)/${#pip_packages[@]})))
        progress $progress
    done
}

install_packages

echo
status_msg "Instalación completada con éxito!"