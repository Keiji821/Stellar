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
echo -e "==============================${Reset}"
echo -e "${Cian_Brillante}STELLAR OS"
echo -e "==============================${Reset}"

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

echo -e "\n${Magenta_Brillante}Gracias por haber utilizado Stellar!"
echo -e "${Cian_Brillante}Atte: Keiji821${Reset}"
echo -e "${Azul_Brillante}¡Hasta pronto! :)${Reset}\n"
sleep 3
login