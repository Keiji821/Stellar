#!/bin/bash

user_config(){
    while true; do
        username=$(dialog --title "Configuración de Usuario" \
                          --inputbox "Ingrese un nombre de usuario (4–15 caracteres, letras/números/_):" 10 60 3>&1 2>&1)
        [[ $? -ne 0 ]] && { clear; echo "Instalación cancelada."; exit 1; }
        [[ ${#username} -ge 4 && ${#username} -le 15 && "$username" =~ ^[a-zA-Z0-9_]+$ ]] && break
    done
    mkdir -p ~/Stellar/config/system
    echo "$username" > ~/Stellar/config/system/user.txt
}

iniciar_instalacion(){
    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    total=$(( ${#apt_packages[@]} + ${#pip_packages[@]} + 2 ))
    step=0
    spinner=('|' '/' '-' '\\')
    idx=0

    logtext="Instalador de Stellar\n\n"

    # Función para refrescar la ventana
    show(){
        dialog --title "Instalador de Stellar" --infobox "$logtext" 20 70
    }

    # Inicio
    ((step++))
    logtext+="[*] Preparando actualización... ($step/$total)\n"
    show
    sleep 0.5

    # Actualizar lista de paquetes
    ((step++))
    logtext+="[*] Actualizando lista de paquetes... ($step/$total)\n"
    show
    apt update -y >/dev/null 2>&1
    logtext+="[✔] Lista de paquetes actualizada. ($step/$total)\n\n"
    show
    sleep 0.5

    # Upgrade sistema
    ((step++))
    logtext+="[*] Actualizando sistema... ($step/$total)\n"
    show
    apt upgrade -y >/dev/null 2>&1
    logtext+="[✔] Sistema actualizado. ($step/$total)\n\n"
    show
    sleep 0.5

    # Paquetes APT
    logtext+="== Instalación de paquetes APT ==\n"
    show
    for pkg in "${apt_packages[@]}"; do
        ((step++))
        # animación breve de spinner
        char="${spinner[idx]}"; idx=$(( (idx+1)%4 ))
        logtext+="[${char}] Instalando $pkg... ($step/$total)\n"
        show
        apt install -y "$pkg" >/dev/null 2>&1
        logtext+="[✔] $pkg instalado. ($step/$total)\n"
        show
        sleep 0.3
    done
    logtext+="\n"

    # Paquetes PIP
    logtext+="== Instalación de paquetes PIP ==\n"
    show
    for pkg in "${pip_packages[@]}"; do
        ((step++))
        char="${spinner[idx]}"; idx=$(( (idx+1)%4 ))
        logtext+="[${char}] Instalando $pkg... ($step/$total)\n"
        show
        pip install "$pkg" >/dev/null 2>&1
        logtext+="[✔] $pkg instalado. ($step/$total)\n"
        show
        sleep 0.3
    done
    logtext+="\n[✔] Instalación completada exitosamente. ($step/$total)\n"
    show
    sleep 1
}

main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    user_config
    iniciar_instalacion
    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main