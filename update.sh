#!/usr/bin/env bash

update_repo() {
    if ! git pull --force; then
        echo "Error al actualizar el repositorio" >&2
        exit 1
    fi
}

show_lolcat_message() {
    local message="$1"
    local delay="${2:-20}"
    echo "$message" | lolcat -a -d "$delay"
}

show_lolcat_message "Iniciando actualización..."
if update_repo; then
    show_lolcat_message "¡Repositorio actualizado con éxito!"
else
    show_lolcat_message "Falló la actualización" 5
    exit 1
fi