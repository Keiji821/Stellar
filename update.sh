#!/usr/bin/env bash

STELLAR_DIR="$HOME/Stellar"
CONFIG_SYSTEM_DIR="$STELLAR_DIR/config/system"
CONFIG_THEMES_DIR="$STELLAR_DIR/config/themes"

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

show_message() {
    local message="$1"
    echo -e "\n${Azul_Brillante}╭──────────────────────────────────────────────╮"
    echo -e "│  ${Blanco}$message${Azul_Brillante}     │"
    echo -e "╰──────────────────────────────────────────────╯${Reset}"
}

show_progress() {
    local message="$1"
    echo -e "${Azul_Brillante}➤ ${Blanco}$message...${Reset}"
}

show_warning() {
    local message="$1"
    echo -e "${Amarillo_Brillante}⚠ ${Amarillo}$message${Reset}"
}

show_success() {
    local message="$1"
    echo -e "${Verde_Brillante}✔ ${Verde}$message${Reset}"
}

show_error() {
    local message="$1"
    echo -e "${Rojo_Brillante}✘ ${Rojo}Error: $message${Reset}"
}

safe_move() {
    local src="$1"
    local dest="$2"

    if [[ ! -f "$src" ]]; then
        show_warning "Archivo no encontrado: $src"
        return 1
    fi

    if mv -v "$src" "$dest"; then
        return 0
    else
        show_error "Falló al mover $src"
        return 1
    fi
}

backup_config() {
    show_progress "Resguardando archivos de configuración"

    safe_move "$CONFIG_SYSTEM_DIR/user.txt" "$HOME" || return 1
    safe_move "$CONFIG_SYSTEM_DIR/login_method.txt" "$HOME" || return 1
    safe_move "$CONFIG_SYSTEM_DIR/password.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner_color.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner_background.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner_background_color.txt" "$HOME" || return 1

    return 0
}

update_repository() {
    show_progress "Actualizando repositorio Stellar"

    if ! cd "$STELLAR_DIR"; then
        show_error "No se pudo acceder al directorio $STELLAR_DIR"
        return 1
    fi

    if ! git stash push -m "Auto-stash before update"; then
        show_warning "Falló el stash de cambios"
    fi

    if git pull --rebase --autostash; then
        return 0
    else
        show_error "Falló al actualizar el repositorio"
        return 1
    fi
}

restore_config() {
    show_progress "Restaurando configuraciones"

    safe_move "$HOME/user.txt" "$CONFIG_SYSTEM_DIR/" || return 1
    safe_move "$HOME/login_method.txt" "$CONFIG_SYSTEM_DIR/" || return 1
    safe_move "$HOME/password.txt" "$CONFIG_SYSTEM_DIR/" || return 1
    safe_move "$HOME/banner.txt" "$CONFIG_THEMES_DIR/" || return 1
    safe_move "$HOME/banner_color.txt" "$CONFIG_THEMES_DIR/" || return 1
    safe_move "$HOME/banner_background.txt" "$CONFIG_THEMES_DIR/" || return 1
    safe_move "$HOME/banner_background_color.txt" "$CONFIG_THEMES_DIR/" || return 1

    return 0
}

main() {
    echo -e "${Cian}"
    echo -e "  ███████╗████████╗███████╗██╗     ██╗      █████╗ ██████╗  "
    echo -e "  ██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗██╔══██╗ "
    echo -e "  ███████╗   ██║   █████╗  ██║     ██║     ███████║██████╔╝ "
    echo -e "  ╚════██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║██╔══██╗ "
    echo -e "  ███████║   ██║   ███████╗███████╗███████╗██║  ██║██║  ██║ "
    echo -e "  ╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ${Reset}"
    echo -e "${Azul_Brillante}╭──────────────────────────────────────────────╮"
    echo -e "│          ${Blanco}ACTUALIZACIÓN DE STELLAR${Azul_Brillante}            │"
    echo -e "╰──────────────────────────────────────────────╯${Reset}"

    if ! backup_config; then
        show_warning "Algunos archivos no se resguardaron"
    fi

    if ! update_repository; then
        show_message "FALLA CRÍTICA: No se pudo actualizar Stellar"
        exit 1
    fi

    if ! restore_config; then
        show_warning "Algunas configuraciones no se restauraron"
    fi

    show_message "¡Actualización completada exitosamente!"
    show_success "Configuración personalizada preservada"
}

main
echo
echo