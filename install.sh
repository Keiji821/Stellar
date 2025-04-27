#!/bin/bash
LOG="$HOME/stellar_install.log"
trap 'cleanup' EXIT

cleanup(){
    [[ -n "$TAIL_PID" ]] && kill "$TAIL_PID" 2>/dev/null
    rm -f "$LOG"
}

# Colores
gris="\033[1;30m"; blanco="\033[0m"
rojo="\033[1;31m"; verde="\033[1;32m"
amarillo="\033[1;33m"; azul="\033[1;34m"
azul_agua="\033[1;36m"; morado="\033[1;35m"
cyan="\033[38;2;23;147;209m"

user_config(){
    while true; do
        username=$(dialog --title "Configuración de Usuario" \
            --inputbox "Ingrese un usuario (4-15 caracteres, letras/números/_):" 10 60 3>&1 2>&1)
        [[ $? -ne 0 ]] && { clear; echo -e "${rojo}Instalación cancelada.${blanco}"; exit 1; }
        [[ ${#username} -ge 4 && ${#username} -le 15 && "$username" =~ ^[a-zA-Z0-9_]+$ ]] && break
    done
    mkdir -p ~/Stellar/config/system
    echo "$username" > ~/Stellar/config/system/user.txt
}

install_tasks(){
    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    total=$(( ${#apt_packages[@]} + ${#pip_packages[@]} + 2 ))
    current=0

    echo -e "${azul}== Instalador de Stellar ==${blanco}" >>"$LOG"
    echo "" >>"$LOG"

    echo -e "${cyan}➔ Preparando la instalación...${blanco}" >>"$LOG"
    sleep 1

    ((current++))
    echo -e "${azul_agua}➔ Actualizando APT... (${current}/${total})${blanco}" >>"$LOG"
    if apt update -y >>"$LOG" 2>&1; then
        echo -e "${verde}✔ APT actualizado. (${current}/${total})${blanco}" >>"$LOG"
    else
        echo -e "${rojo}✘ Error APT. (${current}/${total})${blanco}" >>"$LOG"
    fi
    sleep 0.3

    ((current++))
    echo -e "${azul_agua}➔ Upgrade sistema... (${current}/${total})${blanco}" >>"$LOG"
    if apt upgrade -y >>"$LOG" 2>&1; then
        echo -e "${verde}✔ Sistema upgraded. (${current}/${total})${blanco}" >>"$LOG"
    else
        echo -e "${rojo}✘ Error upgrade. (${current}/${total})${blanco}" >>"$LOG"
    fi
    sleep 0.3

    echo "" >>"$LOG"
    echo -e "${morado}== Paquetes APT ==${blanco}" >>"$LOG"
    for pkg in "${apt_packages[@]}"; do
        ((current++))
        echo -e "${amarillo}➔ Instalando $pkg... (${current}/${total})${blanco}" >>"$LOG"
        if apt install -y "$pkg" >>"$LOG" 2>&1; then
            echo -e "${verde}✔ $pkg instalado. (${current}/${total})${blanco}" >>"$LOG"
        else
            echo -e "${rojo}✘ Error $pkg. (${current}/${total})${blanco}" >>"$LOG"
        fi
        sleep 0.2
    done

    echo "" >>"$LOG"
    echo -e "${morado}== Paquetes PIP ==${blanco}" >>"$LOG"
    for pkg in "${pip_packages[@]}"; do
        ((current++))
        echo -e "${amarillo}➔ Instalando $pkg... (${current}/${total})${blanco}" >>"$LOG"
        if pip install "$pkg" >>"$LOG" 2>&1; then
            echo -e "${verde}✔ $pkg instalado. (${current}/${total})${blanco}" >>"$LOG"
        else
            echo -e "${rojo}✘ Error $pkg. (${current}/${total})${blanco}" >>"$LOG"
        fi
        sleep 0.2
    done

    echo "" >>"$LOG"
    echo -e "${verde}✔ ¡Instalación completada! (${current}/${total})${blanco}" >>"$LOG"
}

main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    >"$LOG"
    user_config
    dialog --title "Instalador de Stellar" --colors --tailboxbg "$LOG" 20 70 &
    TAIL_PID=$!
    install_tasks
    sleep 1
    kill "$TAIL_PID" 2>/dev/null
    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main