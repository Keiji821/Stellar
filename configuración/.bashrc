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

function cd() {
  builtin cd "$@"
  local pwd_relative="${PWD/#$HOME}"
  pwd_relative=${pwd_relative#/}
  PS1="""${gris}[${rojo}~ ${amarillo}/${pwd_relative}${gris}]${verde} $ ${blanco2}"""
}

# Iniciar tor y cloudflared 

clear
pkill tor &>/dev/null &
pkill cloudflared &>/dev/null &
sleep 5
export ALL_PROXY=socks5h://localhost:9050
tor &>/dev/null &
sleep 5
cloudflared --url Stellar &>/dev/null &
sleep 5

# Actualizar automáticamente el directorio Stellar con el de github

cd
cd Stellar
bash update.sh &>/dev/null &
git pull --force
cp ~/Stellar/configuración/.bash_profile ~/.

# Mostrar banner al final

cd
cd Stellar/configuración 
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

# Pentesting

ddos() {
  cd
  cd Stellar/pentesting
  python ddos.py
 cd
}

# Menu y reload

menu() {
  cd
  cd Stellar/configuración
  python menu.py
  cd
}

reload() {
  cd
  cd Stellar
  git pull --force
  clear
  python banner.py
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
