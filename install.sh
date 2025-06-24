#!/bin/bash

CONFIG_DIR="$HOME/Stellar/config/system"

Negro="\033[0;30m"
Rojo="\033[0;31m"
Verde="\033[0;32m"
Amarillo="\033[0;33m"
Azul="\033[0;34m"
Magenta="\033[0;35m"
Cian="\033[0;36m"
Blanco="\033[0;37m"

Negro_Brillante="\033[1;30m"
Rojo_Brillante="\033[1;31m"
Verde_Brillante="\033[1;32m"
Amarillo_Brillante="\033[1;33m"
Azul_Brillante="\033[1;34m"
Magenta_Brillante="\033[1;35m"
Cian_Brillante="\033[1;36m"
Blanco_Brillante="\033[1;37m"

Fondo_Negro="\033[40m"
Fondo_Rojo="\033[41m"
Fondo_Verde="\033[42m"
Fondo_Amarillo="\033[43m"
Fondo_Azul="\033[44m"
Fondo_Magenta="\033[45m"
Fondo_Cian="\033[46m"
Fondo_Blanco="\033[47m"

Fondo_Negro_Brillante="\033[0;100m"
Fondo_Rojo_Brillante="\033[0;101m"
Fondo_Verde_Brillante="\033[0;102m"
Fondo_Amarillo_Brillante="\033[0;103m"
Fondo_Azul_Brillante="\033[0;104m"
Fondo_Magenta_Brillante="\033[0;105m"
Fondo_Cian_Brillante="\033[0;106m"
Fondo_Blanco_Brillante="\033[0;107m"

Reset="\033[0m"
Negrita="\033[1m"
Atenuado="\033[2m"
Italico="\033[3m"
Subrayado="\033[4m"
Parpadeo="\033[5m"
Invertido="\033[7m"
Oculto="\033[8m"
Tachado="\033[9m"

Color8="\033[38;5;"
Fondo8="\033[48;5;"

ColorRGB="\033[38;2;"
FondoRGB="\033[48;2;"

header_color="${Cian_Brillante}${Negrita}"
success_color="${Verde_Brillante}"
warning_color="${Amarillo_Brillante}"
error_color="${Rojo_Brillante}"
prompt_color="${Magenta_Brillante}"
progress_color="${Azul_Brillante}"
info_color="${Blanco_Brillante}"
separator_color="${Fondo_Cian_Brillante}${Negro}"
box_color="${Fondo_Negro_Brillante}${Blanco_Brillante}"

show_header() {
    clear
    echo -e "${header_color}"
    echo -e "  ███████╗████████╗███████╗██╗     ██╗      █████╗ ██████╗  "
    echo -e "  ██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗██╔══██╗ "
    echo -e "  ███████╗   ██║   █████╗  ██║     ██║     ███████║██████╔╝ "
    echo -e "  ╚════██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║██╔══██╗ "
    echo -e "  ███████║   ██║   ███████╗███████╗███████╗██║  ██║██║  ██║ "
    echo -e "  ╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ "
    echo -e "${Reset}"
    echo -e "${separator_color}╭──────────────────────────────────────────────────────╮${Reset}"
}

show_message() {
    echo -e "${success_color}${Negrita}  ✦ ✔ $1${Reset}"
}

show_warning() {
    echo -e "${warning_color}${Negrita}  ✦ ⚠ $1${Reset}"
}

show_error() {
    echo -e "${error_color}${Negrita}  ✦ ✘ Error: $1${Reset}"
}

show_progress() {
    echo -e "${progress_color}${Negrita}  ✦ ➔ $1...${Reset}"
}

prompt_continue() {
    echo -e "${prompt_color}${Negrita}  ✦ $1${Reset}"
    read -rp "  ➤ Presione Enter para continuar..."
}

prompt_yesno() {
    while true; do
        read -rp "$(echo -e "${prompt_color}${Negrita}  ✦ $1 [s/n]: ${Reset}")" yn
        case $yn in
            [Ss]*) return 0 ;;
            [Nn]*) return 1 ;;
            *) echo -e "${warning_color}${Negrita}  ✦ Por favor responda s o n${Reset}" ;;
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

install_pkg() {
    local pkg=$1
    show_progress "Instalando $pkg"

    if command -v dpkg >/dev/null && dpkg -l | grep -q "^ii  $pkg "; then
        show_message "$pkg ya está instalado"
        return 0
    fi

    if command -v apt-get >/dev/null; then
        if apt-get install -y "$pkg"; then
            show_message "$pkg instalado correctamente"
            return 0
        else
            show_warning "Reintentando instalación de $pkg"
            if apt-get install -y --fix-broken "$pkg"; then
                show_message "$pkg instalado después de reintento"
                return 0
            fi
        fi
    elif command -v pkg >/dev/null; then
        if pkg install -y "$pkg"; then
            show_message "$pkg instalado correctamente"
            return 0
        fi
    elif command -v pacman >/dev/null; then
        if pacman -S --noconfirm "$pkg"; then
            show_message "$pkg instalado correctamente"
            return 0
        fi
    fi

    show_error "No se pudo instalar $pkg"
    return 1
}

