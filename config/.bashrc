#!/bin/bash

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

clear
cd

# Método de desbloqueo - Huella dactilar
if [ -f ~/Stellar/config/system/login_method.txt ]; then
    method=$(cat ~/login_method.txt)
    if [ "$method" == "termux-fingerprint" ]; then
        termux-fingerprint
        if [ $? -ne 0 ]; then
            killall -9 bash 2>/dev/null
            pkill -9 -u $(whoami) 2>/dev/null
            exit 1
        fi
    elif [ "$method" == "no" ]; then
        :
    fi
fi

input=$(grep -v '^[[:space:]]*$' "$HOME/Stellar/config/system/user.txt" 2>/dev/null || {
    echo -ne "\033[1;32mUsuario: \033[0m"
    read -r input
    echo "$input" > "$HOME/Stellar/config/system/user.txt"
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

pkill -f "tor"
pkill -f 9052
export puerto="9052"
export ALL_PROXY="socks5h://localhost:${puerto}"
tor --SocksPort $puerto &>tor.txt &

cp ~/Stellar/config/.bash_profile ~/.
cd Stellar/config/themes
clear
python banner.py
cd
printf "${Gris}[INFO] ${Blanco_Brillante}Stellar se ha iniciado correctamente.\n"
printf "${Gris}[INFO] ${Blanco_Brillante}Escriba ${Fondo_Azul}${Blanco_Brillante}menu${Reset} para ver los comandos disponibles.\n"

# Sistema

menu() {
    cd ~/Stellar/config
    python menu.py
    cd
}

reload() {
    cd ~/Stellar/config/themes
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

my() {
    cd ~/Stellar/config/system
    python user.py
    cd
}

userconf() {
    cd ~/Stellar/config/system
    bash user.sh
    cd
}

# Discord

weebhook-mass-spam() {
    cd ~/Stellar/commands/general/Discord/weebhookraid
    python weebhook_mass_spam.py
    cd
}

mass-delete-channels() {
    cd ~/Stellar/commands/general/Discord/botraid
    python mass_delete_channels.py
    cd
}

# Osint

ipinfo() {
    cd ~/Stellar/commands/osint/main
    python ipinfo.py
    cd
}

phoneinfo() {
    cd ~/Stellar/commands/osint/main
    python phoneinfo.py
    cd
}

urlinfo() {
    cd ~/Stellar/commands/osint/main
    python urlinfo.py
    cd
}

metadatainfo() {
    cd ~/Stellar/commands/osint/main
    bash metadatainfo.sh
    cd
}

emailsearch() {
    cd ~/Stellar/commands/osint/main
    python emailfinder.py
    cd
}

userfinder() {
    cd ~/Stellar/commands/osint/main
    python userfinder.py
    cd
}


# Osint/Discord

userinfo() {
    cd ~/Stellar/commands/osint/discord
    python userinfo.py
    cd
}

serverinfo() {
    cd ~/Stellar/commands/osint/discord
    python serverinfo.py
    cd
}

searchinvites() {
    cd ~/Stellar/commands/osint/discord
    python searchserverinvites.py
    cd
}

inviteinfo() {
    cd ~/Stellar/commands/osint/discord
    python inviteinfo.py
    cd
}

role-mapper() {
    cd ~/Stellar/commands/osint/discord
    python role_mapper.py
    cd
}

mutual-servers() {
    cd ~/Stellar/commands/osint/discord
    python mutual_servers.py
    cd
}

# Osint/Instagram

profileinfo() {
    cd ~/Stellar/commands/osint/instagram
    python profileinfo.py
    cd
}

# Pentest

ddos() {
    cd ~/Stellar/commands/pentesting/main
    node ddos.js
    cd
}

# Networks

traceroute() {
    cd ~/Stellar/commands/networks
    python traceroute.py
    cd
}

# Phishing

tunnel() {
    cd ~/Stellar/commands/phishing
    python tunnel.py
    cd
}

# Misc

ia() {
    cd ~/Stellar/commands/misc/tools
    python iahttp.py
    cd
}

ia-image() {
    cd ~/Stellar/commands/misc/tools
    python ia_image.py
    cd
}

traductor() {
    cd ~/Stellar/commands/misc/tools
    python traductor.py
    cd
}

myip() {
    cd ~/Stellar/commands/misc/tools
    python myip.py
    cd
}

passwordgen() {
    cd ~/Stellar/commands/misc/tools
    python passwordgen.py
    cd
}

encrypt-file() {
    cd ~/Stellar/commands/misc/tools
    python encrypt-file.py
    cd
}

command_not_found_handle() {
    echo -e "${Gris}[INFO] ${Blanco_Brillante}Comando no encontrado: $1"
    return 127
}