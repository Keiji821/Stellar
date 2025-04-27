#!/bin/bash

PROGRESO_CANAL="$HOME/.stellar_install_pipe"
CONFIG_DIR="$HOME/Stellar/config/system"
USER_FILE="$CONFIG_DIR/user.txt"

check_environment() {
    if ! [[ $(uname -o) == *Android* ]]; then
        echo "Este script solo funciona en Termux (Android)."
        exit 1
    fi
}

install_dependencies() {
    if ! command -v dialog &> /dev/null; then
        pkg install dialog -y >/dev/null 2>&1 || {
            echo "Error: No se pudo instalar dialog"
            exit 1
        }
    fi
}

user_config() {
    while true; do
        username=$(dialog --title "Configuración de Usuario" --colors \
                          --inputbox "\Z1Ingrese nombre de usuario (4-15 caracteres, solo alfanuméricos y _):\Z0" \
                          10 60 3>&1 1>&2 2>&3)

        local exit_code=$?

        if [[ $exit_code -ne 0 ]]; then
            dialog --title "Confirmación" --yesno "\Z1¿Cancelar instalación?\Z0" 6 50 && {
                clear
                echo "Instalación cancelada."
                exit 1
            }
            continue
        fi

        if [[ -z "$username" ]]; then
            dialog --msgbox "\Z1El nombre de usuario no puede estar vacío.\Z0" 6 50
            continue
        fi

        if [[ ${#username} -lt 4 || ${#username} -gt 15 ]]; then
            dialog --msgbox "\Z1Longitud inválida (debe ser 4-15 caracteres).\Z0" 6 50
            continue
        fi

        if [[ "$username" =~ ^[a-zA-Z0-9_]+$ ]]; then
            mkdir -p "$CONFIG_DIR"
            echo "$username" > "$USER_FILE"
            break
        else
            dialog --msgbox "\Z1Caracteres inválidos. Solo se permiten letras, números y _.\Z0" 6 60
        fi
    done
}

iniciar_instalacion() {
    [[ -e "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"
    mkfifo "$PROGRESO_CANAL"

    dialog --title "Instalador Stellar" --colors --programbox 20 70 < "$PROGRESO_CANAL" &
    exec 3>"$PROGRESO_CANAL"

    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)

    echo "\Z2➔ Preparando instalación...\Z0" >&3
    sleep 1

    echo "\Z3➔ Actualizando paquetes...\Z0" >&3
    if apt update -y >/dev/null 2>&1; then
        echo "\Z2✔ Paquetes actualizados.\Z0" >&3
    else
        echo "\Z1✘ Error actualizando paquetes.\Z0" >&3
    fi
    sleep 0.5

    echo "\Z3➔ Actualizando sistema...\Z0" >&3
    if apt upgrade -y >/dev/null 2>&1; then
        echo "\Z2✔ Sistema actualizado.\Z0" >&3
    else
        echo "\Z1✘ Error actualizando sistema.\Z0" >&3
    fi
    sleep 0.5

    for pkg in "${apt_packages[@]}"; do
        echo "\Z3➔ Instalando $pkg...\Z0" >&3
        if apt install -y "$pkg" >/dev/null 2>&1; then
            echo "\Z2✔ $pkg instalado.\Z0" >&3
        else
            echo "\Z1✘ Error instalando $pkg.\Z0" >&3
        fi
        sleep 0.3
    done

    for pkg in "${pip_packages[@]}"; do
        echo "\Z3➔ Instalando $pkg...\Z0" >&3
        if pip install "$pkg" >/dev/null 2>&1; then
            echo "\Z2✔ $pkg instalado.\Z0" >&3
        else
            echo "\Z1✘ Error instalando $pkg.\Z0" >&3
        fi
        sleep 0.3
    done

    echo "\Z2✔ Instalación completada!\Z0" >&3
    sleep 2

    exec 3>&-
    rm -f "$PROGRESO_CANAL"
}

main() {
    check_environment
    install_dependencies
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    user_config
    iniciar_instalacion

    dialog --title "Completado" --colors --msgbox "\Z2¡Instalación finalizada correctamente!\Z0" 8 50
    clear
}

main
