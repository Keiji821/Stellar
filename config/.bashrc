# Definir colores

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

# Personalizar input

input=$(cat Stellar/config/themes/input.txt)

function cd() {
  builtin cd "$@"
  local pwd_relative="${PWD/#$HOME}"
  pwd_relative=${pwd_relative#/}
  PS1="${gris}╭────────${azul_agua}(${rojo}${pwd_relative}${azul_agua})${gris}
${gris}╰──${azul_agua}[${verde}${input}${azul_agua}]${gris}── ${amarillo}~ ${verde} $ ${blanco2}"
}

# Iniciar configuración

clear
export ALL_PROXY=socks5h://localhost:9050
pkill cloudflared &
cloudflared --url Stellar &>/dev/null &
python Stellar/config/run.py

# Mostrar banner al final

cd
cd Stellar/config/themes
clear
python banner.py
cd

# Osint

ipinfo() {
  cd
  cd Stellar/osint
  python ipinfo.py
  cd
}

phoneinfo() {
  cd
  cd Stellar/osint
  python phoneinfo.py
  cd
}

urlinfo() {
  cd
  cd Stellar/osint
  python urlinfo.py
  cd
}

metadatainfo() {
  cd
  cd Stellar/osint
  bash metadatainfo.sh
  cd
}

emailsearch() {
 cd
 cd Stellar/osint
 python emailfinder.py
 cd
}

userfinder() {
 cd
 cd Stellar/osint
 python userfinder.py
 cd
}

# Pentesting

ddos() {
  cd
  cd Stellar/pentesting
  python ddos.py
 cd
}

# Sistema

menu() {
  cd
  cd Stellar/config
  python menu.py
  cd
}

reload() {
  cd
  cd Stellar/config/themes
  git pull --force
  clear
  python banner.py
  cd
}

ui() {
 cd
 cd Stellar/config/themes
 bash ui_config.sh
 cd
}

# Utilidades - herramientas

ia() {
 cd
 cd Stellar/misc/utilidades
 python iahttp.py
 cd
}

traductor() {
 cd
 cd Stellar/misc/utilidades
 python traductor.py
 cd
}

myip() {
 cd
 cd Stellar/misc/utilidades
 python myip.py
 cd
}
