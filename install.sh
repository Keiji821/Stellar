#!/bin/bash
LOG="$HOME/stellar_install.log"
trap 'rm -f "$LOG"' EXIT

user_config(){
    while true; do
        username=$(dialog --title "Configuración de Usuario" \
                          --inputbox "Ingrese un nombre de usuario (4–15 caracteres, letras/números/_):" 10 60 3>&1 2>&1)
        [[ $? -ne 0 ]] && { clear; echo "Instalación cancelada."; exit 1; }
        [[ ${#username} -ge 4 && ${#username} -le 15 && "$username" =~ ^[a-zA-Z0-9_]+$ ]] && break
    done
    mkdir -p ~/Stellar/config/system
    echo "$username" > ~/Stellar/config/system/user.txt
}

append_and_show(){
    echo -e "$1" >> "$LOG"
    dialog --title "Instalador de Stellar" --infobox "$(cat "$LOG")" 20 70
    sleep 0.5
}

main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    > "$LOG"
    user_config

    append_and_show "== Instalador de Stellar ==\n"
    append_and_show "[*] Preparando instalación...\n"

    append_and_show "[*] Actualizando lista de paquetes..."
    apt update -y >/dev/null 2>&1
    append_and_show "[✔] Lista de paquetes actualizada.\n"

    append_and_show "[*] Actualizando sistema..."
    apt upgrade -y >/dev/null 2>&1
    append_and_show "[✔] Sistema actualizado.\n"

    append_and_show "== Instalación de paquetes APT ==\n"
    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    for pkg in "${apt_packages[@]}"; do
        append_and_show "[*] Instalando $pkg (APT)..."
        if apt install -y "$pkg" >/dev/null 2>&1; then
            append_and_show "[✔] $pkg instalado.\n"
        else
            append_and_show "[✖] Error con $pkg.\n"
        fi
    done

    append_and_show "== Instalación de paquetes PIP ==\n"
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    for pkg in "${pip_packages[@]}"; do
        append_and_show "[*] Instalando $pkg (pip)..."
        if pip install "$pkg" >/dev/null 2>&1; then
            append_and_show "[✔] $pkg instalado.\n"
        else
            append_and_show "[✖] Error con $pkg.\n"
        fi
    done

    append_and_show "[✔] Instalación completada exitosamente!\n"
    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main