#!/bin/bash

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
    (
        apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
        pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
        total_steps=$(( ${#apt_packages[@]} + ${#pip_packages[@]} + 2 ))
        current=0
        spinner=('|' '/' '-' '\\')
        idx=0

        spinner_next(){
            echo -n "${spinner[idx]}"
            idx=$(( (idx+1) % 4 ))
        }

        echo "== Instalador de Stellar =="

        echo
        echo "Preparando actualización..."
        apt update -y >/dev/null 2>&1
        ((current++))
        echo "[✔] Lista de paquetes actualizada ($current/$total_steps)"

        echo "Actualizando sistema..."
        apt upgrade -y >/dev/null 2>&1
        ((current++))
        echo "[✔] Sistema actualizado ($current/$total_steps)"

        echo
        echo "Instalando paquetes APT..."
        for pkg in "${apt_packages[@]}"; do
            echo "[$(spinner_next)] Instalando $pkg..."
            if apt install -y "$pkg" >/dev/null 2>&1; then
                echo "[✔] $pkg instalado ($((++current))/$total_steps)"
            else
                echo "[✖] Error al instalar $pkg ($((++current))/$total_steps)"
            fi
            sleep 0.2
        done

        echo
        echo "Instalando paquetes PIP..."
        for pkg in "${pip_packages[@]}"; do
            echo "[$(spinner_next)] Instalando $pkg..."
            if pip install "$pkg" >/dev/null 2>&1; then
                echo "[✔] $pkg instalado ($((++current))/$total_steps)"
            else
                echo "[✖] Error al instalar $pkg ($((++current))/$total_steps)"
            fi
            sleep 0.2
        done

        echo
        echo "[✔] Instalación completada exitosamente."
    ) | dialog --title "Instalador de Stellar" --programbox 30 80
}

main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    user_config
    iniciar_instalacion
    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main