#!/bin/bash
if [ -n "$PS1" ]; then
chmod +x ~/Stellar/plugins/*.sh ~/Stellar/plugins/*.py 2>/dev/null
source venv/bin/activate
export Gris="\033[1;30m"
export Negro="\033[0;30m"
export Rojo="\033[0;31m"
export Verde="\033[0;32m"
export Amarillo="\033[0;33m"
export Azul="\033[0;34m"
export Magenta="\033[0;35m"
export Cian="\033[0;36m"
export Blanco="\033[0;37m"

export Negro_Brillante="\033[1;30m"
export Rojo_Brillante="\033[1;31m"
export Verde_Brillante="\033[1;32m"
export Amarillo_Brillante="\033[1;33m"
export Azul_Brillante="\033[1;34m"
export Magenta_Brillante="\033[1;35m"
export Cian_Brillante="\033[1;36m"
export Blanco_Brillante="\033[1;37m"

export Fondo_Negro="\033[40m"
export Fondo_Rojo="\033[41m"
export Fondo_Verde="\033[42m"
export Fondo_Amarillo="\033[43m"
export Fondo_Azul="\033[44m"
export Fondo_Magenta="\033[45m"
export Fondo_Cian="\033[46m"
export Fondo_Blanco="\033[47m"

export Fondo_Negro_Brillante="\033[0;100m"
export Fondo_Rojo_Brillante="\033[0;101m"
export Fondo_Verde_Brillante="\033[0;102m"
export Fondo_Amarillo_Brillante="\033[0;103m"
export Fondo_Azul_Brillante="\033[0;104m"
export Fondo_Magenta_Brillante="\033[0;105m"
export Fondo_Cian_Brillante="\033[0;106m"
export Fondo_Blanco_Brillante="\033[0;107m"

export Reset="\033[0m"
export Negrita="\033[1m"
export Atenuado="\033[2m"
export Italico="\033[3m"
export Subrayado="\033[4m"
export Parpadeo="\033[5m"
export Invertido="\033[7m"
export Oculto="\033[8m"
export Tachado="\033[9m"

# ┌────────────────────────────────┐
# │ Clear and start                │
# └────────────────────────────────┘

clear
history -c && rm -f ~/.bash_history
cd

# ┌────────────────────────────────┐
# │ Definition of PS1 (input)      │
# └────────────────────────────────┘

os=$(grep '^NAME=' /etc/os-release | cut -d'"' -f2)
whoami=$(whoami)
input=$(hostname 2>/dev/null || {
    echo -ne "\033[1;32mUsuario: \033[0m"
    read -r input
    echo "$input" > "$HOME/Stellar/linux/lang_es/config/system/user.txt"
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

    PS1="${Cian_Brillante}[${whoami}] ${colors[user]}${input}${colors[reset]}@${colors[host]}${os}${colors[reset]}:${colors[path]}${current_dir}${git_info}${colors[reset]}"
    PS1+="\n${colors[symbol]}└─╼${colors[reset]} "

    echo -ne "\033]0;${input}@termux: ${current_dir}\007"
}

cd "$HOME"

clear

# ┌────────────────────────────────┐
# │ Security                       │
# └────────────────────────────────┘

tor-enable() {
pkill -f "tor"
pkill -f "9052"
pkill -f "9053"
export torport="9052"
export dnsport="9053"
export ALL_PROXY="socks5h://localhost:${torport}"
tor --SocksPort $torport \
    --CircuitBuildTimeout 30 \
    --NumEntryGuards 2 \
    --NewCircuitPeriod 60 \
    --MaxCircuitDirtiness 600 \
    --ClientOnly 1 \
    --AvoidDiskWrites 1 \
    --DNSPort $dnsport &>tor.txt &
sleep 5
printf "${Verde_Brillante}[INFO] ${Verde_Brillante}Tor ha sido activado"
}

tor-disable() {
unset torport
unset dnsport
unset ALL_PROXY
pkill -f "tor"
pkill -f "9052"
pkill -f "9053"
printf "${Rojo_Brillante}[INFO] ${Verde_Brillante}Tor ha sido desactivado"
}


# ┌────────────────────────────────┐
# │ Imports and banner             │
# └────────────────────────────────┘

command cp ~/Stellar/linux/lang_es/config/.bash_profile ~/.
cd ~/Stellar/linux/lang_es/config/themes
clear
data=$(grep -o "y" ~/Stellar/linux/lang_es/config/themes/isbanner.txt)
if [[ "$data" == "y" ]]; then
    python banner.py
fi
cd
printf "${Gris}[INFO] ${Blanco_Brillante}Stellar se ha iniciado correctamente.\n"
printf "${Gris}[INFO] ${Blanco_Brillante}Escriba ${Fondo_Azul}${Blanco_Brillante}menu${Reset} para ver los comandos disponibles.\n"


# ┌────────────────────────────────┐
# │ Definition of commands         │
# └────────────────────────────────┘

# Sistema

menu() {
    cd ~/Stellar/linux/lang_es/config
    python menu.py
    cd
}

reload() {
    cd ~/Stellar/linux/lang_es/config/themes
    clear
    data=$(grep -o "y" ~/Stellar/linux/lang_es/config/themes/isbanner.txt)
    if [[ "$data" == "y" ]]; then
        python banner.py
    fi
    cd
}

user-config() {
    cd ~/Stellar/linux/lang_es/config
    python user_config.py
    cd
}

uninstall() {
    cd ~/Stellar
    bash uninstall.sh
    cd
}

update() {
    cd ~/Stellar/linux/lang_es
    bash update.sh
    cd
}

reinstall() {
    cd ~/Stellar
    bash reinstall.sh
    cd
}

my() {
    cd ~/Stellar/linux/lang_es/config/system
    python user.py
    cd
}

banner-enable() {
    echo "y" > ~/Stellar/linux/lang_es/config/themes/isbanner.txt
    printf "${Verde_Brillante}[INFO] ${Reset}El banner ha sido habilitado"
    printf ""
    printf "\n"
}

banner-disable() {
    echo "n" > ~/Stellar/linux/lang_es/config/themes/isbanner.txt
    printf "${Rojo_Brillante}[INFO] ${Reset}El banner ha sido deshabilitado"
    printf ""
    printf "\n"
}

# Discord

weebhook-mass-spam() {
    cd ~/Stellar/linux/lang_es/commands/general/discord/weebhookraid
    python weebhook_mass_spam.py
    cd
}

mass-delete-channels() {
    cd ~/Stellar/linux/lang_es/commands/general/discord/botraid
    python mass_delete_channels.py
    cd
}

# Osint

ipinfo() {
    cd ~/Stellar/linux/lang_es/commands/osint/main
    python ipinfo.py
    cd
}

phoneinfo() {
    cd ~/Stellar/linux/lang_es/commands/osint/main
    python phoneinfo.py
    cd
}

urlinfo() {
    cd ~/Stellar/linux/lang_es/commands/osint/main
    python urlinfo.py
    cd
}

metadatainfo() {
    cd ~/Stellar/linux/lang_es/commands/osint/main
    bash metadatainfo.sh
    cd
}

emailsearch() {
    cd ~/Stellar/linux/lang_es/commands/osint/main
    python emailfinder.py
    cd
}

userfinder() {
    cd ~/Stellar/linux/lang_es/commands/osint/main
    python userfinder.py
    cd
}

instagraminfo() {
    cd ~/Stellar/linux/lang_es/commands/osint/instagram
    python profileinfo.py
    cd
}


# Osint/Discord

userinfo() {
    cd ~/Stellar/linux/lang_es/commands/osint/discord
    python userinfo.py
    cd
}

serverinfo() {
    cd ~/Stellar/linux/lang_es/commands/osint/discord
    python serverinfo.py
    cd
}

searchinvites() {
    cd ~/Stellar/linux/lang_es/commands/osint/discord
    python searchserverinvites.py
    cd
}

inviteinfo() {
    cd ~/Stellar/linux/lang_es/commands/osint/discord
    python inviteinfo.py
    cd
}

role-mapper() {
    cd ~/Stellar/linux/lang_es/commands/osint/discord
    python role_mapper.py
    cd
}

mutual-servers() {
    cd ~/Stellar/linux/lang_es/commands/osint/discord
    python mutual_servers.py
    cd
}

# Misc

ia() {
    cd ~/Stellar/linux/lang_es/commands/misc/tools/ia
    python iahttp.py
    cd
}

ia-image() {
    cd ~/Stellar/linux/lang_es/commands/misc/tools/ia
    python ia_image.py
    cd
}

ia-config-apikey() {
    cd ~/Stellar/linux/lang_es/commands/misc/tools/ia
    bash config-api_key.sh
    cd
}

traductor() {
    cd ~/Stellar/linux/lang_es/commands/misc/tools
    python traductor.py
    cd
}

myip() {
    cd ~/Stellar/linux/lang_es/commands/misc/tools
    python myip.py
    cd
}

passwordgen() {
    cd ~/Stellar/linux/lang_es/commands/misc/tools
    python passwordgen.py
    cd
}

encrypt-file() {
    cd ~/Stellar/linux/lang_es/commands/misc/tools
    python encrypt-file.py
    cd
}

ddos() {
    cd ~/Stellar/linux/lang_es/commands/misc/tools
    node ddos.js
    cd
}

# ┌────────────────────────────────┐
# │ Plugins system                │
# └────────────────────────────────┘

PLUGINS_DIR="$HOME/Stellar/plugins"
if [ -d "$PLUGINS_DIR" ]; then
    plugin_count=0
    for plugin_script in "$PLUGINS_DIR"/*; do
        if [ -f "$plugin_script" ]; then
            plugin_name=$(basename "$plugin_script")
            command_name="${plugin_name%.*}"
            eval "_stellar_plugin_$command_name() { \"$plugin_script\" \"\$@\"; }"
            alias "$command_name"="_stellar_plugin_$command_name"
            ((plugin_count++))
        fi
    done
    
    if [ $plugin_count -gt 0 ]; then
        printf "${Gris}[INFO]${Reset} Plugins cargados: ${Cian}%d${Reset}\n" "$plugin_count"
    fi
    
    original_command_not_found_handle=$(declare -f command_not_found_handle)
    eval "${original_command_not_found_handle/command_not_found_handle/original_command_not_found}"
    
    command_not_found_handle() {
        local cmd="$1"
        local plugin_path="$PLUGINS_DIR/$cmd".*
        
        for file in $plugin_path; do
            if [ -f "$file" ]; then
                echo -e "${Gris}[INFO]${Reset} El comando '${Blanco}$cmd${Reset}' existe como plugin (${Verde}$(basename "$file")${Reset}). ¿Quieres ejecutarlo? (s/n): "
                read -n 1 -r
                echo
                if [[ $REPLY =~ ^[Ss]$ ]]; then
                    "$file" "${@:2}"
                    return $?
                else
                    return 127
                fi
            fi
        done
        
        original_command_not_found "$@"
    }
fi

# ┌────────────────────────────────┐
# │ Other configs                 │
# └────────────────────────────────┘

alias ls='lsd --icon-theme unicode'

command_not_found_handle() {
    echo -e "${Gris}[INFO] ${Blanco_Brillante}Comando no encontrado: $1"
    return 127
}

fi

export STELLAR_PROTECT="$HOME/Stellar"

rm() {
  local p
  for p in "$@"; do
    [[ "$(realpath "$p" 2>/dev/null)" == "$STELLAR_PROTECT"* ]] && \
      { printf "${Amarillo_Brillante}[WARNING]${Blanco_Brillante} Protegido: $p\n"; return 1; }
  done
  command rm -I --preserve-root "$@"
}

mv() {
  local p
  for p in "$@"; do
    [[ "$(realpath "$p" 2>/dev/null)" == "$STELLAR_PROTECT"* ]] && \
      { printf "${Amarillo_Brillante}[WARNING]${Blanco_Brillante} Protegido: $p\n"; return 1; }
  done
  command mv -i "$@"
}

cp() {
  local p
  for p in "$@"; do
    [[ "$(realpath "$p" 2>/dev/null)" == "$STELLAR_PROTECT"* ]] && \
      { printf "${Amarillo_Brillante}[WARNING]${Blanco_Brillante} Protegido: $p\n"; return 1; }
  done
  command cp -i "$@"
}