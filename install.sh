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
        username=$(dialog --title "Configuración de Usuario" \
                          --inputbox "Ingrese nombre de usuario (4-15 caracteres, solo alfanuméricos y _):" \
                          10 60 3>&1 1>&2 2>&3)

        local exit_code=$?

        if [[ $exit_code -ne 0 ]]; then
            dialog --title "Confirmación" --yesno "¿Cancelar instalación?" 6 50 && {
                clear
                echo "Instalación cancelada."
                exit 1
            }
            continue
        fi

        if [[ -z "$username" ]]; then
            dialog --msgbox "El nombre de usuario no puede estar vacío." 6 50
            continue
        fi

        if [[ ${#username} -lt 4 || ${#username} -gt 15 ]]; then
            dialog --msgbox "Longitud inválida (debe ser 4-15 caracteres)." 6 50
            continue
        fi

        if [[ "$username" =~ ^[a-zA-Z0-9_]+$ ]]; then
            mkdir -p "$CONFIG_DIR"
            echo "$username" > "$USER_FILE"
            break
        else
            dialog --msgbox "Caracteres inválidos. Solo se permiten letras, números y _." 6 60
        fi
    done
}

iniciar_instalacion() {
    [[ -e "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"
    mkfifo "$PROGRESO_CANAL"

    dialog --title "Instalador Stellar" --programbox 20 70 < "$PROGRESO_CANAL" &
    exec 3>"$PROGRESO_CANAL"

    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)

    echo "➔ Preparando instalación..." >&3
    sleep 1

    echo "➔ Actualizando paquetes..." >&3
    if apt update -y >/dev/null 2>&1; then
        echo "✔ Paquetes actualizados." >&3
    else
        echo "✘ Error actualizando paquetes." >&3
    fi
    sleep 0.5

    echo "➔ Actualizando sistema..." >&3
    if apt upgrade -y >/dev/null 2>&1; then
        echo "✔ Sistema actualizado." >&3
    else
        echo "✘ Error actualizando sistema." >&3
    fi
    sleep 0.5

    for pkg in "${apt_packages[@]}"; do
        echo "➔ Instalando $pkg..." >&3
        if apt install -y "$pkg" >/dev/null 2>&1; then
            echo "✔ $pkg instalado." >&3
        else
            echo "✘ Error instalando $pkg." >&3
        fi
        sleep 0.3
    done

    for pkg in "${pip_packages[@]}"; do
        echo "➔ Instalando $pkg..." >&3
        if pip install "$pkg" >/dev/null 2>&1; then
            echo "✔ $pkg instalado." >&3
        else
            echo "✘ Error instalando $pkg." >&3
        fi
        sleep 0.3
    done

    echo "✔ Instalación completada!" >&3
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

    dialog --title "Completado" --msgbox "¡Instalación finalizada correctamente!" 8 50
    clear
}

main
