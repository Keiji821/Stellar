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
printf "${amarillo}[${verde}+${amarillo}] ${blanco2} Iniciando Tor y Cloudflared"
echo
pkill tor &>>/dev/null 
echo
pkill cloudflared &>>/dev/null 
sleep 5
echo
export ALL_PROXY=socks5h://localhost:9050
echo
tor &>>/dev/null
sleep 5
echo
cloudflared --url Stellar &>>/dev/null
sleep 5
echo
printf "${amarillo}[${verde}✔${amarillo}] ${blanco2} Tor y Cloudflared iniciados correctamente"

# Actualizar automáticamente el directorio Stellar con el de github

echo
printf "${amarillo}[${verde}+${amarillo}] ${blanco2} Vericando actualizaciones..."
echo
cd Stellar
echo
printf "${amarillo}[${verde}+${amarillo}] ${blanco2} Verificando actualizaciones..."
echo
bash update.sh &>>/dev/null
echo
printf "${amarillo}[${verde}✔${amarillo}] ${blanco2} Actualizaciones verificadas correctamente"
echo
git pull --force
cp ~/Stellar/.bash_profile ~/.
cd
echo
printf "${amarillo}[${verde}✔${amarillo}] ${blanco2} Actualizaciones verificadas correctamente"
sleep 1
echo
printf "${amarillo}[${verde}✔${amarillo}] ${blanco2} Operación completada"
echo

# Mostrar banner al final

cd
cd Stellar
clear
python banner.py
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
  bash metadatainfo.sh
  cd
}

ddos() {
  cd
  cd Stellar/pentesting
  python ddos.py
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
  source .bashrc
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
