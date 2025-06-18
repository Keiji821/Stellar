#!/bin/bash

CONFIG_DIR="$HOME/Stellar/config/system"
USER_FILE="$CONFIG_DIR/user.txt"

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
    echo -e "${verde}$1${blanco}"
}

show_warning() {
    echo -e "${amarillo}$1${blanco}"
}

show_error() {
    echo -e "${rojo}✘ Error: $1${blanco}"
}

show_progress() {
    echo -e "${cyan}➔ $1${blanco}"
}

prompt_continue() {
    echo -e "${morado}$1${blanco}"
    read -p "Presione Enter para continuar..."
}

prompt_yesno() {
    while true; do
        read -p "$(echo -e "${morado}$1 [s/n]: ${blanco}")" yn
        case $yn in
            [Ss]*) return 0 ;;
            [Nn]*) return 1 ;;
            *) echo -e "${amarillo}Por favor responda s o n${blanco}" ;;
        esac
    done
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
    show_progress "Instalando $pkg..."
    
    if dpkg -s "$pkg" &> /dev/null; then
        show_message "✔ $pkg ya está instalado"
        return 0
    fi
    
    if apt install -y "$pkg" &> /dev/null; then
        show_message "✔ $pkg instalado correctamente"
        return 0
    else
        show_warning "Reintentando instalación de $pkg..."
        if apt install -y --reinstall "$pkg" &> /dev/null; then
            show_message "✔ $pkg instalado después de reintento"
            return 0
        else
            show_error "No se pudo instalar $pkg"
            return 1
        fi
    fi
}

install_pip() {
    local pkg=$1
    show_progress "Instalando $pkg..."
    
    if pip show "$pkg" &> /dev/null; then
        show_message "✔ $pkg ya está instalado"
        return 0
    fi
    
    if pip install --no-cache-dir "$pkg" &> /dev/null; then
        show_message "✔ $pkg instalado correctamente"
        return 0
    else
        show_warning "Intentando instalación local de $pkg..."
        if pip install --user --no-cache-dir "$pkg" &> /dev/null; then
            show_message "✔ $pkg instalado localmente"
            return 0
        else
            show_error "No se pudo instalar $pkg"
            return 1
        fi
    fi
}

install_npm() {
    local pkg=$1
    show_progress "Instalando $pkg..."
    
    if npm list -g "$pkg" &> /dev/null; then
        show_message "✔ $pkg ya está instalado"
        return 0
    fi
    
    if npm install -g "$pkg" &> /dev/null; then
        show_message "✔ $pkg instalado correctamente"
        return 0
    else
        show_warning "Intentando con permisos elevados para $pkg..."
        if npm install -g "$pkg" --unsafe-perm &> /dev/null; then
            show_message "✔ $pkg instalado con permisos elevados"
            return 0
        else
            show_error "No se pudo instalar $pkg"
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
        read -p "Nombre de usuario: " username
        
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
    show_progress "Actualizando lista de paquetes..."
    if apt update -y &> /dev/null; then
        show_message "✔ Repositorios actualizados correctamente"
    else
        show_warning "Intentando solución alternativa para repositorios..."
        if apt update -y --fix-missing &> /dev/null; then
            show_message "✔ Repositorios actualizados después de reintento"
        else
            show_error "No se pudieron actualizar los repositorios"
            return 1
        fi
    fi
    
    show_progress "Actualizando sistema..."
    if apt upgrade -y &> /dev/null; then
        show_message "✔ Sistema actualizado correctamente"
        return 0
    else
        show_error "Error al actualizar el sistema"
        return 1
    fi
}

install_dependencies() {
    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    for pkg in "${apt_packages[@]}"; do
        install_pkg "$pkg" || return 1
    done
    
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    for pkg in "${pip_packages[@]}"; do
        install_pip "$pkg" || return 1
    done
    
    npm_packages=(chalk)
    for pkg in "${npm_packages[@]}"; do
        install_npm "$pkg" || return 1
    done
    
    return 0
}

main_install() {
    show_header
    show_message "INICIANDO INSTALACIÓN DE STELLAR"
    echo -e "${gris}================================================${blanco}"
    
    mkdir -p ~/Stellar
    
    user_config
    
    if update_system; then
        if install_dependencies; then
            show_message "✔ INSTALACIÓN COMPLETADA EXITOSAMENTE"
            sleep 2
            
            show_progress "Configurando entorno..."
            cp ~/Stellar/config/.bash_profile ~/.
            cp ~/Stellar/config/.bashrc ~/.
            
            show_header
            echo -e "${verde}¡Stellar se ha instalado correctamente!${blanco}"
            prompt_continue "Presione Enter para finalizar"
            
            exec bash
            return 0
        fi
    fi
    
    show_error "La instalación no pudo completarse"
    prompt_continue "Presione Enter para salir"
    return 1
}

main_install