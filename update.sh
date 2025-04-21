#!/usr/bin/env bash

show_lolcat_message() {
    local message="$1"
    local delay="${2:-20}"
    echo "$message" | lolcat -a -d "$delay"
}

update_repo() {
    if ! git pull --force; then
        show_lolcat_message "Error al actualizar el repositorio" 5 >&2
        return 1
    fi
    return 0
}

handle_theme_files() {
    local theme_dir="config/themes"
    local backup_dir="/tmp/stellar_theme_backup_$(date +%s)"
    
    mkdir -p "$backup_dir" || return 1
    
    cp "$theme_dir"/banner*.txt "$backup_dir"/ || return 1
    
    if ! update_repo; then
        cp "$backup_dir"/* "$theme_dir"/ && \
        show_lolcat_message "Se restauraron los archivos originales" 5
        return 1
    fi
    
    cp "$backup_dir"/* "$theme_dir"/ || return 1
    
    rm -rf "$backup_dir"
    
    return 0
}

main() {
    local original_dir="$PWD"
    
    if [[ ! -d "config/themes" ]]; then
        cd "$HOME/Stellar" || {
            show_lolcat_message "No se pudo acceder al directorio Stellar" 5 >&2
            exit 1
        }
    fi
    
    show_lolcat_message "Iniciando actualización..."
    
    git stash || {
        show_lolcat_message "Advertencia: No se pudo guardar cambios locales" 5 >&2
    }
    
    if handle_theme_files; then
        show_lolcat_message "¡Repositorio actualizado con éxito!"
        show_lolcat_message "¡Todo en orden!" 20
    else
        show_lolcat_message "Falló la actualización" 5 >&2
        exit 1
    fi
    
    cd "$original_dir" || exit 0
}

main "$@"