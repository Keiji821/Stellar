#!/bin/bash
gris="\033[1;30m"
blanco="\033[0m"
blanco2="\033[1;37m"
rojo="\033[1;31m"
rojo2="\033[31m"
azul="\033[1;34m"
azul2="\033[34m"
azul_agua="\e[1;36m"
azul_agua2="\e[36m"
verde="\033[1;32m"
verde2="\033[32m"
morado="\033[1;35m"
morado2="\033[35m"
amarillo="\033[1;33m"
amarillo2="\033[33m"
cyan="\033[38;2;23;147;209m"

PROGRESO_CANAL="$HOME/.progress_pipe"

user_config(){
    while true; do
        username=$(dialog --title "Configuración de Usuario" \
                          --inputbox "${cyan}Ingrese un nombre de usuario (4-15 caracteres, letras/números/_)${blanco}" 10 60 3>&1 1>&2 2>&3)
        [[ $? -ne 0 ]] && { clear; echo -e "${rojo}Instalación cancelada.${blanco}"; exit 1; }
        [[ ${#username} -ge 4 && ${#username} -le 15 && "$username" =~ ^[a-zA-Z0-9_]+$ ]] && break
    done
    mkdir -p ~/Stellar/config/system
    echo "$username" > ~/Stellar/config/system/user.txt
}

iniciar_instalacion(){
    [[ -e "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"
    mkfifo "$PROGRESO_CANAL"
    dialog --title "Instalador de Stellar" --programbox 20 70 < "$PROGRESO_CANAL" &
    exec 3>"$PROGRESO_CANAL"

    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)

    echo -e "${azul}➔ Preparando la instalación...${blanco}" >&3
    sleep 1

    echo -e "${azul_agua}➔ Actualizando lista de paquetes...${blanco}" >&3
    if apt update -y >/dev/null 2>&1; then
        echo -e "${verde}✔ Lista de paquetes actualizada.${blanco}" >&3
    else
        echo -e "${rojo}✘ Error al actualizar lista de paquetes.${blanco}" >&3
    fi
    sleep 0.5

    echo -e "${azul_agua}➔ Actualizando sistema...${blanco}" >&3
    if apt upgrade -y >/dev/null 2>&1; then
        echo -e "${verde}✔ Sistema actualizado.${blanco}" >&3
    else
        echo -e "${rojo}✘ Error al actualizar el sistema.${blanco}" >&3
    fi
    sleep 0.5

    for pkg in "${apt_packages[@]}"; do
        echo -e "${amarillo}➔ Instalando $pkg (APT)...${blanco}" >&3
        if apt install -y "$pkg" >/dev/null 2>&1; then
            echo -e "${verde}✔ $pkg instalado correctamente.${blanco}" >&3
        else
            echo -e "${rojo}✘ Error al instalar $pkg.${blanco}" >&3
        fi
        sleep 0.3
    done

    for pkg in "${pip_packages[@]}"; do
        echo -e "${amarillo2}➔ Instalando $pkg (pip)...${blanco}" >&3
        if pip install "$pkg" >/dev/null 2>&1; then
            echo -e "${verde2}✔ $pkg instalado correctamente.${blanco}" >&3
        else
            echo -e "${rojo2}✘ Error al instalar $pkg (pip).${blanco}" >&3
        fi
        sleep 0.3
    done

    echo -e "${morado}✔ ¡Instalación completada exitosamente!${blanco}" >&3
    sleep 2

    exec 3>&-
    rm -f "$PROGRESO_CANAL"
}

main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    user_config
    iniciar_instalacion
    dialog --title "Instalación Completa" --msgbox "$(echo -e "${verde2}¡Todos los componentes se instalaron correctamente!${blanco}")" 8 50
    clear
}

main