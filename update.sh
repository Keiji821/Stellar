#!/usr/bin/env bash

STELLAR_DIR="$HOME/Stellar"
CONFIG_SYSTEM_DIR="$STELLAR_DIR/config/system"
CONFIG_THEMES_DIR="$STELLAR_DIR/config/themes"

show_message() {
    local message="$1"
    local delay="${2:-20}"
    echo
    echo "==========================================================="
    echo "$message" | lolcat -a -d "$delay"
    echo "==========================================================="
    echo
}

safe_move() {
    local src="$1"
    local dest="$2"
    
    if [[ ! -f "$src" ]]; then
        echo "Advertencia: Archivo no encontrado: $src" >&2
        return 1
    fi
    
    if ! mv -v "$src" "$dest"; then
        echo "Error crítico moviendo $src" >&2
        return 1
    fi
    return 0
}

backup_config() {
    show_message "Resguardando archivos de configuración..."
    
    safe_move "$CONFIG_SYSTEM_DIR/user.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner_color.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner_background.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner_background_color.txt" "$HOME" || return 1
    
    return 0
}

update_repository() {
    show_message "Actualizando repositorio Stellar..."
    
    if ! cd "$STELLAR_DIR"; then
        echo "Error: No se pudo acceder al directorio $STELLAR_DIR" >&2
        return 1
    fi
    
    if ! git stash push -m "Auto-stash before update"; then
        echo "Advertencia: Falló el stash de cambios" >&2
    fi
    
    if ! git pull --rebase --autostash; then
        echo "Error crítico al actualizar el repositorio" >&2
        return 1
    fi
    
    return 0
}

restore_config() {
    show_message "Restaurando configuraciones..."
    
    safe_move "$HOME/user.txt" "$CONFIG_SYSTEM_DIR/" || return 1
    safe_move "$HOME/banner.txt" "$CONFIG_THEMES_DIR/" || return 1
    safe_move "$HOME/banner_color.txt" "$CONFIG_THEMES_DIR/" || return 1
    safe_move "$HOME/banner_background.txt" "$CONFIG_THEMES_DIR/" || return 1
    safe_move "$HOME/banner_background_color.txt" "$CONFIG_THEMES_DIR/" || return 1
    
    return 0
}

main() {
    if ! backup_config; then
        show_message "Advertencia: Algunos archivos no se resguardaron" 5
    fi
    
    if ! update_repository; then
        show_message "FALLA CRÍTICA: No se pudo actualizar Stellar" 5
        exit 1
    fi
    
    if ! restore_config; then
        show_message "Advertencia: Algunas configuraciones no se restauraron" 5
    fi
    
    show_message "¡Actualización completada exitosamente!"
    echo
    show_message "Configuración personalizada preservada" 10
}

main