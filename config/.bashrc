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
amarillo2="\033[33m"
cyan="\033[38;2;23;147;209m"

input=$(cat ~/.configs_stellar/themes/input.txt)

update_prompt() {
    local pwd_relative="${PWD/#$HOME}"
    pwd_relative=${pwd_relative#/}
    PS1="${azul}${morado}(${pwd_relative}) ${azul}${verde}${input}${azul} ${amarillo}~${verde} $ ${blanco2}"
}

cd() {
    builtin cd "$@" || return
    update_prompt
}

clear
export ALL_PROXY=socks5h://localhost:9050
python Stellar/config/run.py

cp ~/Stellar/config/.bash_profile ~/.
clear
cd .configs_stellar/themes
python banner.py
cd

run_script() {
    local path="$1"
    local script="$2"
    [ -f "$path/$script" ] && python "$path/$script"
}

# OSINT - Main
ipinfo() { run_script "Stellar/osint/main" "ipinfo.py"; }
phoneinfo() { run_script "Stellar/osint/main" "phoneinfo.py"; }
urlinfo() { run_script "Stellar/osint/main" "urlinfo.py"; }
metadatainfo() { bash "Stellar/osint/main/metadatainfo.sh"; }
emailsearch() { run_script "Stellar/osint/main" "emailfinder.py"; }
userfinder() { run_script "Stellar/osint/main" "userfinder.py"; }

# OSINT - Discord
userinfo() { run_script "Stellar/osint/discord" "userinfo.py"; }

# Pentesting
ddos() { run_script "Stellar/pentesting" "ddos.py"; }

# Sistema
menu() { run_script "Stellar/config" "menu.py"; }
reload() { clear; python ~/.configs_stellar/themes/banner.py; }
ui() { run_script "Stellar/config" "ui_config.py"; }

# Utilidades - herramientas
ia() { run_script "Stellar/misc/tools" "iahttp.py"; }
ia-image() { run_script "Stellar/misc/tools" "ia_image.py"; }
traductor() { run_script "Stellar/misc/tools" "traductor.py"; }
myip() { run_script "Stellar/misc/tools" "myip.py"; }
