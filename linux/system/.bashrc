#!/bin/bash

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
# │ Translate                      │
# └────────────────────────────────┘

translate() {
    local value=$1
    local lang=$(cat ~/Stellar/configs/selected_lang.txt)
    awk -F': ' -v clave="$value" '$1==clave {print $2}' ~/Stellar/langs/"$lang".yml
}

init_message=$(translate init_message)
init2_message=$(translate init2_message)
activate_tor_message=$(translate activate_tor_message)
deactivate_tor_message=$(translate deactivate_tor_message)
banner_active_message=$(translate banner_active_message)
banner_deactivate_message=$(translate banner_deactivate_message)
protect_message=$(translate protect_message)
load_plugins_message=$(translate load_plugins_message)
load2_plugins_message=$(translate load2_plugins_message)
command_not_found_message=$(translate command_not_found_message)

eval "init_message=\"$init_message\""
eval "init2_message=\"$init2_message\""
eval "activate_tor_message=\"$activate_tor_message\""
eval "deactivate_tor_message=\"$deactivate_tor_message\""
eval "banner_active_message=\"$banner_active_message\""
eval "banner_deactivate_message=\"$banner_deactivate_message\""
eval "protect_message=\"$protect_message\""
eval "load_plugins_message=\"$load_plugins_message\""
eval "load2_plugins_message=\"$load2_plugins_message\""
eval "command_not_found_message=\"$command_not_found_message\""

# ┌────────────────────────────────┐
# │ Definition of PS1 (input)      │
# └────────────────────────────────┘

