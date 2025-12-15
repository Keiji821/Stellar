#!/usr/bin/env bash

STELLAR_DIR="$HOME/Stellar"
CONFIG_SYSTEM_DIR="$STELLAR_DIR/termux/lang_es/config/system"
CONFIG_THEMES_DIR="$STELLAR_DIR/termux/lang_es/config/themes"

show_progress() {
    echo -e "${Azul_Brillante}➤ ${Blanco}$1...${Reset}"
}

show_warning() {
    echo -e "${Amarillo_Brillante}⚠ ${Amarillo}$1${Reset}"
}

show_success() {
    echo -e "${Verde_Brillante}✔ ${Verde}$1${Reset}"
}

show_error() {
    echo -e "${Rojo_Brillante}✘ ${Rojo}Error: $1${Reset}"
}

safe_move() {
    if [[ ! -f "$1" ]]; then
        show_warning "Archivo no encontrado: $1"
        return 1
    fi

    if command mv -v "$1" "$2"; then
        return 0
    else
        show_error "Falló al mover $1"
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
    if ! backup_config; then
        show_warning "Algunos archivos no se resguardaron"
    fi

    if ! update_repository; then
        show_error "No se pudo actualizar Stellar"
        exit 1
    fi

    if ! restore_config; then
        show_warning "Algunas configuraciones no se restauraron"
    fi

    show_success "Actualización completada - Configuración preservada"
}

main