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

input=$(cat .configs_stellar/themes/input.txt)

function cd() {
builtin cd "$@"
local pwd_relative="${PWD/#$HOME}"
pwd_relative=${pwd_relative#/}
PS1="${azul_agua}(${morado}${pwd_relative}${azul_agua}) ${azul_agua}${verde}${input}${azul_agua} ${amarillo}~${verde} $ ${blanco2}"
}

clear
export ALL_PROXY=socks5h://localhost:9050
python Stellar/config/run.py

cd
cd .configs_stellar/themes
cp ~/Stellar/config/.bash_profile ~/. &>/dev/null &
clear
python banner.py
cd

# Osint - main

ipinfo() {
cd
cd Stellar/osint/main
python ipinfo.py
cd
}

phoneinfo() {
cd
cd Stellar/osint/main
python phoneinfo.py
cd
}

urlinfo() {
cd
cd Stellar/osint/main
python urlinfo.py
cd
}

metadatainfo() {
cd
cd Stellar/osint/main
bash metadatainfo.sh
cd
}

emailsearch() {
cd
cd Stellar/osint/main
python emailfinder.py
cd
}

userfinder() {
cd
cd Stellar/osint/main
python userfinder.py
cd
}

# Osint - Discod

userinfo() {
cd
cd Stellar/osint/discord
python userinfo.py
cd
}

# Pentesting

ddos() {
cd
cd Stellar/pentesting
python ddos.py
cd
}

# System

menu() {
cd
cd Stellar/config
python menu.py
cd
}

reload() {
cd
cd .configs_stellar/themes
clear
python banner.py
cd
}

ui() {
cd
cd Stellar/config
python ui_config.py
cd
}

# Misc

ia() {
cd
cd Stellar/misc/tools
python iahttp.py
cd
}

ia-image() {
cd
cd Stellar/misc/tools
python ia_image.py
cd
}

traductor() {
cd
cd Stellar/misc/tools
python traductor.py
cd
}

myip() {
cd
cd Stellar/misc/tools
python myip.py
cd
}

# Config

command_not_found_handle() {
    echo -e "${gris}[INFO] ${rojo}Comando no encontrado:${rojo} ${blanco}$1${blanco}"
    return 127
}

trap 'printf "${gris}[INFO] ${verde}Ejecutando comando: ${blanco}$1
"' DEBUG