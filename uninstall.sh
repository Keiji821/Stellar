#!/bin/bash

gris="\033[1;30m"
blanco="\033[0m"
blanco2="\033[1;37m"
rojo="\033[1;31m"
rojo2="\033[31m"
azul="\033[1;34m"
azul2="\033[34m"
azul_agua="\033[1;36m"
azul_agua2="\033[36m"
verde="\033[1;32m"
verde2="\033[32m"
morado="\033[1;35m"
morado2="\033[35m"
amarillo="\033[1;33m"
amarillo2="\033[33m"
cyan="\033[38;2;23;147;209m"

respuesta=$(dialog --colors --backtitle "Stellar" \
                  --title "Confirmación" \
                  --clear \
                  --yesno "${rojo}¿Desea borrar Stellar completamente? (S/N)${blanco}" 10 60)

case $respuesta in
    Yes)
        rm -rf Stellar && rm -rf .bashrc && rm -rf .bash_profile
        dialog --colors --backtitle "Stellar" \
               --title "Éxito" \
               --clear \
               --msgbox "${verde}Stellar borrado con éxito${blanco}" 10 60
        ;;
    No|*)
        dialog --colors --backtitle "Stellar" \
               --title "Cancelado" \
               --clear \
               --msgbox "${rojo}Operación cancelada${blanco}" 10 60
        ;;
esac

dialog --colors --backtitle "Stellar" \
       --title "Cerrando sesión" \
       --clear \
       --infobox "Cerrando sesión....." 10 60

clear

dialog --colors --backtitle "Stellar" \
       --title "Despedida" \
       --clear \
       --msgbox "Espero hayas disfrutado de mi herramienta! :3 Atte: Keiji821" 15 60

dialog --colors --backtitle "Stellar" \
       --title "Despedida" \
       --clear \
       --msgbox "¡Adiós! :)" 10 60

exit 0
