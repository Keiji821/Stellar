#!/bin/bash

Negro="\033[0;30m"
Rojo="\033[0;31m"
Verde="\033[0;32m"
Amarillo="\033[0;33m"
Azul="\033[0;34m"
Magenta="\033[0;35m"
Cian="\033[0;36m"
Blanco="\033[0;37m"

Rojo_Brillante="\033[1;31m"
Verde_Brillante="\033[1;32m"
Amarillo_Brillante="\033[1;33m"
Reset="\033[0m"

clear
echo -e "${Cian}"
echo -e "  ███████╗████████╗███████╗██╗     ██╗      █████╗ ██████╗  "
echo -e "  ██╔════╝╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗██╔══██╗ "
echo -e "  ███████╗   ██║   █████╗  ██║     ██║     ███████║██████╔╝ "
echo -e "  ╚════██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║██╔══██╗ "
echo -e "  ███████║   ██║   ███████╗███████╗███████╗██║  ██║██║  ██║ "
echo -e "  ╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ${Reset}"
echo -e "${Magenta}╭──────────────────────────────────────────────╮"
echo -e "│          ${Blanco}DESINSTALACIÓN DE STELLAR${Magenta}          │"
echo -e "╰──────────────────────────────────────────────╯${Reset}"

echo -e "${Rojo_Brillante}¿Desea eliminar Stellar completamente?${Reset}"
read -p "Esta acción no se puede deshacer [S/N]: " respuesta

if [[ "$respuesta" =~ ^[SsYy]$|^[Ss]í$|^[Ss]i$ ]]; then
    echo -e "\n${Rojo}➤ Eliminando archivos de Stellar...${Reset}"
    rm -rf ~/Stellar
    rm -f ~/.bashrc
    rm -f ~/.bash_profile
    echo -e "${Verde_Brillante}✔ Stellar se ha eliminado completamente${Reset}"
else
    echo -e "\n${Amarillo_Brillante}➤ Operación cancelada${Reset}"
fi

echo -e "\n${Magenta}╭──────────────────────────────────────────────╮"
echo -e "│     ${Blanco}Gracias por haber utilizado Stellar!${Magenta}     │"
echo -e "│             ${Cian}Atte: Keiji821${Magenta}                │"
echo -e "╰──────────────────────────────────────────────╯${Reset}"
echo -e "${Azul}¡Hasta pronto! :)${Reset}\n"