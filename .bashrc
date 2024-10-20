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
  PS1="""${gris}
 _____________________________________
▕⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺▏
▕_[${rojo}~ ${amarillo}/${pwd_relative}${gris}]${verde} $ """
}

# Iniciar sistema

cd

clear

python Stellar/tor_init.py

clear

python Stellar/banner.py

cd

# Comandos y scripts

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
  python metadatainfo.py
  cd
}

# Base de datos

ipinfohistory() {
  cd
  cd Stellar/database
  ips_info_db_consult.py
  cd
}

phoneinfohistory() {
  cd
  cd Stellar/database
  phone_info_db_consult.py
  cd
}

# Menu y reload

menu() {
  cd
  cd Stellar
  python menu.py
  cd
}

reload() {
  cd
  clear
  cd Stellar
  python banner.py
  cd
}

# Utilidades

neko() {
  cd
  cd Stellar/misc/anime
  python neko.py
  cd
}
