gris="${b}[1;30m"
blanco="[0m"
blanco2="$b[1;37m"
rojo="${b}[1;31m"
rojo2="${b}[31m"
azul="${b}[1;34m"
azul2="${b}[34m"
azul_agua="${b}\e[1;36m"
azul_agua2="${b}\e[36m"
verde="${b}[1;32m"
verde2="${b}[32m"
morado="$b[1;35m"
morado2="$b[35m"
amarillo="$b[1;33m"
amarillo2="$b[33m"
cyan="$b[38;2;23;147;209m"

read -p "${rojo}¿Desea borrar Stellar completamente? S/N${blanco} " respuesta

if [ "$respuesta" = "s" ] || [ "$respuesta" = "S" ] || [ "$respuesta" = "sí" ] || [ "$respuesta" = "Si" ]; then
rm -rf Stellar && rm -rf .bashrc && rm -rf .bash_profile

printf "${verde}Stellar borrado con éxito${blanco}"
else
printf "${rojo}Operación cancelada${blanco}"
fi

printf "Cerrando sesión....." | lolcat -a -d 30

clear

printf "Espero hayas disfrutado de mi herramienta! :3 Atte: Keiji821" | lolcat -a -d 100
printf "¡Adiós! :)" | lolcat -a -d 20

login