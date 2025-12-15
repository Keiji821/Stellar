#!/usr/bin/env bash

STELLAR_DIR="$HOME/Stellar"
CONFIG_SYSTEM_DIR="$STELLAR_DIR/linux/lang_es/config/system"
CONFIG_THEMES_DIR="$STELLAR_DIR/linux/lang_es/config/themes"

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

safe_copy() {
    if [[ ! -f "$1" ]]; then
        show_warning "Archivo no encontrado para copiar: $1"
        return 1
    fi

    if command cp -v "$1" "$2"; then
        return 0
    else
        show_error "Falló al copiar $1"
        return 1
    fi
}

create_backup() {
    local backup_dir="$HOME/stellar_backup_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$backup_dir"
    echo "$backup_dir"
}

backup_config() {
    show_progress "Resguardando archivos de configuración"

    local backup_dir=$(create_backup)

    safe_copy "$CONFIG_SYSTEM_DIR/user.txt" "$backup_dir/" || return 1
    safe_copy "$CONFIG_SYSTEM_DIR/login_method.txt" "$backup_dir/" || return 1
    safe_copy "$CONFIG_SYSTEM_DIR/password.txt" "$backup_dir/" || return 1
    safe_copy "$CONFIG_THEMES_DIR/banner.txt" "$backup_dir/" || return 1
    safe_copy "$CONFIG_THEMES_DIR/banner_color.txt" "$backup_dir/" || return 1
    safe_copy "$CONFIG_THEMES_DIR/banner_background.txt" "$backup_dir/" || return 1
    safe_copy "$CONFIG_THEMES_DIR/banner_background_color.txt" "$backup_dir/" || return 1

    safe_move "$CONFIG_SYSTEM_DIR/user.txt" "$HOME" || return 1
    safe_move "$CONFIG_SYSTEM_DIR/login_method.txt" "$HOME" || return 1
    safe_move "$CONFIG_SYSTEM_DIR/password.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner_color.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner_background.txt" "$HOME" || return 1
    safe_move "$CONFIG_THEMES_DIR/banner_background_color.txt" "$HOME" || return 1

    show_success "Backup creado en: $backup_dir"
    return 0
}

check_git() {
    if ! command -v git &>/dev/null; then
        show_error "Git no está instalado"
        return 1
    fi

    if [[ ! -d "$STELLAR_DIR/.git" ]]; then
        show_error "No es un repositorio Git válido"
        return 1
    fi

    return 0
}

update_repository() {
    show_progress "Actualizando repositorio Stellar"

    if ! check_git; then
        return 1
    fi

    if ! cd "$STELLAR_DIR"; then
        show_error "No se pudo acceder al directorio $STELLAR_DIR"
        return 1
    fi

    local has_changes=false
    if ! git diff --quiet || ! git diff --staged --quiet; then
        has_changes=true
        show_warning "Hay cambios sin guardar en el repositorio"
        if git stash push -m "Auto-stash before update $(date +%Y-%m-%d_%H:%M:%S)"; then
            show_success "Cambios guardados en stash"
        else
            show_error "Falló al guardar cambios en stash"
            return 1
        fi
    fi

    show_progress "Descargando actualizaciones"
    if git fetch origin; then
        show_success "Actualizaciones descargadas"
    else
        show_error "Falló al descargar actualizaciones"
        return 1
    fi

    show_progress "Aplicando actualizaciones"
    if git pull --rebase --autostash; then
        show_success "Actualizaciones aplicadas"
        if [[ "$has_changes" == true ]]; then
            show_progress "Restaurando cambios guardados"
            if git stash pop; then
                show_success "Cambios restaurados"
            else
                show_warning "Hubo conflictos al restaurar cambios. Revisa git stash list"
            fi
        fi
        return 0
    else
        show_error "Falló al aplicar actualizaciones"
        if [[ "$has_changes" == true ]]; then
            show_warning "Cambios guardados en stash. Usa 'git stash pop' para restaurarlos"
        fi
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

verify_update() {
    show_progress "Verificando actualización"

    if ! cd "$STELLAR_DIR"; then
        return 1
    fi

    local current_commit=$(git rev-parse HEAD)
    local remote_commit=$(git rev-parse origin/main 2>/dev/null || git rev-parse origin/master 2>/dev/null)

    if [[ -z "$remote_commit" ]]; then
        show_warning "No se pudo verificar commit remoto"
        return 1
    fi

    if [[ "$current_commit" == "$remote_commit" ]]; then
        show_success "Repositorio actualizado correctamente"
        return 0
    else
        show_error "El repositorio no está actualizado"
        return 1
    fi
}

main() {
    echo -e "${Azul_Brillante}╔══════════════════════════════════════╗${Reset}"
    echo -e "${Azul_Brillante}║     ACTUALIZADOR DE STELLAR           ║${Reset}"
    echo -e "${Azul_Brillante}╚══════════════════════════════════════╝${Reset}"
    echo ""

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

    if verify_update; then
        show_success "Actualización completada exitosamente"
        show_success "Configuración preservada y actualizada"
    else
        show_warning "Actualización completada con advertencias"
    fi
}

main "$@"