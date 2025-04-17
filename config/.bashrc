#!/bin/bash

gris="\033[1;30m"
blanco="\033[0m"
blanco2="\033[1;37m"
rojo="\033[1;31m"
rojo2="\033[31m"
azul="\033[1;34m"
azul2="\033[34m"
azul_agua="\e[1;36m"
azul_agua2="\e[36m"
verde="\033[1;32m"
verde2="\033[32m"
morado="\033[1;35m"
morado2="\033[35m"
amarillo="\033[1;33m"
amarillo2="\033[33m"
cyan="\033[38;2;23;147;209m"

clear
cd

input=$(grep -v '^[[:space:]]*$' "$HOME/.configs_stellar/themes/user.txt" 2>/dev/null || {
    mkdir -p "$HOME/.configs_stellar/themes"
    echo -ne "\033[1;32mUsuario: \033[0m"
    read -r input
    echo "$input" > "$HOME/.configs_stellar/themes/user.txt"
    echo "$input"
})

function cd() {
    builtin cd "$@" || return 1
    local current_dir="${PWD/#$HOME/\~}"
    
    declare -A colors=(
        ["user"]="\033[1;32m"
        ["host"]="\033[1;31m"
        ["path"]="\033[1;36m"
        ["symbol"]="\033[1;35m"
        ["git"]="\033[1;33m"
        ["reset"]="\033[0m"
    )

    local git_branch=$(git branch --show-current 2>/dev/null)
    local git_info=""
    
    if [ -n "$git_branch" ]; then
        git_info=" ${colors[symbol]}[${colors[git]}⎇ $git_branch${colors[symbol]}]"
    fi

    PS1="${colors[user]}${input}${colors[reset]}@${colors[host]}termux${colors[reset]}:${colors[path]}${current_dir}${git_info}${colors[reset]}"
    PS1+="\n${colors[symbol]}└─╼${colors[reset]} "
    
    echo -ne "\033]0;${input}@termux: ${current_dir}\007"
}

cd "$HOME"

clear
export ALL_PROXY=socks5h://localhost:9052
pkill tor
tor &>/dev/null &

cd
cd .configs_stellar/themes
cp ~/Stellar/config/.bash_profile ~/.
clear
python banner.py
cd
printf "${gris}[INFO] ${blanco}Stellar se ha iniciado correctamente.\n"
printf "${gris}[INFO] ${blanco}Escriba (menu) para ver los comandos disponibles.\n"

# Sistema

menu() {
    cd ~/Stellar/config
    python menu.py
    cd
}

reload() {
    cd ~/.configs_stellar/themes
    clear
    python banner.py
    cd
}

ui() {
    cd ~/Stellar/config
    python ui_config.py
    cd
}

uninstall() {
    cd ~/Stellar
    bash uninstall.sh
    cd
}

update() {
    cd ~/Stellar
    bash update.sh
    cd
}


# Osint

ipinfo() {
    cd ~/Stellar/osint/main
    python ipinfo.py
    cd
}

phoneinfo() {
    cd ~/Stellar/osint/main
    python phoneinfo.py
    cd
}

urlinfo() {
    cd ~/Stellar/osint/main
    python urlinfo.py
    cd
}

metadatainfo() {
    cd ~/Stellar/osint/main
    bash metadatainfo.sh
    cd
}

emailsearch() {
    cd ~/Stellar/osint/main
    python emailfinder.py
    cd
}

userfinder() {
    cd ~/Stellar/osint/main
    python userfinder.py
    cd
}

userinfo() {
    cd ~/Stellar/osint/discord
    python userinfo.py
    cd
}

# Pentest

ddos() {
    cd ~/Stellar/pentesting
    python ddos.py
    cd
}

# Misc

ia() {
    cd ~/Stellar/misc/tools
    python iahttp.py
    cd
}

ia-image() {
    cd ~/Stellar/misc/tools
    python ia_image.py
    cd
}

traductor() {
    cd ~/Stellar/misc/tools
    python traductor.py
    cd
}

myip() {
    cd ~/Stellar/misc/tools
    python myip.py
    cd
}

command_not_found_handle() {
    echo -e "${gris}[INFO] ${blanco}Comando no encontrado: $1"
    return 127
}