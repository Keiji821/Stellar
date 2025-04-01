#!/bin/bash
set -euo pipefail

gris="\033[1;30m"
blanco="\033[0m"
blanco2="\033[1;37m"
rojo="\033[1;31m"
rojo2="\033[31m"
azul="\033[1;34m"
azul2="\033[34m"
verde="\033[1;32m"
verde2="\033[32m"
morado="\033[1;35m"
morado2="\033[35m"
amarillo="\033[1;33m"
amarillo2="\033[1;33m"
cyan="\033[38;2;23;147;209m"

log_info()    { echo -e "\n${cyan}[INFO]${blanco} $*\n"; }
log_success() { echo -e "\n${verde}[SUCCESS]${blanco} $*\n"; }
log_error()   { echo -e "\n${rojo}[ERROR]${blanco} $*\n"; }

export TMPDIR="$HOME/tmp"
mkdir -p "$TMPDIR"

INPUT_FILE="$HOME/.configs_stellar/themes/input.txt"
input=$(cat "$INPUT_FILE" 2>/dev/null || echo "default")

update_prompt() {
    local pwd_relative="${PWD/#$HOME}"
    pwd_relative=${pwd_relative#/}
    PS1="${azul}${morado}(${pwd_relative:-~}) ${azul}${verde}${input}${azul} ${amarillo}~${verde} \$ ${blanco2}"
}

cd() {
    builtin cd "$@" && update_prompt || log_error "Error al cambiar de directorio"
}

update_prompt

if command -v termux-setup-storage -y &>/dev/null; then
    termux-setup-storage
fi

clear

export ALL_PROXY="socks5h://localhost:9050"

LOG_FILE="$TMPDIR/stellar_bg.log"
touch "$LOG_FILE"

run_bg() {
    local cmd="$1"
    log_info "Ejecutando en segundo plano: $cmd"
    eval "$cmd" >>"$LOG_FILE" 2>&1 & disown
}

run_bg "python Stellar/config/run.py"

[ -f "$HOME/Stellar/config/.bash_profile" ] && cp "$HOME/Stellar/config/.bash_profile" "$HOME/."

cd .configs_stellar/themes
python banner.py
cd

run_script() {
    local path="$1"
    local script="$2"
    if [ -f "$path/$script" ]; then
        log_info "Ejecutando $path/$script"
        python "$path/$script" || log_error "Error ejecutando $path/$script"
    else
        log_error "Script no encontrado: $path/$script"
    fi
}

run_bash() {
    local path="$1"
    local script="$2"
    if [ -f "$path/$script" ]; then
        log_info "Ejecutando $path/$script (bash)"
        bash "$path/$script" || log_error "Error ejecutando $path/$script"
    else
        log_error "Script no encontrado: $path/$script"
    fi
}

ipinfo()       { run_script "Stellar/osint/main" "ipinfo.py"; }
phoneinfo()    { run_script "Stellar/osint/main" "phoneinfo.py"; }
urlinfo()      { run_script "Stellar/osint/main" "urlinfo.py"; }
metadatainfo() { run_bash "Stellar/osint/main" "metadatainfo.sh"; }
emailsearch()  { run_script "Stellar/osint/main" "emailfinder.py"; }
userfinder()   { run_script "Stellar/osint/main" "userfinder.py"; }
userinfo()     { run_script "Stellar/osint/discord" "userinfo.py"; }
ddos()         { run_script "Stellar/pentesting" "ddos.py"; }
menu()         { run_script "Stellar/config" "menu.py"; }
reload()       { clear; run_bg "python ~/.configs_stellar/themes/banner.py"; update_prompt; }
ui()           { run_script "Stellar/config" "ui_config.py"; }
ia()           { run_script "Stellar/misc/tools" "iahttp.py"; }
ia_image()     { run_script "Stellar/misc/tools" "ia_image.py"; }
traductor()    { run_script "Stellar/misc/tools" "traductor.py"; }
myip()         { run_script "Stellar/misc/tools" "myip.py"; }

stellar_update() {
    log_info "Actualizando Stellar OS..."
    if cd ~/Stellar && git pull; then
        log_success "Actualización completada"
    else
        log_error "Error en la actualización"
    fi
}

open_stellar_config() { cd ~/Stellar/config && ls -la; }

clear_logs() { : > "$LOG_FILE" && log_success "Logs limpiados"; }

system_status() {
    log_info "Estado del sistema:"
    echo -e "${amarillo}Memoria:${blanco}"
    free -h
    echo -e "\n${amarillo}Disco:${blanco}"
    df -h
    echo ""
}

check_network() {
    log_info "Comprobando conectividad (ping a google.com)..."
    if ping -c 2 google.com &>/dev/null; then
        log_success "Conectividad OK"
    else
        log_error "Problema de conectividad"
    fi
}

backup_config() {
    local backup_file="$HOME/stellar_config_backup_$(date +%Y%m%d_%H%M%S).tar.gz"
    tar -czf "$backup_file" ~/Stellar/config && log_success "Backup realizado en: $backup_file" || log_error "Error en el backup"
}

export -f update_prompt cd run_script run_bash ipinfo phoneinfo urlinfo metadatainfo emailsearch userfinder userinfo ddos menu reload ui ia ia_image traductor myip stellar_update open_stellar_config clear_logs system_status check_network backup_config log_info log_success log_error

log_success "Stellar OS cargado. Usa los comandos disponibles para gestionar el sistema."