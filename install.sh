#!/bin/bash

PROGRESO_CANAL="$HOME/.stellar_install_pipe"
CONFIG_DIR="$HOME/Stellar/config/system"
USER_FILE="$CONFIG_DIR/user.txt"
LOG_FILE="$HOME/stellar_install.log"

cleanup() {
    exec 3>&-
    [[ -e "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"
}
trap cleanup EXIT ERR

install_dependencies() {
    echo "➔ Verificando dependencias..." >&3
    if ! command -v dialog &> /dev/null; then
        if ! pkg install dialog -y >> "$LOG_FILE" 2>&1; then
            echo "✘ Error: No se pudo instalar dialog. Ver $LOG_FILE" >&3
            exit 1
        fi
    fi
}

user_config() {
    while true; do
        username=$(dialog --title "Configuración de Usuario" \
                        --inputbox "Ingrese nombre de usuario (4-15 caracteres, solo alfanuméricos y _):" \
                        10 60 3>&1 1>&2 2>&3)
        local exit_code=$?

        case $exit_code in
            0)
                if [[ -z "$username" ]]; then
                    dialog --msgbox "El nombre de usuario no puede estar vacío." 6 50
                    continue
                elif [[ ${#username} -lt 4 || ${#username} -gt 15 ]]; then
                    dialog --msgbox "Longitud inválida (debe ser 4-15 caracteres)." 6 50
                    continue
                elif [[ ! "$username" =~ ^[a-zA-Z0-9_]+$ ]]; then
                    dialog --msgbox "Caracteres inválidos. Solo letras, números y _." 6 60
                    continue
                else
                    mkdir -p "$CONFIG_DIR"
                    echo "$username" > "$USER_FILE"
                    break
                fi
                ;;
            1)
                dialog --title "Confirmación" --yesno "¿Cancelar instalación?" 6 50 && {
                    echo "Instalación cancelada por el usuario." >> "$LOG_FILE"
                    exit 1
                }
                ;;
            *)
                echo "Error inesperado en dialog. Código: $exit_code" >> "$LOG_FILE"
                exit 1
                ;;
        esac
    done
}

iniciar_instalacion() {
    [[ -e "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"
    if ! mkfifo "$PROGRESO_CANAL"; then
        echo "Error: No se pudo crear la tubería FIFO." >&2
        exit 1
    fi

    dialog --title "Instalación de Stellar" --programbox 20 70 < "$PROGRESO_CANAL" &
    if [[ $? -ne 0 ]]; then
        echo "Error: No se pudo iniciar dialog." >&2
        rm -f "$PROGRESO_CANAL"
        exit 1
    fi
    exec 3>"$PROGRESO_CANAL"

    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)

    echo "➔ Preparando instalación..." >&3
    sleep 1

    echo "➔ Actualizando paquetes..." >&3
    if ! apt update -y >> "$LOG_FILE" 2>&1; then
        echo "✘ Error actualizando paquetes. Ver $LOG_FILE" >&3
        exit 1
    fi
    echo "✔ Paquetes actualizados." >&3
    sleep 0.5

    echo "➔ Actualizando sistema..." >&3
    if ! apt upgrade -y >> "$LOG_FILE" 2>&1; then
        echo "✘ Error actualizando sistema. Ver $LOG_FILE" >&3
        exit 1
    fi
    echo "✔ Sistema actualizado." >&3
    sleep 0.5

    for pkg in "${apt_packages[@]}"; do
        echo "➔ Instalando $pkg..." >&3
        if ! apt install -y "$pkg" >> "$LOG_FILE" 2>&1; then
            echo "✘ Error instalando $pkg. Ver $LOG_FILE" >&3
            exit 1
        fi
        echo "✔ $pkg instalado." >&3
        sleep 0.3
    done

    for pkg in "${pip_packages[@]}"; do
        echo "➔ Instalando $pkg..." >&3
        if ! pip install "$pkg" >> "$LOG_FILE" 2>&1; then
            echo "✘ Error instalando $pkg. Ver $LOG_FILE" >&3
            exit 1
        fi
        echo "✔ $pkg instalado." >&3
        sleep 0.3
    done

    echo "✔ Instalación completada!" >&3
    sleep 2
}

main() {
    install_dependencies
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    user_config
    iniciar_instalacion

    dialog --title "Completado" --msgbox "¡Instalación finalizada correctamente!" 8 50
    clear
}

main
reset
bash