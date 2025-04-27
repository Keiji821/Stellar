#!/bin/bash

PROGRESO_CANAL="/tmp/progress_pipe"

user_config() {
    while true; do
        username=$(dialog --title "Configuración de Usuario" \
                          --inputbox "Ingrese un nombre de usuario (4-15 caracteres, letras/números/_):" 10 60 3>&1 1>&2 2>&3)
        
        if [[ $? -ne 0 ]]; then
            clear
            echo "Instalación cancelada."
            exit 1
        fi

        [[ -z "$username" ]] && continue
        [[ ${#username} -lt 4 || ${#username} -gt 15 ]] && continue
        [[ "$username" =~ ^[a-zA-Z0-9_]+$ ]] && break
    done

    mkdir -p ~/Stellar/config/system
    echo "$username" > ~/Stellar/config/system/user.txt
}

iniciar_instalacion() {
    mkfifo "$PROGRESO_CANAL"
    
    dialog --title "Instalador Stellar" --gauge "Preparando instalación..." 10 60 0 < "$PROGRESO_CANAL" &
    
    exec 3>"$PROGRESO_CANAL"
    
    # Paquetes a instalar
    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    
    total_pasos=$((2 + ${#apt_packages[@]} + ${#pip_packages[@]}))
    paso_actual=0
    
    echo "XXX\n0\nIniciando proceso de instalación...\nXXX" >&3
    
    # Actualizar sistema
    echo "XXX\n5\nActualizando lista de paquetes...\nXXX" >&3
    apt update -y >/dev/null 2>&1
    echo "XXX\n10\nActualizando sistema...\nXXX" >&3
    apt upgrade -y >/dev/null 2>&1
    
    # Instalar paquetes APT
    for pkg in "${apt_packages[@]}"; do
        paso_actual=$((paso_actual + 1))
        progreso=$((10 + 40 * paso_actual / ${#apt_packages[@]}))
        echo "XXX\n$progreso\nInstalando $pkg (APT)...\nXXX" >&3
        apt install -y "$pkg" >/dev/null 2>&1
    done
    
    # Instalar paquetes PIP
    for pkg in "${pip_packages[@]}"; do
        paso_actual=$((paso_actual + 1))
        progreso=$((50 + 50 * paso_actual / (${#apt_packages[@]} + ${#pip_packages[@]})))
        echo "XXX\n$progreso\nInstalando $pkg (pip)...\nXXX" >&3
        pip install "$pkg" >/dev/null 2>&1
    done
    
    # Finalización
    echo "XXX\n100\nInstalación completada exitosamente!\nXXX" >&3
    sleep 2
    
    exec 3>&-
    rm -f "$PROGRESO_CANAL"
}

main() {
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    
    user_config
    iniciar_instalacion
    
    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main