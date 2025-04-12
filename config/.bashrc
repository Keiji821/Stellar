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

clear
cd

echo -ne '\033]0;~ Stellar\007'

function pwlogin_loop() {
    local max_intentos=3
    local intentos=0
    local user=""
    local shell_pid=$$

    if ! command -v pwlogin &>/dev/null; then
        echo -e "${rojo}[ERROR]${blanco} Comando 'pwlogin' no encontrado${reset}"
        return 1
    fi

    if [[ ! -f "$HOME/.termux_authinfo" ]]; then
        echo -e "${rojo}[ERROR]${blanco} No hay contraseña configurada${reset}"
        return 1
    fi

    echo -e "${azul}[INFO]${blanco} Autenticación requerida${reset}"

    if [[ -f "$HOME/.configs_stellar/themes/user.txt" ]]; then
        user=$(cat "$HOME/.configs_stellar/themes/user.txt")
        echo -e "${gris}[INFO]${blanco} Usuario actual: ${verde}$user${reset}"
    else
        echo -n -e "${gris}[INFO]${blanco} Ingrese su nombre de usuario: "
        read user
        mkdir -p "$HOME/.configs_stellar/themes"
        echo "$user" > "$HOME/.configs_stellar/themes/user.txt"
    fi

    while [[ $intentos -lt $max_intentos ]]; do
        echo -n -e "${gris}[INFO]${blanco} Ingrese su contraseña: "
        read -s password
        echo

        if [[ -z "$password" ]]; then
            intentos=$((intentos+1))
            echo -e "${amarillo}[WARNING]${blanco} Contraseña vacía (Intento $intentos/$max_intentos)${reset}\n"
            continue
        fi

        if echo "$password" | pwlogin 2>/dev/null; then
            echo -e "${verde}[SUCCESS]${blanco} Autenticación exitosa${reset}"
            return 0
        else
            intentos=$((intentos+1))
            echo -e "${rojo}[ERROR]${blanco} Contraseña incorrecta (Intento $intentos/$max_intentos)${reset}\n"
        fi
    done

    echo -e "${rojo}[ERROR]${blanco} Demasiados intentos fallidos. Cerrando sesión...${reset}"
    sleep 2
    kill -9 $shell_pid 2>/dev/null
    exit 1
}

pwlogin_loop

input=$(cat .configs_stellar/themes/user.txt)

function cd() {
builtin cd "$@"
local pwd_relative="${PWD/#$HOME}"
pwd_relative=${pwd_relative#/}
PS1="${azul_agua}(${morado}${pwd_relative}${azul_agua}) ${azul_agua}${verde}${input}${azul_agua} ${amarillo}~${verde} $ ${blanco2}"
}

clear
export ALL_PROXY=socks5h://localhost:9052
pkill tor
tor &>/dev/null &
bash Stellar/update.sh &>/dev/null &",
cd Stellar && git pull --force &>/dev/null &

cd
cd .configs_stellar/themes
cp ~/Stellar/config/.bash_profile ~/.
clear
python banner.py
cd
printf "${gris}[INFO] ${blanco}Stellar se ha iniciado correctamente.
"
printf "${gris}[INFO] ${blanco}Escriba (menu) para ver los comandos disponibles.
"

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
    echo -e "${gris}[INFO] ${blanco}Comando no encontrado: $1"
    return 127
}