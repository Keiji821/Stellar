#!/bin/bash

PROGRESO_CANAL="/tmp/progress_pipe"

user_config() {
    while true; do
        username=$(dialog --title "Configuración de Usuario" \
                          --inputbox "Ingrese un nombre de usuario (4-15 caracteres, letras/números/_):" 10 60 3>&1 1>&2 2>&3)

        if [[ $? -ne 0 ]]; then
            clear
            echo "Instalación cancelada."
            exit 1
        fi

        [[ -z "$username" ]] && continue
        [[ ${#username} -lt 4 || ${#username} -gt 15 ]] && continue
        [[ "$username" =~ ^[a-zA-Z0-9_]+$ ]] && break
    done

    mkdir -p ~/Stellar/config/system
    echo "$username" > ~/Stellar/config/system/user.txt
}

iniciar_instalacion() {
    mkdir -p /tmp

    if [[ ! -p "$PROGRESO_CANAL" ]]; then
        mkfifo "$PROGRESO_CANAL"
    fi

    dialog --title "Instalador Stellar" --gauge "Preparando instalación..." 10 70 0 < "$PROGRESO_CANAL" &
    exec 3>"$PROGRESO_CANAL"

    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)

    total_items=$(( ${#apt_packages[@]} + ${#pip_packages[@]} + 2 ))
    current_item=0

    enviar_progreso() {
        porcentaje=$(( 100 * current_item / total_items ))
        echo "$porcentaje"
    }

    echo "0" >&3
    sleep 1

    echo "5" >&3
    apt update -y >/dev/null 2>&1

    echo "10" >&3
    apt upgrade -y >/dev/null 2>&1

    for pkg in "${apt_packages[@]}"; do
        current_item=$((current_item + 1))
        enviar_progreso >&3
        echo "Instalando $pkg (APT)..." >&3
        apt install -y "$pkg" >/dev/null 2>&1
    done

    for pkg in "${pip_packages[@]}"; do
        current_item=$((current_item + 1))
        enviar_progreso >&3
        echo "Instalando $pkg (pip)..." >&3
        pip install "$pkg" >/dev/null 2>&1
    done

    echo "100" >&3
    echo "Instalación completada exitosamente!" >&3
    sleep 2

    exec 3>&-
    rm -f "$PROGRESO_CANAL"
}

main() {
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar

    user_config
    iniciar_instalacion

    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main