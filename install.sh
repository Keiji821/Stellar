1Gris="\033[1;30m"
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

clear

banner="""
#####
#     # ##### ###### #      #        ##   #####
#         #   #      #      #       #  #  #    #
 #####    #   #####  #      #      #    # #    #  
      #   #   #      #      #      ###### #####
#     #   #   #      #      #      #    # #   #
 #####    #   ###### ###### ###### #    # #    # 

                                   @Instalador/Installer"""

printf "${Azul_Brillante} ${banner} ${Reset}"
printf "\n"
printf "\n${Magenta_Brillante}⭐ Created by: Keiji821 ${Reset}"
printf "\n${Cian_Brillante}🔵 My Discord contact: ${Verde_Brillante}keiji100 ${Reset}"
printf "\n${Magenta_Brillante}📦 Repository ${Rojo_Brillante} >>> ${Cian_Brillante}${Subrayado}https://github.com/Keiji821/Stellar${Reset}\n"
printf "\n"

# Inicio/Start - Stellar


printf "${Amarillo_Brillante}"
read -p "• Elija su idioma/Choose your language (Español/English): " language

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" ]]; then
    printf "\n${Verde_Brillante}[+]${Verde_Brillante}${Blanco_Brillante} Stellar ha empezado a instalarse en su Termux/Terminal ${Reset}"
fi

if [[ "$language" == "English" || "$language" == "english" ]]; then
    printf "\n${Verde_Brillante}[+]${Verde_Brillante}${Blanco_Brillante} Stellar has started installing on your Termux/Terminal ${Reset}"
fi

printf "\n"

# Dependencias/Dependencies - Stellar

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" ]]; then
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Instalando dependencias necesarias para el correcto funcionamiento de Stellar ${Reset}"
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante}Esperé un momento... ${Reset}"
fi

if [[ "$language" == "English" || "$language" == "english" ]]; then
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Installing dependencies required for Stellar to run properly ${Reset}"
    printf "\n{Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante}Please wait... ${Reset}"
fi


apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs lsd)
pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord fake_useragent pycryptodome)


# Instalador/Installer - Stellar

printf "\n"

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" ]]; then
    printf "\n${Verde_Brillante}[+]${Amarillo_Brillante}${Blanco_Brillante} Empezando instalación... ${Reset}"
fi

if [[ "$language" == "English" || "$language" == "english" ]]; then
    printf "\n${Verde_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Starting installation... ${Reset}"
fi

printf "\n"

printf "${Verde_Brillante}"
apt install $apt_packages -y 
pip install $pip_packages
sleep 3
printf "${Reset}"

printf "\n"

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" ]]; then
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Finalizando instalación... ${Reset}"
fi

if [[ "$language" == "English" || "$language" == "english" ]]; then
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Finishing installation... ${Reset}"
fi

sleep 5

cp ~/Stellar/lang_es/config/.bash_profile ~/.
cp ~/Stellar/lang_es/config/.bashrc ~/.


# Final/End - Stellar

printf "\n"

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" ]]; then
    printf "\n${Verde_Brillante}✓${Blanco_Brillante} ¡Stellar se ha instalado correctamente!${Reset}"
    printf "\n${Rojo_Brillante}${Rojo_Brillante}[!]${Blanco_Brillante} Nota: Es recomendable que cierres Termux y lo vuelvas a abrir para que todo e incluyendo ${Rojo_Brillante}TOR${Verde_Brillante} funcione correctamente ${Reset}"
    printf "\n${Amarillo_Brillante}${Rojo_Brillante}[!]${Blanco_Brillante} Iniciando sesión en Stellar...${Reset}"
   sleep 5
   login
fi


if [[ "$language" == "English" || "$language" == "english" ]]; then
    printf "\n${Verde_Brillante}✓${Blanco_Brillante} Stellar has been installed successfully!${Reset}"    
    printf "\n${Rojo_Brillante}${Rojo_Brillante}[!]${Blanco_Brillante} Nota: It is recommended that you close Termux and reopen it so that everything including ${Rojo_Brillante}TOR${Blanco_Brillante} work properly ${Reset}"
    printf "\n${Amarillo_Brillante}${Rojo_Brillante}[!]${Blanco_Brillante} Logging in to Stellar...${Reset}"
   sleep 5
   login
fi


