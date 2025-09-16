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
export Amarillo_Brillante="\033[1;33m"
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

clear

banner="""
███████╗████████╗███████╗██╗     ██╗      █████╗ ██████╗ 
██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗██╔══██╗
███████╗   ██║   █████╗  ██║     ██║     ███████║██████╔╝
╚════██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║██╔══██╗
███████║   ██║   ███████╗███████╗███████╗██║  ██║██║  ██║
╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

                                   @Instalador/Installer"""

printf "${Azul_Brillante} ${banner} ${Reset}"
printf "\n"
printf "\n${Magenta_Brillante}⭐ Created by: Keiji821 ${Reset}"
printf "\n${Cian_Brillante}🔵 My Discord contact: ${Verde_Brillante}keiji100 ${Reset}"
printf "\n${Magenta_Brillante}📦 Repository ${Rojo_Brillante} >>> ${Cian_Brillante}${Subrayado}https://github.com/Keiji821/Stellar${Reset}\n"
printf "\n"
printf "\n${Rojo_Brillante}[!]${Blanco_Brillante} Note: The program is currently in Spanish,\nwith full English support coming soon. ${Reset}"
printf "\n"

# Inicio/Start - Stellar


printf "${Amarillo_Brillante}"
read -p "• Elija su idioma/Choose your language (Español/English): " language

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" || "$language" == "es" ]]; then
    printf "\n${Verde_Brillante}[+]${Verde_Brillante}${Blanco_Brillante} Stellar ha empezado a instalarse en su Termux/Terminal ${Reset}"
fi

sleep 3

if [[ "$language" == "English" || "$language" == "english" || "$language" == "en" ]]; then
    printf "\n${Verde_Brillante}[+]${Verde_Brillante}${Blanco_Brillante} Stellar has started installing on your Termux/Terminal ${Reset}"
fi

sleep 3

printf "\n"

# Dependencias/Dependencies - Stellar

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" || "$language" == "es" ]]; then
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Instalando dependencias necesarias para el correcto funcionamiento de Stellar ${Reset}"
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Esperé un momento... ${Reset}"
fi

sleep 3

if [[ "$language" == "English" || "$language" == "english" || "$language" == "en" ]]; then
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Installing dependencies required for Stellar to run properly ${Reset}"
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Please wait... ${Reset}"
fi

sleep 3

apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs lsd root-repo)
pip_packages=(
    beautifulsoup4
    pyfiglet
    phonenumbers
    psutil
    PySocks
    requests
    rich
    "rich[jupyter]"
    lolcat
    discord
    fake_useragent
    pycryptodome
)


# Instalador/Installer - Stellar

printf "\n"

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" || "$language" == "es" ]]; then
    printf "\n${Verde_Brillante}[+]${Amarillo_Brillante}${Blanco_Brillante} Empezando instalación... ${Reset}"
    sleep 5
   
    apt install "${apt_packages[@]}" -y
    if [[ $? -ne 0 ]]; then
        printf "\n${Verde_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Falló la instalación de algunos paquetes APT. Revisa los errores anteriores. ${Reset}\n"
        exit 1
    fi

    printf "\n"

    pip3 install "${pip_packages[@]}"
    if [[ $? -ne 0 ]]; then
        printf "\n${Verde_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Falló la instalación de algunos paquetes PIP. Revisa los errores anteriores. ${Reset}\n"
        exit 1
    fi
fi

if [[ "$language" == "English" || "$language" == "english" || "$language" == "en" ]]; then
    printf "\n${Verde_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Starting installation... ${Reset}"
    sleep 5

    apt install "${apt_packages[@]}" -y
    if [[ $? -ne 0 ]]; then
        printf "\n${Verde_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Some APT packages failed to install. Please review the previous errors. ${Reset}\n"
        exit 1
    fi

    printf "\n"

    pip3 install "${pip_packages[@]}"
    if [[ $? -ne 0 ]]; then
        printf "\n${Verde_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Some PIP packages failed to install. Please review the previous errors. ${Reset}\n"
        exit 1
    fi
