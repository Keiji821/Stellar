#!/bin/bash

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

clear

banner="""
███████╗████████╗███████╗██╗     ██╗      █████╗ ██████╗ 
██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗██╔══██╗
███████╗   ██║   █████╗  ██║     ██║     ███████║██████╔╝
╚════██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║██╔══██╗
███████║   ██║   ███████╗███████╗███████╗██║  ██║██║  ██║
╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

                                   @Desinstalador/Uninstaller"""

printf "${Azul_Brillante} ${banner} ${Reset}"
printf "\n"
printf "\n${Magenta_Brillante}⭐ Created by: Keiji821 ${Reset}"
printf "\n${Cian_Brillante}🔵 My Discord contact: ${Verde_Brillante}keiji100 ${Reset}"
printf "\n${Magenta_Brillante}📦 Repository ${Rojo_Brillante} >>> ${Cian_Brillante}${Subrayado}https://github.com/Keiji821/Stellar${Reset}\n"
printf "\n"
printf "\n${Rojo_Brillante}[!]${Blanco_Brillante} Note: The program is currently in Spanish,\nwith full English support coming soon. ${Reset}"
printf "\n"

printf "\n${Amarillo_Brillante}"
read -p "• Elija su idioma/Choose your language (Español/English): " language


# Desinstalador/Uninstaller

if [[ "$language" == "Español" || "$language" == "Spanish" || "$language" == "spanish" || "$language" == "español" || "$language" == "es" ]]; then
    echo -e "${Rojo_Brillante}¿Desea eliminar Stellar completamente?${Reset}"
    read -p "\nEsta acción no se puede deshacer [S/N]: " respuesta

    if [[ "$respuesta" =~ ^[SsYy]$|^[Ss]í$|^[Ss]i$ ]]; then
        echo -e "\n${Rojo_Brillante}➤ Eliminando archivos de Stellar...${Reset}"
        rm -rf ~/Stellar
        rm -rf ~/.bashrc
        rm -rf ~/.bash_profile
        rm -rf ~/tor.txt
        echo -e "\n${Verde_Brillante}✔ Stellar se ha eliminado completamente${Reset}"
        echo -e "\n${Magenta_Brillante}Gracias por haber utilizado Stellar!"
        echo -e "\n${Cian_Brillante}Atte: Keiji821${Reset}"
        echo -e "\n${Azul_Brillante}¡Hasta pronto! :)${Reset}"
    else
        echo -e "${Amarillo_Brillante}➤ Operación cancelada${Reset}"
    fi
sleep 3
login
fi


if [[ "$language" == "English" || "$language" == "english" || "$language" == "en" ]]; then
    echo -e "${Rojo_Brillante}Do you want to remove Stellar completely?${Reset}"
    read -p "\nThis action cannot be undone [S/N]: " respuesta

    if [[ "$respuesta" =~ ^[SsYy]$|^[Ss]í$|^[Ss]i$ ]]; then
        echo -e "\n${Rojo_Brillante}➤ Deleting files from Stellar...${Reset}"
        rm -rf ~/Stellar
        rm -rf ~/.bashrc
        rm -rf ~/.bash_profile
        rm -rf ~/tor.txt
        echo -e "\n${Verde_Brillante}✔ Stellar has been completely removed${Reset}"
        echo -e "\n${Magenta_Brillante}Thank you for using Stellar!"
        echo -e "\n${Cian_Brillante}Atte: Keiji821${Reset}"
        echo -e "\n${Azul_Brillante}¡See you soon! :)${Reset}"
    else
        echo -e "${Amarillo_Brillante}➤ Operation cancelled${Reset}"
    fi
sleep 3
login
fi