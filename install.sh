#!/bin/bash

PROGRESO_CANAL="$HOME/.stellar_install_pipe"
CONFIG_DIR="$HOME/Stellar/config/system"
USER_FILE="$CONFIG_DIR/user.txt"
LOG_FILE="$HOME/stellar_install.log"
export NCURSES_NO_UTF8_ACS=1

cleanup() {
    [[ -e "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"
}
trap cleanup EXIT ERR

show_error() {
    local msg="$1"
    echo "✘ Error: $msg" >&3
    echo "    Detalles en: $LOG_FILE" >&3
    sleep 3
}

install_dependencies() {
    if ! command -v dialog &> /dev/null; then
        echo "➔ Instalando dialog..." >&3
        if ! pkg install dialog -y >> "$LOG_FILE" 2>&1; then
            show_error "Instalación de dialog fallida"
            return 1
        fi
    fi
    return 0
}

user_config() {
    while true; do
        username=$(dialog --title "CONFIGURACIÓN DE USUARIO" \
                         --inputbox "\nNombre de usuario (4-15 caracteres):\nSolo letras, números y _" \
                         10 60 3>&1 1>&2 2>&3)
        local exit_code=$?

        case $exit_code in
            0)
                if [[ -z "$username" ]]; then
                    dialog --msgbox "El nombre no puede estar vacío." 6 50
                    continue
                elif [[ ${#username} -lt 4 || ${#username} -gt 15 ]]; then
                    dialog --msgbox "Longitud inválida (4-15 caracteres)." 7 50
                    continue
                elif [[ ! "$username" =~ ^[a-zA-Z0-9_]+$ ]]; then
                    dialog --msgbox "Caracteres inválidos. Solo letras, números y _." 7 60
                    continue
                else
                    mkdir -p "$CONFIG_DIR"
                    echo "$username" > "$USER_FILE"
                    return 0
                fi
                ;;
            1)
                dialog --title "CONFIRMACIÓN" --yesno "¿Cancelar instalación?" 7 50
                if [[ $? -eq 0 ]]; then
                    echo "Instalación cancelada por usuario" >> "$LOG_FILE"
                    exit 1
                fi
                ;;
            *)
                show_error "Error inesperado"
                exit 1
                ;;
        esac
    done
}

iniciar_instalacion() {
    [[ -e "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"
    if ! mkfifo "$PROGRESO_CANAL"; then
        show_error "No se creó el canal de progreso"
        exit 1
    fi

    dialog --title "INSTALACIÓN DE STELLAR" --programbox 20 70 < "$PROGRESO_CANAL" &
    exec 3>"$PROGRESO_CANAL"

    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    npm_packages=(chalk)

    echo "➔ Preparando instalación..." >&3
    sleep 1

    echo "➔ Actualizando repositorios..." >&3
    if ! apt update -y >> "$LOG_FILE" 2>&1; then
        show_error "Error actualizando repositorios"
        echo "➔ Solución alternativa..." >&3
        if ! apt update -y --fix-missing >> "$LOG_FILE" 2>&1; then
            show_error "Error persistente en repositorios"
            exit 1
        fi
    fi
    echo "✔ Repositorios actualizados" >&3
    sleep 0.5

    echo "➔ Actualizando sistema..." >&3
    if ! apt upgrade -y >> "$LOG_FILE" 2>&1; then
        show_error "Error actualizando sistema"
        exit 1
    fi
    echo "✔ Sistema actualizado" >&3
    sleep 0.5

    for pkg in "${apt_packages[@]}"; do
        echo "➔ Instalando $pkg..." >&3
        
        if dpkg -s "$pkg" &> /dev/null; then
            echo "✔ $pkg ya instalado" >&3
            sleep 0.2
            continue
        fi
        
        if ! apt install -y "$pkg" >> "$LOG_FILE" 2>&1; then
            show_error "Instalando $pkg"
            echo "➔ Reintentando $pkg..." >&3
            if ! apt install -y --reinstall "$pkg" >> "$LOG_FILE" 2>&1; then
                show_error "Error persistente con $pkg"
                exit 1
            fi
        fi
        echo "✔ $pkg instalado" >&3
        sleep 0.3
    done

    for pkg in "${pip_packages[@]}"; do
        echo "➔ Instalando $pkg..." >&3
        
        if pip show "$pkg" &> /dev/null; then
            echo "✔ $pkg ya instalado" >&3
            sleep 0.2
            continue
        fi
        
        if ! pip install --no-cache-dir "$pkg" >> "$LOG_FILE" 2>&1; then
            show_error "Instalando $pkg"
            echo "➔ Instalación local..." >&3
            if ! pip install --user --no-cache-dir "$pkg" >> "$LOG_FILE" 2>&1; then
                show_error "Error persistente con $pkg"
                exit 1
            fi
        fi
        echo "✔ $pkg instalado" >&3
        sleep 0.3
    done

    for pkg in "${npm_packages[@]}"; do
        echo "➔ Instalando $pkg..." >&3
        
        if npm list -g "$pkg" &> /dev/null; then
            echo "✔ $pkg ya instalado" >&3
            sleep 0.2
            continue
        fi
        
        if ! npm install -g "$pkg" >> "$LOG_FILE" 2>&1; then
            show_error "Instalando $pkg"
            echo "➔ Permisos elevados..." >&3
            if ! npm install -g "$pkg" --unsafe-perm >> "$LOG_FILE" 2>&1; then
                show_error "Error persistente con $pkg"
                exit 1
            fi
        fi
        echo "✔ $pkg instalado" >&3
        sleep 0.3
    done

    echo "✔ Instalación completada!" >&3
    sleep 2
}

main() {
    echo "Inicio: $(date)" > "$LOG_FILE"
    mkdir -p ~/Stellar
    
    if ! install_dependencies; then
        exit 1
    fi
    
    user_config
    iniciar_instalacion

    dialog --title "COMPLETADO" --msgbox "\n¡Stellar instalado correctamente!\n\nPuede comenzar a usar el sistema." 10 50
    clear
    
    cp ~/Stellar/config/.bash_profile ~/.
    cp ~/Stellar/config/.bashrc ~/.
    reset
    bash
}

main