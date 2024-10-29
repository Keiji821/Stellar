# Definir colores

gris="${b}\033[1;30m"
blanco="\033[0m"
blanco2="$b\033[1;37m"
rojo="${b}\033[1;31m"
rojo2="${b}\033[31m"
azul="${b}\033[1;34m"
azul2="${b}\033[34m"
azul_agua="${b}\e[1;36m"
azul_agua2="${b}\e[36m"
verde="${b}\033[1;32m"
verde2="${b}\033[32m"
morado="$b\033[1;35m"
morado2="$b\033[35m"
amarillo="$b\033[1;33m"
amarillo2="$b\033[33m"
cyan="$b\033[38;2;23;147;209m"

# Actualizar .bashrc y .bash_profile

cp ~/Stellar/.bash_profile ~/.
cp ~/Stellar/.bashrc ~/.

# Actualizar paquetes automáticamente 

