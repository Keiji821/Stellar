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

success_color="${Verde_Brillante}"
warning_color="${Amarillo_Brillante}"
error_color="${Rojo_Brillante}"
prompt_color="${Magenta_Brillante}"
progress_color="${Azul_Brillante}"

banner="
 ____  _       _ _
/ ___|| |_ ___| | | __ _ _ __
\___ \| __/ _ \ | |/ _` | '__|
 ___) | ||  __/ | | (_| | |
|____/ \__\___|_|_|\__,_|_|"

# Inicio/Start - Stellar

read -p "Elija su idioma/Choose your language (Español/English): " language

if [ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" ]; then
    printf "${Subrayado}${Verde_Brillante}Stellar ha empezado a instalarse en su Termux/Terminal ${Reset}"

if

if [ "$language" == "English" || "$language" == "english" ]; then
    printf "${Subrayado}${Verde_Brillante}Stellar ha empezado a instalarse en su Termux/Terminal ${Reset}"

if

# Dependencias/Dependencies - Stellar

apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs lsd)
pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord fake_useragent pycryptodome)

# Instalador/Installer - Stellar

apt install $apt_packages
pip install $pip_packages

sleep 5

cp ~/Stellar/lang_es/config/.bash_profile ~/.
cp ~/Stellar/lang_es/config/.bashrc ~/.


# Final/End - Stellar



