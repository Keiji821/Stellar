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

# ┌────────────────────────────────┐
# │ Cleaning and starting                 │
# └────────────────────────────────┘


clear
history -c && rm -f ~/.bash_history
cd


# ┌────────────────────────────────┐
# │ Security lock for the screen          │
# └────────────────────────────────┘


# Método de desbloqueo - Huella dactilar
cd ~/Stellar/lang_es/config/system

if [ -f login_method.txt ]; then
    method=$(cat login_method.txt)

    if [ "$method" = "termux-fingerprint" ]; then
        termux-toast -c red -b black -g medium "🔐 Verificación de huella requerida"

        response=$(termux-fingerprint)
        auth_result=$(echo "$response" | grep -o '"auth_result": "[^"]*' | cut -d'"' -f4)

        case "$auth_result" in
            "AUTH_RESULT_SUCCESS")
                termux-toast -c green -b black -g medium "✅ Autenticación exitosa"
                ;;
            "AUTH_RESULT_FAILURE")
                termux-toast -c red -b black -g medium "⛔ Autenticación fallida - Cerrando sesión..."
                nohup bash -c '
                    pkill -9 -f "/data/data/com.termux/files/usr/bin/bash"
                    pkill -9 -f "com.termux"
                    am stopservice com.termux/.app.TermuxService
                    sleep 1
                    pkill -9 -f "termux"
                ' >/dev/null 2>&1 &
                exit 1
                ;;
            *)
                termux-toast -c red -b black -g medium "❌ Error en verificación - Cerrando sesión..."
                nohup bash -c '
                    pkill -9 -f "/data/data/com.termux/files/usr/bin/bash"
                    pkill -9 -f "com.termux"
                    am stopservice com.termux/.app.TermuxService
                    sleep 1
                    pkill -9 -f "termux"
                ' >/dev/null 2>&1 &
                exit 1
                ;;
        esac
    fi
fi

cd


# ┌────────────────────────────────┐
# │ Definition of PS1 (input)             │
# └────────────────────────────────┘


