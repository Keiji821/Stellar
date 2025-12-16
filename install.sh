#!/bin/bash
cd
  
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

export system="Stellar"

clear

banner="""
███████╗████████╗███████╗██╗     ██╗      █████╗ ██████╗ 
██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗██╔══██╗
███████╗   ██║   █████╗  ██║     ██║     ███████║██████╔╝
╚════██║   ██║   ██╔══╝  ██║     ██║     ██╔══██╗██╔══██╗
███████║   ██║   ███████╗███████╗███████╗██║  ██║██║  ██║
╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

                                   @Instalador/Installer"""

printf "${Azul_Brillante}${banner}${Reset}"
printf "\n"
printf "\n${Magenta_Brillante}⭐ Created by: Keiji821 ${Reset}"
printf "\n${Cian_Brillante}🔵 My Discord contact: ${Verde_Brillante}keiji100 ${Reset}"
printf "\n${Magenta_Brillante}📦 Repository ${Rojo_Brillante} >>> ${Cian_Brillante}${Subrayado}https://github.com/Keiji821/Stellar${Reset}\n"
printf "\n"
printf "\n${Rojo_Brillante}[!]${Blanco_Brillante} Note: The program is currently in Spanish,\nwith full English support coming soon. ${Reset}"
printf "\n"

apt_packages=(python3 tor exiftool nmap dnsutils nodejs lsd)
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

spanish() {
    printf "${Verde_Brillante}"
    read -p "[${system}] ¿Desea comenzar con el proceso de instalación? (s/n): " next1

    if [[ "$next1" == "n" ]]; then
        printf "${Verde_Brillante}[${system}] ${Reset}¡Hasta luego!\n"
        exit 1
    fi

    if [[ "$next1" == "s" ]]; then
        printf "${Verde_Brillante}"
        read -p "[${system}] Escoja su plataforma (Termux/Linux): " plataform

        if [[ "$plataform" == "Termux" ]]; then
            printf "${Cian_Brillante}[${system}] ${Reset}¿Desea saltar proceso de instalación de dependencias?\nPueden haber efectos no deseados\n"
            read -p "» (s/n): " skip_install

            if [[ "$skip_install" == "s" ]]; then
                printf "${Cian_Brillante}[${system}] ${Reset}Instalando configuraciones basicas....\n"
                cd
                mkdir -p .termux
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
                command cp ~/Stellar/termux/lang_es/config/.bash_profile ~/. 2>/dev/null
                command cp ~/Stellar/termux/lang_es/config/.bashrc ~/. 2>/dev/null
                mkdir -p ~/.termux/fonts
                command cp ~/Stellar/fonts/fira-mono/font.ttf ~/.termux/fonts/ 2>/dev/null
                printf "${Cian_Brillante}[${system}] ${Reset}¡Listo!\nCerrando programa en 3 segundos\n"
                sleep 3
                exit 1
            fi

            if [[ "$skip_install" == "n" ]]; then
                printf "${Cian_Brillante}[${system}] ${Reset}Comenzando instalación....\n"
                pkg install termux-api -y
                pkg install root-repo -y
                pkg install "${apt_packages[@]}" -y
                if [[ $? -ne 0 ]]; then
                    printf "\n${Rojo_Brillante}[!][${system}]${Amarillo_Brillante} Falló la instalación de algunos paquetes APT. Revisa los errores anteriores. ${Reset}\n"
                    exit 1
                fi
                printf "\n"

                printf "${Cian_Brillante}[${system}] ${Reset}Instalando paquetes Python globalmente...\n"
                pip3 install "${pip_packages[@]}"
                if [[ $? -ne 0 ]]; then
                    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante} Falló la instalación de algunos paquetes PIP. Revisa los errores anteriores. ${Reset}\n"
                    exit 1
                fi

                cd
                mkdir -p .termux
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
                command cp ~/Stellar/termux/lang_es/config/.bash_profile ~/. 2>/dev/null
                command cp ~/Stellar/termux/lang_es/config/.bashrc ~/. 2>/dev/null
                mkdir -p ~/.termux/fonts
                command cp ~/Stellar/fonts/fira-mono/font.ttf ~/.termux/fonts/ 2>/dev/null

                printf "${Verde_Brillante}[${system}] ${Reset}¡Hecho!\n"
                printf "${Verde_Brillante}[${system}] ${Reset}Cerrando programa en 3 segundos...\n"
                sleep 3
                bash
                exit 1
            fi
        fi

        if [[ "$plataform" == "linux" ]] || [[ "$plataform" == "Linux" ]]; then
            printf "${Cian_Brillante}[${system}] ${Reset}¿Desea saltar proceso de instalación de dependencias?\nPueden haber efectos no deseados\n"
            read -p "» (s/n): " skip_install

            if [[ "$skip_install" == "s" ]]; then
                command cp ~/Stellar/linux/lang_es/config/.bash_profile ~/. 2>/dev/null
                command cp ~/Stellar/linux/lang_es/config/.bashrc ~/. 2>/dev/null
                printf "${Cian_Brillante}[${system}] ${Reset}¡Listo!\nCerrando programa en 3 segundos\n"
                sleep 3
                exit 1
            fi

            if [[ "$skip_install" == "n" ]]; then
                printf "${Cian_Brillante}[${system}] ${Reset}Comenzando instalación....\n"
                command cp ~/Stellar/linux/lang_es/config/.bash_profile ~/. 2>/dev/null
                command cp ~/Stellar/linux/lang_es/config/.bashrc ~/. 2>/dev/null
                sudo apt install "${apt_packages[@]}" -y
                if [[ $? -ne 0 ]]; then
                    printf "\n${Rojo_Brillante}[!][${system}]${Amarillo_Brillante} Falló la instalación de algunos paquetes APT. Revisa los errores anteriores. ${Reset}\n"
                    exit 1
                fi

                printf "\n"

                printf "${Cian_Brillante}[${system}] ${Reset}Probando instalación de paquetes PIP globalmente...\n"
                pip3 install --user beautifulsoup4 2>/dev/null
                if [[ $? -eq 0 ]]; then
                    printf "${Verde_Brillante}[${system}] ${Reset}Se pueden instalar paquetes PIP globalmente.\n"
                    pip3 install "${pip_packages[@]}"
                    if [[ $? -ne 0 ]]; then
                        printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante} Falló la instalación de algunos paquetes PIP. Revisa los errores anteriores. ${Reset}\n"
                        exit 1
                    fi
                else
                    apt install python3.12-venv
                    printf "${Amarillo_Brillante}[${system}] ${Reset}No se pueden instalar paquetes PIP globalmente, creando entorno virtual...\n"
                    python3 -m venv venv
                    if [[ $? -eq 0 ]]; then
                        source venv/bin/activate
                        printf "${Verde_Brillante}[${system}] ${Reset}Entorno virtual activado.\n"
                        pip install "${pip_packages[@]}"
                        if [[ $? -ne 0 ]]; then
                            printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante} Falló la instalación de algunos paquetes PIP. Revisa los errores anteriores. ${Reset}\n"
                            exit 1
                        fi
                        deactivate
                        printf "${Verde_Brillante}[${system}] ${Reset}Entorno virtual creado en la carpeta 'venv'.\n"
                    else
                        printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante} No se pudo crear entorno virtual ni instalar globalmente. ${Reset}\n"
                        exit 1
                    fi
                fi

                printf "${Verde_Brillante}[${system}] ${Reset}¡Hecho!\n"
                printf "${Verde_Brillante}[${system}] ${Reset}Cerrando programa en 3 segundos...\n"
                sleep 3
                printf "${Verde_Brillante}[${system}] ${Reset}Reinicie su terminal para ver los cambios\n"
                exit 1
            fi
        fi
    fi
}

