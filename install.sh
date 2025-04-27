#!/bin/bash
PROGRESO_CANAL="$HOME/.progress_pipe"
user_config(){
    while true; do
        username=$(dialog --title "Configuración de Usuario" \
            --inputbox "Ingrese un nombre de usuario (4-15 caracteres, letras/números/_):" 10 60 3>&1 2>&1)
        [[ $? -ne 0 ]] && { clear; echo "Instalación cancelada."; exit 1; }
        [[ ${#username} -ge 4 && ${#username} -le 15 && "$username" =~ ^[a-zA-Z0-9_]+$ ]] && break
    done
    mkdir -p ~/Stellar/config/system
    echo "$username" > ~/Stellar/config/system/user.txt
}
iniciar_instalacion(){
    [[ -e "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"
    mkfifo "$PROGRESO_CANAL"
    dialog --title "Instalador de Stellar" --colors --programbox 20 70 < "$PROGRESO_CANAL" &
    exec 3>"$PROGRESO_CANAL"
    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    echo "\Z6➔ Preparando la instalación...\Zn" >&3; sleep 1
    echo "\Z6➔ Actualizando lista de paquetes...\Zn" >&3
    if apt update -y >/dev/null 2>&1; then
        echo "\Z2✔ Lista de paquetes actualizada.\Zn" >&3
    else
        echo "\Z1✘ Error al actualizar lista de paquetes.\Zn" >&3
    fi; sleep 0.5
    echo "\Z6➔ Actualizando sistema...\Zn" >&3
    if apt upgrade -y >/dev/null 2>&1; then
        echo "\Z2✔ Sistema actualizado.\Zn" >&3
    else
        echo "\Z1✘ Error al actualizar el sistema.\Zn" >&3
    fi; sleep 0.5
    for pkg in "${apt_packages[@]}"; do
        echo "\Z3➔ Instalando $pkg (APT)...\Zn" >&3
        if apt install -y "$pkg" >/dev/null 2>&1; then
            echo "\Z2✔ $pkg instalado correctamente.\Zn" >&3
        else
            echo "\Z1✘ Error al instalar $pkg.\Zn" >&3
        fi
        sleep 0.3
    done
    for pkg in "${pip_packages[@]}"; do
        echo "\Z3➔ Instalando $pkg (pip)...\Zn" >&3
        if pip install "$pkg" >/dev/null 2>&1; then
            echo "\Z2✔ $pkg instalado correctamente.\Zn" >&3
        else
            echo "\Z1✘ Error al instalar $pkg (pip).\Zn" >&3
        fi
        sleep 0.3
    done
    echo "\Z5✔ ¡Instalación completada exitosamente!\Zn" >&3
    sleep 2
    exec 3>&-; rm -f "$PROGRESO_CANAL"
}
main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    user_config
    iniciar_instalacion
    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}
main