input=$(grep -v '^[[:space:]]*$' "$HOME/Stellar/lang_es/config/system/user.txt" 2>/dev/null || {
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

# ┌────────────────────────────────┐
# │ Security                              │
# └────────────────────────────────┘


pkill -f "tor"
pkill -f "9052"
export puerto="9052"
export ALL_PROXY="socks5h://localhost:${puerto}"
tor --SocksPort $puerto \
    --NewCircuitPeriod 60 \
    --MaxCircuitDirtiness 600 \
    --NumEntryGuards 7 \
    --CircuitBuildTimeout 60 \
    --ClientOnly 1 \
    --AvoidDiskWrites 1 \
    &>tor.txt &

# ┌────────────────────────────────┐
# │ Imports and banner                    │
# └────────────────────────────────┘

cp ~/Stellar/lang_es/config/.bash_profile ~/.
cd ~/Stellar/lang_es/config/themes
clear
python banner.py
cd
printf "${Gris}[INFO] ${Blanco_Brillante}Stellar se ha iniciado correctamente.\n"
printf "${Gris}[INFO] ${Blanco_Brillante}Escriba ${Fondo_Azul}${Blanco_Brillante}menu${Reset} para ver los comandos disponibles.\n"


# ┌────────────────────────────────┐
# │ Definition of commands                │
# └────────────────────────────────┘

# Sistema

menu() {
    cd ~/Stellar/lang_es/config
    python menu.py
    cd
}

reload() {
    cd ~/Stellar/lang_es/config/themes
    clear
    python banner.py
    cd
}

user-config() {
    cd ~/Stellar/lang_es/config
    python user_config.py
    cd
}

uninstall() {
    cd ~/Stellar
    bash uninstall.sh
    cd
}

update() {
    cd ~/Stellar/lang_es
    bash update.sh
    cd
}

reinstall() {
    cd ~/Stellar
    bash reinstall.sh
    cd
}

my() {
    cd ~/Stellar/lang_es/config/system
    python user.py
    cd
}

# Discord

weebhook-mass-spam() {
    cd ~/Stellar/lang_es/commands/general/discord/weebhookraid
    python weebhook_mass_spam.py
    cd
}

mass-delete-channels() {
    cd ~/Stellar/lang_es/commands/general/discord/botraid
    python mass_delete_channels.py
    cd
}

# Osint

ipinfo() {
    cd ~/Stellar/lang_es/commands/osint/main
    python ipinfo.py
    cd
}

phoneinfo() {
    cd ~/Stellar/lang_es/commands/osint/main
    python phoneinfo.py
    cd
}

urlinfo() {
    cd ~/Stellar/lang_es/commands/osint/main
    python urlinfo.py
    cd
}

metadatainfo() {
    cd ~/Stellar/lang_es/commands/osint/main
    bash metadatainfo.sh
    cd
}

emailsearch() {
    cd ~/Stellar/lang_es/commands/osint/main
    python emailfinder.py
    cd
}

userfinder() {
    cd ~/Stellar/lang_es/commands/osint/main
    python userfinder.py
    cd
}


# Osint/Discord

userinfo() {
    cd ~/Stellar/lang_es/commands/osint/discord
    python userinfo.py
    cd
}

serverinfo() {
    cd ~/Stellar/lang_es/commands/osint/discord
    python serverinfo.py
    cd
}

searchinvites() {
    cd ~/Stellar/lang_es/commands/osint/discord
    python searchserverinvites.py
    cd
}

inviteinfo() {
    cd ~/Stellar/lang_es/commands/osint/discord
    python inviteinfo.py
    cd
}

role-mapper() {
    cd ~/Stellar/lang_es/commands/osint/discord
    python role_mapper.py
    cd
}

mutual-servers() {
    cd ~/Stellar/lang_es/commands/osint/discord
    python mutual_servers.py
    cd
}

# Osint/Instagram

profileinfo() {
    cd ~/Stellar/lang_es/commands/osint/instagram
    python profileinfo.py
    cd
}

# Pentest

ddos() {
    cd ~/Stellar/lang_es/commands/pentesting/main
    node ddos.js
    cd
}

# Networks

traceroute() {
    cd ~/Stellar/lang_es/commands/networks
    python traceroute.py
    cd
}

# Phishing

tunnel() {
    cd ~/Stellar/lang_es/commands/phishing
    python tunnel.py
    cd
}

# Misc

ia() {
    cd ~/Stellar/lang_es/commands/misc/tools
    python iahttp.py
    cd
}

ia-image() {
    cd ~/Stellar/lang_es/commands/misc/tools
    python ia_image.py
    cd
}

traductor() {
    cd ~/Stellar/lang_es/commands/misc/tools
    python traductor.py
    cd
}

myip() {
    cd ~/Stellar/lang_es/commands/misc/tools
    python myip.py
    cd
}

passwordgen() {
    cd ~/Stellar/lang_es/commands/misc/tools
    python passwordgen.py
    cd
}

encrypt-file() {
    cd ~/Stellar/lang_es/commands/misc/tools
    python encrypt-file.py
    cd
}

# ┌────────────────────────────────┐
# │ Termux Properties and Modifications   │
# └────────────────────────────────┘

cd ~/.termux
cat > termux.properties << 'EOF'
# allow-external-apps = true
# default-working-directory = /data/data/# com.termux/files/home
# disable-terminal-session-change-toast = # true
# hide-soft-keyboard-on-startup = true
# soft-keyboard-toggle-behaviour = enable/disable
# terminal-transcript-rows = 2000
volume-keys = volume

# fullscreen = true
# use-fullscreen-workaround = true

# terminal-cursor-blink-rate = 0
terminal-cursor-style = bar

extra-keys-style = arrows-only
# extra-keys-text-all-caps = true
extra-keys = [[ESC, TAB, CTRL, ALT, {key: '-', popup: '|'}, DOWN, UP]]
extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'], \
              ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]

# use-black-ui = true

# disable-hardware-keyboard-shortcuts = true
# shortcut.create-session = ctrl + t
# shortcut.next-session = ctrl + 2
# shortcut.previous-session = ctrl + 1
# shortcut.rename-session = ctrl + n

# bell-character = vibrate
# back-key=escape

# enforce-char-based-input = true
# ctrl-space-workaround = true

# terminal-margin-horizontal=3
# terminal-margin-vertical=0
EOF
cd

alias ls='lsd --icon-theme unicode'
alias delete='rm -rf'
alias move='mv'
alias copy='cp'
x11() {
termux-x11 :0 &
export DISPLAY=:0
}

command_not_found_handle() {
    echo -e "${Gris}[INFO] ${Blanco_Brillante}Comando no encontrado: $1"
    return 127
}