english() {
    printf "${Verde_Brillante}"
    read -p "[${system}] Do you want to start the installation process? (y/n): " next1

    if [[ "$next1" == "n" ]]; then
        printf "${Verde_Brillante}[${system}] ${Reset}Goodbye!\n"
        exit 1
    fi

    if [[ "$next1" == "y" ]]; then
        printf "${Verde_Brillante}"
        read -p "[${system}] Choose your platform (Termux/Linux): " plataform

        if [[ "$plataform" == "Termux" ]]; then
            printf "${Cian_Brillante}[${system}] ${Reset}Do you want to skip the dependency installation process?\nThere may be unwanted effects\n"
            read -p "» (y/n): " skip_install

            if [[ "$skip_install" == "y" ]]; then
                printf "${Cian_Brillante}[${system}] ${Reset}Installing basic configurations....\n"
                cd
                mkdir -p .termux
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
                command cp ~/Stellar/termux/lang_en/config/.bash_profile ~/. 2>/dev/null
                command cp ~/Stellar/termux/lang_en/config/.bashrc ~/. 2>/dev/null
                mkdir -p ~/.termux/fonts
                command cp ~/Stellar/fonts/fira-mono/font.ttf ~/.termux/fonts/ 2>/dev/null
                printf "${Cian_Brillante}[${system}] ${Reset}Done!\nClosing program in 3 seconds\n"
                sleep 3
                exit 1
            fi

            if [[ "$skip_install" == "n" ]]; then
                printf "${Cian_Brillante}[${system}] ${Reset}Starting installation....\n"
                pkg install termux-api -y
                pkg install root-repo -y
                pkg install "${apt_packages[@]}" -y
                if [[ $? -ne 0 ]]; then
                    printf "\n${Rojo_Brillante}[!][${system}]${Amarillo_Brillante} Failed to install some APT packages. Check previous errors. ${Reset}\n"
                    exit 1
                fi
                printf "\n"

                printf "${Cian_Brillante}[${system}] ${Reset}Installing Python packages globally...\n"
                pip3 install "${pip_packages[@]}"
                if [[ $? -ne 0 ]]; then
                    printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante} Failed to install some PIP packages. Check previous errors. ${Reset}\n"
                    exit 1
                fi

                cd
                mkdir -p .termux
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
                command cp ~/Stellar/termux/lang_en/config/.bash_profile ~/. 2>/dev/null
                command cp ~/Stellar/termux/lang_en/config/.bashrc ~/. 2>/dev/null
                mkdir -p ~/.termux/fonts
                command cp ~/Stellar/fonts/fira-mono/font.ttf ~/.termux/fonts/ 2>/dev/null

                printf "${Verde_Brillante}[${system}] ${Reset}Done!\n"
                printf "${Verde_Brillante}[${system}] ${Reset}Closing program in 3 seconds...\n"
                sleep 3
                bash
                exit 1
            fi
        fi

        if [[ "$plataform" == "Linux" ]] || [[ "$plataform" == "linux" ]]; then
            printf "${Cian_Brillante}[${system}] ${Reset}Do you want to skip the dependency installation process?\nThere may be unwanted effects\n"
            read -p "» (y/n): " skip_install

            if [[ "$skip_install" == "y" ]]; then
                command cp ~/Stellar/linux/lang_en/config/.bash_profile ~/. 2>/dev/null
                command cp ~/Stellar/linux/lang_en/config/.bashrc ~/. 2>/dev/null
                printf "${Cian_Brillante}[${system}] ${Reset}Done!\nClosing program in 3 seconds\n"
                sleep 3
                exit 1
            fi

            if [[ "$skip_install" == "n" ]]; then
                printf "${Cian_Brillante}[${system}] ${Reset}Starting installation....\n"
                sudo apt install "${apt_packages[@]}" -y
                if [[ $? -ne 0 ]]; then
                    printf "\n${Rojo_Brillante}[!][${system}]${Amarillo_Brillante} Failed to install some APT packages. Check previous errors. ${Reset}\n"
                    exit 1
                fi

                printf "\n"

                printf "${Cian_Brillante}[${system}] ${Reset}Testing PIP package installation globally...\n"
                pip3 install --user beautifulsoup4 2>/dev/null
                if [[ $? -eq 0 ]]; then
                    printf "${Verde_Brillante}[${system}] ${Reset}PIP packages can be installed globally.\n"
                    pip3 install "${pip_packages[@]}"
                    if [[ $? -ne 0 ]]; then
                        printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante} Failed to install some PIP packages. Check previous errors. ${Reset}\n"
                        exit 1
                    fi
                else
                    apt install python3.12-venv
                    printf "${Amarillo_Brillante}[${system}] ${Reset}Cannot install PIP packages globally, creating virtual environment...\n"
                    python3 -m venv venv
                    if [[ $? -eq 0 ]]; then
                        source venv/bin/activate
                        printf "${Verde_Brillante}[${system}] ${Reset}Virtual environment activated.\n"
                        pip install "${pip_packages[@]}"
                        if [[ $? -ne 0 ]]; then
                            printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante} Failed to install some PIP packages. Check previous errors. ${Reset}\n"
                            exit 1
                        fi
                        deactivate
                        printf "${Verde_Brillante}[${system}] ${Reset}Virtual environment created in 'venv' folder.\n"
                    else
                        printf "\n${Rojo_Brillante}[!]${Amarillo_Brillante} Could not create virtual environment or install globally. ${Reset}\n"
                        exit 1
                    fi
                fi

                printf "${Verde_Brillante}[${system}] ${Reset}Done!\n"
                printf "${Verde_Brillante}[${system}] ${Reset}Closing program in 3 seconds...\n"
                sleep 3
                printf "${Verde_Brillante}[${system}] ${Reset}Restart your terminal to see the changes\n"
                exit 1
            fi
        fi
    fi
}

printf "${Verde_Brillante}"
read -p "Choose your language (Spanish/English): " language

if [[ "$language" == "Spanish" || "$language" == "Español" || "$language" == "spanish" || "$language" == "español" || "$language" == "es" || "$language" == "Es" ]]; then
    spanish
fi

if [[ "$language" == "English" || "$language" == "english" || "$language" == "EN" || "$language" == "En" || "$language" == "en" || "$language" == "Us" ]]; then
    english
fi