input=$(grep -v '^[[:space:]]*$' "$HOME/Stellar/configs/user.stel" 2>/dev/null || {
    echo -ne "\033[1;32mUsuario: \033[0m"
    read -r input
    echo "$input" > "$HOME/Stellar/configs/user.stel"
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
    printf "${Verde_Brillante}[INFO] ${Verde_Brillante}$activate_tor_message\n"
}

tor-disable() {
    unset torport
    unset dnsport
    unset ALL_PROXY
    pkill -f "tor"
    pkill -f "9052"
    pkill -f "9053"
    printf "${Rojo_Brillante}[INFO] ${Verde_Brillante}$deactivate_tor_message\n"
}

# ┌────────────────────────────────┐
# │ Imports and banner             │
# └────────────────────────────────┘

command cp ~/Stellar/termux/system/.bash_profile ~/.
cd ~/Stellar/termux/system
clear
data=$(grep -o "y" ~/Stellar/configs/isbanner.stel)
if [[ "$data" == "y" ]]; then
    python banner.py
fi
cd
printf "${Gris}[INFO] ${Blanco_Brillante}$init_message\n"
printf "${Gris}[INFO] ${Blanco_Brillante}$init2_message\n"

# ┌────────────────────────────────┐
# │ Definition of commands         │
# └────────────────────────────────┘

# Sistema

manager() {
    cd ~/Stellar
    bash init.sh
    cd
}

menu() {
    cd ~/Stellar/termux/system
    python menu.py
    cd
}

reload() {
    cd ~/Stellar/termux/system
    clear
    python banner.py
    cd
}

user-config() {
    cd ~/Stellar/termux/system
    python user_config.py
    cd
}

my() {
    cd ~/Stellar/termux/system
    python user.py
    cd
}

banner-enable() {
    echo "y" > ~/Stellar/configs/isbanner.stel
    printf "${Verde_Brillante}[INFO] ${Reset}$banner_active_message"
    printf ""
    printf "\n"
}

banner-disable() {
    echo "n" > ~/Stellar/configs/isbanner.stel
    printf "${Rojo_Brillante}[INFO] ${Reset}$banner_active_message"
    printf ""
    printf "\n"
}

# Osint

ipinfo() {
    cd ~/Stellar/termux/commands/osint/main
    python ipinfo.py
    cd
}

phoneinfo() {
    cd ~/Stellar/termux/commands/osint/main
    python phoneinfo.py
    cd
}

urlinfo() {
    cd ~/Stellar/termux/commands/osint/main
    python urlinfo.py
    cd
}

metadatainfo() {
    cd ~/Stellar/termux/commands/osint/main
    bash metadatainfo.sh
    cd
}

# ┌────────────────────────────────┐
# │ Plugins system                 │
# └────────────────────────────────┘

chmod +x ~/Stellar/plugins/*.sh ~/Stellar/plugins/*.py ~/Stellar/plugins/*.js 2>/dev/null
PLUGINS_DIR="$HOME/Stellar/plugins"
if [ -d "$PLUGINS_DIR" ]; then
    plugin_count=0
    for plugin_script in "$PLUGINS_DIR"/*.sh "$PLUGINS_DIR"/*.py "$PLUGINS_DIR"/*.js; do
        if [ -f "$plugin_script" ]; then
            plugin_name=$(basename "$plugin_script")
            command_name="${plugin_name%.*}"
            if [[ "$plugin_script" == *.js ]]; then
                eval "_stellar_plugin_$command_name() { node \"$plugin_script\" \"\$@\"; }"
            else
                eval "_stellar_plugin_$command_name() { \"$plugin_script\" \"\$@\"; }"
            fi
            alias "$command_name"="_stellar_plugin_$command_name"
            ((plugin_count++))
        fi
    done

    if [ $plugin_count -gt 0 ]; then
        printf "${Gris}[INFO]${Reset} $load_plugins_message: ${Cian}%d${Reset}\n" "$plugin_count"
    fi

    original_command_not_found_handle=$(declare -f command_not_found_handle)
    eval "${original_command_not_found_handle/command_not_found_handle/original_command_not_found}"

    command_not_found_handle() {
        local cmd="$1"
        local plugin_path="$PLUGINS_DIR/$cmd".*

        for file in $plugin_path; do
            if [ -f "$file" ]; then
                echo -e "${Gris}[INFO]${Reset} $load2_plugins_message (${Verde}$(basename "$file")${Reset}). ¿Quieres ejecutarlo? (s/n): "
                read -n 1 -r
                echo
                if [[ $REPLY =~ ^[Ss]$ ]]; then
                    if [[ "$file" == *.js ]]; then
                        node "$file" "${@:2}"
                    else
                        "$file" "${@:2}"
                    fi
                    return $?
                else
                    return 127
                fi
            fi
        done

        original_command_not_found "$@"
    }
fi

# ┌──────────────────────────────────────┐
# │ Termux Properties and Modifications  │
# └──────────────────────────────────────┘

cd ~/.termux
cat > termux.properties << 'EOF'
# allow-external-apps = true
# default-working-directory = /data/data/com.termux/files/home
# disable-terminal-session-change-toast = true
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
shortcut.create-session = ctrl + t
shortcut.next-session = ctrl + 2
shortcut.previous-session = ctrl + 1
shortcut.rename-session = ctrl + n

bell-character = vibrate
# back-key=escape

# enforce-char-based-input = true
# ctrl-space-workaround = true

# terminal-margin-horizontal=3
# terminal-margin-vertical=0
EOF
cd

alias ls='lsd --icon-theme unicode'
x11() {
    termux-x11 :0 &
    export DISPLAY=:0
}

command_not_found_handle() {
    echo -e "${Gris}[INFO] ${Blanco_Brillante}$command_not_found_message: $1"
    return 127
}

export STELLAR_PROTECT="$HOME/Stellar"

rm() {
  local p
  for p in "$@"; do
    [[ "$(realpath "$p" 2>/dev/null)" == "$STELLAR_PROTECT"* ]] && \
      { printf "${Rojo_Brillante}[WARNING]${Blanco_Brillante} $protect_message: $p\n"; return 1; }
  done
  command rm -I --preserve-root "$@"
}

mv() {
  local p
  for p in "$@"; do
    [[ "$(realpath "$p" 2>/dev/null)" == "$STELLAR_PROTECT"* ]] && \
      { printf "${Rojo_Brillante}[WARNING]${Blanco_Brillante} $protect_message: $p\n"; return 1; }
  done
  command mv -i "$@"
}

cp() {
  local p
  for p in "$@"; do
    [[ "$(realpath "$p" 2>/dev/null)" == "$STELLAR_PROTECT"* ]] && \
      { printf "${Rojo_Brillante}[WARNING]${Blanco_Brillante} $protect_message: $p\n"; return 1; }
  done
  command cp -i "$@"
}