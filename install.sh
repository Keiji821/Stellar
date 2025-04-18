gris="${b}\033[1;30m"
blanco="\033[0m"
blanco2="$b\033[1;37m"
rojo="${b}\033[1;31m"
rojo2="${b}\033[31m"
azul="${b}\033[1;34m"
azul2="${b}\033[34m"
azul_agua="${b}\e[1;36m"
azul_agua2="${b}\e[36m"
verde="${b}\033[1;32m"
verde2="${b}\033[32m"
morado="$b\033[1;35m"
morado2="$b\033[35m"
amarillo="$b\033[1;33m"
amarillo2="$b\033[33m"
cyan="$b\033[38;2;23;147;209m"

clear

cp ~/Stellar/config/.bash_profile ~/.
cp ~/Stellar/config/.bashrc ~/.

user_config() {
    if [ ! -d ~/system ]; then
        echo -e "${rojo}Error: Directorio system no encontrado${blanco}"
        return 1
    fi

    while true; do
        clear
        echo -e "${amarillo Configuración de usuario ${blanco}"
        echo -e "${amarillo}-----------------------${blanco}"
        
        read -p "Nombre de usuario (4-15 caracteres): " usuario
        
        if [[ -z "$usuario" ]]; then
            echo -e "${rojo}El campo no puede estar vacio${blanco}"
            sleep 1
            continue
        fi
        
        if [[ "${#usuario}" -lt 4 || "${#usuario}" -gt 15 ]]; then
            echo -e "${rojo}Debe tener entre 4 y 15 caracteres${blanco}"
            sleep 1
            continue
        fi
        
        if [[ ! "$usuario" =~ ^[a-zA-Z0-9_]+$ ]]; then
            echo -e "${rojo}Solo se permiten letras, numeros y _${blanco}"
            sleep 1
            continue
        fi

        echo "$usuario" > ~/system/user.txt
        echo -e "${verde}Usuario configurado correctamente!${blanco}"
        sleep 2
        break
    done
}

user_config

cd

printf "${amarillo}[${verde}+${amarillo}]${blanco} Iniciando instalación\n"

apt-get update -y && apt-get upgrade -y &>/dev/null &

apt install python &>/dev/null &

apt install tor &>/dev/null &

apt install cloudflared &>/dev/null &

apt install exiftool &>/dev/null &

apt install nmap &>/dev/null &

apt install termux-api &>/dev/null &

apt install dnsutils &>/dev/null &

pip install beautifulsoup4 &>/dev/null &

pip install bs4 &>/dev/null &

pip install pyfiglet &>/dev/null &

pip install phonenumbers &>/dev/null &

pip install psutil &>/dev/null &

pip install PySocks &>/dev/null &

pip install requests &>/dev/null &

pip install rich &>/dev/null &

pip install "rich[jupyter]" &>/dev/null &

pip install lolcat &>/dev/null &

pip install discord &>/dev/null &