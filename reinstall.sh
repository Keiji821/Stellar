#!/bin/bash

CONFIG_DIR="$HOME/Stellar/config/system"
STELLAR_DIR="$HOME/Stellar"

Gris="\033[1;30m"
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

git_force_update() {
    show_progress "Actualizando repositorio Stellar"
    if [ -d "$STELLAR_DIR/.git" ]; then
        cd "$STELLAR_DIR" || return 1
        git stash
        git reset --hard
        if git pull --force; then
            show_message "Repositorio actualizado correctamente"
            return 0
        else
            show_error "Error al actualizar el repositorio"
            return 1
        fi
    else
        show_error "El directorio Stellar no es un repositorio git"
        return 1
    fi
}

reinstall_pkg() {
    local pkg=$1
    show_progress "Reinstalando $pkg"

    if command -v pkg >/dev/null; then
        pkg reinstall -y "$pkg" && return 0
    elif command -v apt-get >/dev/null; then
        apt-get install --reinstall -y "$pkg" && return 0
    elif command -v pacman >/dev/null; then
        pacman -S --noconfirm "$pkg" && return 0
    fi

    show_error "No se pudo reinstalar $pkg"
    return 1
}

reinstall_pip() {
    local pkg=$1
    show_progress "Reinstalando $pkg (pip)"

    pip uninstall -y "$pkg" >/dev/null 2>&1
    if pip install --upgrade --no-cache-dir "$pkg"; then
        show_message "$pkg reinstalado correctamente"
        return 0
    else
        show_error "No se pudo reinstalar $pkg via pip"
        return 1
    fi
}

clean_pycache() {
    show_progress "Limpiando archivos Python temporales"
    find ~/Stellar -type d -name "__pycache__" -exec rm -rf {} +
    return 0
}

reinstall_dependencies() {
    local packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    for pkg in "${packages[@]}"; do
        if ! reinstall_pkg "$pkg"; then
            return 1
        fi
    done

    local pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich lolcat discord fake_useragent pycryptodome)
    for pkg in "${pip_packages[@]}"; do
        if ! reinstall_pip "$pkg"; then
            return 1
        fi
    done

    return 0
}

restore_configs() {
    show_progress "Restaurando configuraciones"
    [ -f "$CONFIG_DIR/.bashrc" ] && cp -f "$CONFIG_DIR/.bashrc" ~/
    [ -f "$CONFIG_DIR/.bash_profile" ] && cp -f "$CONFIG_DIR/.bash_profile" ~/
    chmod 700 ~/Stellar
    return 0
}

main_reinstall() {
    show_header

    if ! check_internet; then
        show_error "Se requiere conexión a Internet para reinstalar"
        exit 1
    fi

    echo -e "${separator_color}│                                                    │${Reset}"
    echo -e "${separator_color}│  ${header_color}${Negrita}REINSTALACIÓN COMPLETA DE STELLAR${Reset}${separator_color}             │${Reset}"
    echo -e "${separator_color}│                                                    │${Reset}"
    echo -e "${separator_color}╰──────────────────────────────────────────────────────╯${Reset}"

    if ! git_force_update; then
        show_error "No se pudo actualizar el código base"
        exit 1
    fi

    if ! clean_pycache; then
        show_warning "No se pudieron limpiar algunos archivos temporales"
    fi

    if ! reinstall_dependencies; then
        show_error "Error al reinstalar dependencias"
        exit 1
    fi

    if ! restore_configs; then
        show_error "Error al restaurar configuraciones"
        exit 1
    fi

    show_header
    echo -e "${separator_color}╭──────────────────────────────────────────────────────╮${Reset}"
    echo -e "${separator_color}│                                                    │${Reset}"
    echo -e "${separator_color}│  ${success_color}${Negrita}¡REINSTALACIÓN COMPLETADA CON ÉXITO!${Reset}${separator_color}         │${Reset}"
    echo -e "${separator_color}│                                                    │${Reset}"
    echo -e "${separator_color}╰──────────────────────────────────────────────────────╯${Reset}"
    prompt_continue "Presione Enter para finalizar"
    exec bash
}

main_reinstall
