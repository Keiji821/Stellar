#!/bin/bash

CONFIG_DIR="$HOME/Stellar/config/system"
USER_FILE="$CONFIG_DIR/user.txt"
LOG_DIR="/tmp/stellar_install_logs"
mkdir -p "$LOG_DIR"

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
amarillo2="\033[33m"
cyan="\033[38;2;23;147;209m"

trap 'show_error "Instalación interrumpida por el usuario"; cleanup; exit 1' INT TERM

cleanup() {
    show_warning "Limpiando archivos temporales..."
    rm -rf "$LOG_DIR"/*.log
}

show_header() {
    clear
    echo -e "${azul_agua}"
    echo "███████╗████████╗███████╗██╗     ██╗      █████╗ ██████╗ "
    echo "██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗██╔══██╗"
    echo "███████╗   ██║   █████╗  ██║     ██║     ███████║██████╔╝"
    echo "╚════██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║██╔══██╗"
    echo "███████║   ██║   ███████╗███████╗███████╗██║  ██║██║  ██║"
    echo "╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝"
    echo -e "${blanco}"
    echo "========================================================"
}

show_message() {
    echo -e "${verde}✔ $1${blanco}"
}

show_warning() {
    echo -e "${amarillo}⚠ $1${blanco}"
}

show_error() {
    echo -e "${rojo}✘ Error: $1${blanco}"
    echo -e "${rojo2}Detalles en $LOG_DIR/error.log${blanco}"
}

show_progress() {
    echo -e "${cyan}➔ $1...${blanco}"
}

log_error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $1" >> "$LOG_DIR/error.log"
}

prompt_continue() {
    echo -e "${morado}$1${blanco}"
    read -rp "Presione Enter para continuar..."
}

prompt_yesno() {
    while true; do
        read -rp "$(echo -e "${morado}$1 [s/n]: ${blanco}")" yn
        case $yn in
            [Ss]*) return 0 ;;
            [Nn]*) return 1 ;;
            *) echo -e "${amarillo}Por favor responda s o n${blanco}" ;;
        esac
    done
}

check_internet() {
    show_progress "Verificando conexión a Internet"
    if ! ping -c 2 -W 2 google.com > /dev/null 2>&1; then
        if ! ping -c 2 -W 2 8.8.8.8 > /dev/null 2>&1; then
            show_error "No hay conexión a Internet"
            return 1
        fi
    fi
    return 0
}

validate_username() {
    local username=$1
    if [[ -z "$username" ]]; then
        show_error "El nombre de usuario no puede estar vacío"
        return 1
    elif [[ ${#username} -lt 4 || ${#username} -gt 15 ]]; then
        show_error "Longitud inválida (debe ser 4-15 caracteres)"
        return 1
    elif [[ ! "$username" =~ ^[a-zA-Z0-9_]+$ ]]; then
        show_error "Caracteres inválidos. Solo letras, números y _"
        return 1
    fi
    return 0
}

install_pkg() {
    local pkg=$1
    show_progress "Instalando $pkg"
    
    if dpkg -l | grep -q "^ii  $pkg "; then
        show_message "$pkg ya está instalado"
        return 0
    fi

    if sudo apt-get install -y "$pkg" >> "$LOG_DIR/apt_install.log" 2>&1; then
        show_message "$pkg instalado correctamente"
        return 0
    else
        log_error "Falló la instalación de $pkg"
        show_warning "Reintentando instalación de $pkg"
        
        if sudo apt-get install -y --fix-broken "$pkg" >> "$LOG_DIR/apt_install_retry.log" 2>&1; then
            show_message "$pkg instalado después de reintento"
            return 0
        else
            log_error "Falló el reintento de instalación de $pkg"
            show_error "No se pudo instalar $pkg"
            return 1
        fi
    fi
}

install_pip() {
    local pkg=$1
    show_progress "Instalando $pkg (pip)"
    
    if pip show "$pkg" > /dev/null 2>&1; then
        show_message "$pkg ya está instalado (pip)"
        return 0
    fi

    if pip install --upgrade --no-cache-dir "$pkg" >> "$LOG_DIR/pip_install.log" 2>&1; then
        show_message "$pkg instalado correctamente (pip)"
        return 0
    else
        log_error "Falló la instalación pip de $pkg"
        show_warning "Intentando instalación local de $pkg"
        
        if pip install --user --upgrade --no-cache-dir "$pkg" >> "$LOG_DIR/pip_install_user.log" 2>&1; then
            show_message "$pkg instalado localmente (pip)"
            return 0
        else
            log_error "Falló la instalación local pip de $pkg"
            show_error "No se pudo instalar $pkg via pip"
            return 1
        fi
    fi
}

install_npm() {
    local pkg=$1
    show_progress "Instalando $pkg (npm)"
    
    if npm list -g "$pkg" --depth=0 > /dev/null 2>&1; then
        show_message "$pkg ya está instalado (npm)"
        return 0
    fi

    if npm install -g "$pkg" >> "$LOG_DIR/npm_install.log" 2>&1; then
        show_message "$pkg instalado correctamente (npm)"
        return 0
    else
        log_error "Falló la instalación npm de $pkg"
        show_warning "Intentando con permisos elevados"
        
        if npm install -g "$pkg" --unsafe-perm >> "$LOG_DIR/npm_install_unsafe.log" 2>&1; then
            show_message "$pkg instalado con permisos elevados (npm)"
            return 0
        else
            log_error "Falló la instalación npm con unsafe-perm de $pkg"
            show_error "No se pudo instalar $pkg via npm"
            return 1
        fi
    fi
}

user_config() {
    while true; do
        show_header
        echo -e "${azul}CONFIGURACIÓN DE USUARIO${blanco}"
        echo -e "${gris}----------------------------------------${blanco}"
        echo -e "${blanco2}Ingrese un nombre de usuario para Stellar"
        echo -e "Requisitos:"
        echo -e " - 4-15 caracteres"
        echo -e " - Solo letras, números y guiones bajos (_)"
        echo -e "${gris}----------------------------------------${blanco}"
        read -rp "Nombre de usuario: " username

        if validate_username "$username"; then
            mkdir -p "$CONFIG_DIR"
            echo "$username" > "$USER_FILE"
            show_message "Usuario configurado correctamente: $username"
            sleep 1
            return 0
        fi

        prompt_continue "Intente nuevamente"
    done
}

update_system() {
    show_progress "Limpiando caché de paquetes"
    sudo apt-get clean >> "$LOG_DIR/apt_clean.log" 2>&1
    
    show_progress "Actualizando lista de paquetes"
    if timeout 300 sudo apt-get update -y >> "$LOG_DIR/apt_update.log" 2>&1; then
        show_message "Repositorios actualizados correctamente"
    else
        log_error "Timeout o error en apt-get update"
        show_warning "Intentando solución alternativa para repositorios"
        
        if timeout 300 sudo apt-get update -y --fix-missing >> "$LOG_DIR/apt_update_retry.log" 2>&1; then
            show_message "Repositorios actualizados después de reintento"
        else
            log_error "Falló el reintento de apt-get update"
            show_error "No se pudieron actualizar los repositorios"
            return 1
        fi
    fi

    show_progress "Actualizando sistema (esto puede tomar tiempo)"
    if timeout 600 sudo apt-get upgrade -y >> "$LOG_DIR/apt_upgrade.log" 2>&1; then
        show_message "Sistema actualizado correctamente"
    else
        log_error "Timeout o error en apt-get upgrade"
        show_warning "Intentando actualización mínima"
        
        if timeout 300 sudo apt-get --fix-broken install -y >> "$LOG_DIR/apt_fix.log" 2>&1; then
            show_message "Problemas de dependencias resueltos"
        else
            log_error "Falló la reparación de dependencias"
            show_error "Error al actualizar el sistema"
            return 1
        fi
    fi

    return 0
}

install_dependencies() {
    local apt_packages=(python3 python3-pip tor cloudflared exiftool nmap termux-api dnsutils nodejs npm)
    for pkg in "${apt_packages[@]}"; do
        if ! install_pkg "$pkg"; then
            return 1
        fi
    done

    local pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    for pkg in "${pip_packages[@]}"; do
        if ! install_pip "$pkg"; then
            return 1
        fi
    done

    local npm_packages=(chalk)
    for pkg in "${npm_packages[@]}"; do
        if ! install_npm "$pkg"; then
            return 1
        fi
    done

    return 0
}

finalize_installation() {
    show_progress "Configurando entorno"
    
    if [ -f ~/Stellar/config/.bash_profile ]; then
        cp ~/Stellar/config/.bash_profile ~/.
    fi
    
    if [ -f ~/Stellar/config/.bashrc ]; then
        cp ~/Stellar/config/.bashrc ~/.
    fi

    chmod 755 ~/Stellar
    chmod 644 "$USER_FILE"

    show_message "✔ Configuración completada"
    return 0
}

main_install() {
    show_header
    
    if ! check_internet; then
        prompt_continue "Verifique su conexión a Internet y reintente"
        exit 1
    fi

    show_message "INICIANDO INSTALACIÓN DE STELLAR"
    echo -e "${gris}================================================${blanco}"

    mkdir -p ~/Stellar/{config,tools,modules}

    user_config

    if update_system; then
        if install_dependencies; then
            if finalize_installation; then
                show_header
                echo -e "${verde}¡Stellar se ha instalado correctamente!${blanco}"
                echo -e "${amarillo}Recomendamos reiniciar el sistema.${blanco}"
                
                if prompt_yesno "¿Desea reiniciar ahora?"; then
                    sudo shutdown -r now
                else
                    prompt_continue "Presione Enter para finalizar"
                    exec bash
                fi
                return 0
            fi
        fi
    fi

    show_error "La instalación no pudo completarse"
    echo -e "${amarillo}Revise los logs en $LOG_DIR para más detalles.${blanco}"
    prompt_continue "Presione Enter para salir"
    return 1
}

main_install