install_pip() {
    local pkg=$1
    show_progress "Instalando $pkg (pip)"

    if pip show "$pkg" > /dev/null 2>&1; then
        show_message "$pkg ya está instalado (pip)"
        return 0
    fi

    if pip install --upgrade --no-cache-dir "$pkg"; then
        show_message "$pkg instalado correctamente (pip)"
        return 0
    else
        show_warning "Intentando instalación local de $pkg"
        if pip install --user --upgrade --no-cache-dir "$pkg"; then
            show_message "$pkg instalado localmente (pip)"
            return 0
        else
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

    if npm install -g "$pkg"; then
        show_message "$pkg instalado correctamente (npm)"
        return 0
    else
        show_warning "Intentando con permisos elevados"
        if npm install -g "$pkg" --unsafe-perm; then
            show_message "$pkg instalado con permisos elevados (npm)"
            return 0
        else
            show_error "No se pudo instalar $pkg via npm"
            return 1
        fi
    fi
}

update_system() {
    if command -v apt-get >/dev/null; then
        show_progress "Actualizando lista de paquetes (APT)"
        if apt-get update -y; then
            show_message "Repositorios actualizados correctamente"

            show_progress "Actualizando sistema (APT)"
            if apt-get upgrade -y; then
                show_message "Sistema actualizado correctamente"
                return 0
            fi
        fi
    elif command -v pkg >/dev/null; then
        show_progress "Actualizando sistema (Termux)"
        if pkg update -y && pkg upgrade -y; then
            show_message "Sistema actualizado correctamente"
            return 0
        fi
    elif command -v pacman >/dev/null; then
        show_progress "Actualizando sistema (Pacman)"
        if pacman -Syu --noconfirm; then
            show_message "Sistema actualizado correctamente"
            return 0
        fi
    fi

    show_error "Error al actualizar el sistema"
    return 1
}

install_dependencies() {
    local packages=()

    if command -v apt-get >/dev/null; then
        packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    elif command -v pkg >/dev/null; then
        packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    elif command -v pacman >/dev/null; then
        packages=(python tor cloudflared exiftool nmap dnsutils nodejs)
    fi

    for pkg in "${packages[@]}"; do
        if ! install_pkg "$pkg"; then
            return 1
        fi
    done

    local pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord fake_useragent pycryptodome)
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

    show_message "Configuración completada"
    return 0
}

main_install() {
    show_header

    if ! check_internet; then
        prompt_continue "Verifique su conexión a Internet y reintente"
        exit 1
    fi

    echo -e "${separator_color}│                                                    │${Reset}"
    echo -e "${separator_color}│  ${header_color}${Negrita}INSTALACIÓN DE STELLAR${Reset}${separator_color}                       │${Reset}"
    echo -e "${separator_color}│                                                    │${Reset}"
    echo -e "${separator_color}╰──────────────────────────────────────────────────────╯${Reset}"
    echo ""

    mkdir -p ~/Stellar/{config,tools,modules}

    if update_system; then
        if install_dependencies; then
            if finalize_installation; then
                show_header
                echo -e "${separator_color}╭──────────────────────────────────────────────────────╮${Reset}"
                echo -e "${separator_color}│                                                    │${Reset}"
                echo -e "${separator_color}│  ${success_color}${Negrita}¡STELLAR INSTALADO CORRECTAMENTE!${Reset}${separator_color}              │${Reset}"
                echo -e "${separator_color}│                                                    │${Reset}"
                echo -e "${separator_color}╰──────────────────────────────────────────────────────╯${Reset}"
                prompt_continue "Presione Enter para finalizar"
                exec bash
                return 0
            fi
        fi
    fi

    echo -e "${separator_color}╭──────────────────────────────────────────────────────╮${Reset}"
    echo -e "${separator_color}│                                                    │${Reset}"
    echo -e "${separator_color}│  ${error_color}${Negrita}ERROR EN LA INSTALACIÓN${Reset}${separator_color}                         │${Reset}"
    echo -e "${separator_color}│                                                    │${Reset}"
    echo -e "${separator_color}╰──────────────────────────────────────────────────────╯${Reset}"
    prompt_continue "Presione Enter para salir"
    return 1
}

main_install