fi

printf "\n"

sleep 3

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" || "$language" == "es" ]]; then
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Finalizando instalación... ${Reset}"
    command cp ~/Stellar/lang_es/config/.bash_profile ~/.
    command cp ~/Stellar/lang_es/config/.bashrc ~/.
    command cp ~/Stellar/fonts/fira-mono/font.ttf ~/termux
    command cp ~/Stellar/fonts/fira-mono/font.ttf ~/termux
    cat > ~/.termux/color.properties << 'EOF'
    background=#0f111a
    foreground=#a6accd
    color0=#0f111a
    color1=#ff5370
    color2=#c3e88d
    color3=#ffcb6b
    color4=#82aaff
    color5=#c792ea
    color6=#89ddff
    color7=#a6accd
    color8=#3a3c4e
    color9=#ff5370
    color10=#c3e88d
    color11=#ffcb6b
    color12=#82aaff
    color13=#c792ea
    color14=#89ddff
    color15=#d0d0d0
    EOF
fi

if [[ "$language" == "English" || "$language" == "english" || "$language" == "en" ]]; then
    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante}${Blanco_Brillante} Finishing installation... ${Reset}"
    command cp ~/Stellar/lang_es/config/.bash_profile ~/.
    command cp ~/Stellar/lang_es/config/.bashrc ~/.
    command cp ~/Stellar/fonts/fira-mono/font.ttf ~/termux
    cat > ~/.termux/color.properties << 'EOF'
    background=#0f111a
    foreground=#a6accd
    color0=#0f111a
    color1=#ff5370
    color2=#c3e88d
    color3=#ffcb6b
    color4=#82aaff
    color5=#c792ea
    color6=#89ddff
    color7=#a6accd
    color8=#3a3c4e
    color9=#ff5370
    color10=#c3e88d
    color11=#ffcb6b
    color12=#82aaff
    color13=#c792ea
    color14=#89ddff
    color15=#d0d0d0
    EOF
fi

sleep 5

# Final/End - Stellar

printf "\n"

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" || "$language" == "es" ]]; then
    printf "\n${Verde_Brillante}✓${Blanco_Brillante} ¡Stellar se ha instalado correctamente!${Reset}"
    printf "\n${Rojo_Brillante}${Rojo_Brillante}[!]${Blanco_Brillante} Nota: Es recomendable que cierres Termux y lo vuelvas a abrir para que todo e incluyendo ${Rojo_Brillante}TOR${Blanco_Brillante} funcione correctamente ${Reset}"

    Salir=""

    while [[ "$Salir" != "Salir" ]]; do
           
        printf "\n${Verde_Brillante}¿Desea salir del programa?\n" 
        read -p "Escriba (Salir) para continuar: " Salir
    
        case "$Salir" in
            Salir)
                 printf "\n${Amarillo_Brillante}${Rojo_Brillante}[!]${Blanco_Brillante} Iniciando sesión en Stellar...${Reset}"
        esac
done


   sleep 5
   login
fi


if [[ "$language" == "English" || "$language" == "english" || "$language" == "en" ]]; then
    printf "\n${Verde_Brillante}✓${Blanco_Brillante} Stellar has been installed successfully!${Reset}"    
    printf "\n${Rojo_Brillante}${Rojo_Brillante}[!]${Blanco_Brillante} Nota: It is recommended that you close Termux and reopen it so that everything including ${Rojo_Brillante}TOR${Blanco_Brillante} work properly ${Reset}"

    Exit=""

    while [[ "$Exit" != "Exit" ]]; do
    
        printf "\n${Verde_Brillante}Do you want to exit the program?\n" 
        read -p "Type (Exit) to continue: " Exit
    
        case "$Exit" in
            Exit)
                 printf "\n${Amarillo_Brillante}${Rojo_Brillante}[!]${Blanco_Brillante} Logging in to Stellar...${Reset}"
        esac
done    


   sleep 5
   login
fi