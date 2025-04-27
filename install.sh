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

install_tasks(){
    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)

    echo "== Instalador de Stellar =="  
    echo

    echo "[*] Preparando instalación..."
    sleep 1

    echo "[*] Actualizando lista de paquetes..."
    apt update -y >/dev/null 2>&1
    echo "[✔] Lista de paquetes actualizada."
    echo

    echo "[*] Actualizando sistema..."
    apt upgrade -y >/dev/null 2>&1
    echo "[✔] Sistema actualizado."
    echo

    echo "== Instalación de paquetes APT =="
    for pkg in "${apt_packages[@]}"; do
        echo "[*] Instalando $pkg (APT)..."
        if apt install -y "$pkg" >/dev/null 2>&1; then
            echo "[✔] $pkg instalado correctamente."
        else
            echo "[✖] Error al instalar $pkg."
        fi
        sleep 0.3
    done
    echo

    echo "== Instalación de paquetes PIP =="
    for pkg in "${pip_packages[@]}"; do
        echo "[*] Instalando $pkg (pip)..."
        if pip install "$pkg" >/dev/null 2>&1; then
            echo "[✔] $pkg instalado correctamente."
        else
            echo "[✖] Error al instalar $pkg."
        fi
        sleep 0.3
    done
    echo

    echo "[✔] ¡Instalación completada exitosamente!"
}

main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    user_config

    # Aquí va todo el output de install_tasks dentro de la caja
    install_tasks | dialog --title "Instalador de Stellar" --progressbox 20 70

    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main