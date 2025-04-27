#!/bin/bash

LOG="$HOME/stellar_install.log"
trap 'rm -f "$LOG"' EXIT

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

install_tasks(){
    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    total_steps=$(( ${#apt_packages[@]} + ${#pip_packages[@]} + 2 ))
    current=0
    spinner=('|' '/' '-' '\\')
    idx=0

    spinner_next(){
        printf "%s" "${spinner[idx]}"
        idx=$(( (idx+1) % 4 ))
    }

    echo "== Instalador de Stellar =="                        >> "$LOG"
    echo                                                    >> "$LOG"
    echo "[*] Preparando actualización... (0/$total_steps)" >> "$LOG"
    sleep 0.5

    echo "[${spinner_next}] Actualizando lista de paquetes... ($((++current))/$total_steps)" >> "$LOG"
    apt update -y   >> "$LOG" 2>&1
    echo "[✔] Lista de paquetes actualizada ($current/$total_steps)"                   >> "$LOG"
    sleep 0.3

    echo "[${spinner_next}] Actualizando sistema... ($((++current))/$total_steps)"      >> "$LOG"
    apt upgrade -y  >> "$LOG" 2>&1
    echo "[✔] Sistema actualizado ($current/$total_steps)"                             >> "$LOG"
    sleep 0.3

    echo                                                    >> "$LOG"
    echo "== Instalación de paquetes APT =="                 >> "$LOG"
    for pkg in "${apt_packages[@]}"; do
        echo "[${spinner_next}] Instalando $pkg (APT) ($((current+1))/$total_steps)" >> "$LOG"
        if apt install -y "$pkg" >> "$LOG" 2>&1; then
            current=$((current+1))
            echo "[✔] $pkg instalado ($current/$total_steps)"                        >> "$LOG"
        else
            current=$((current+1))
            echo "[✖] Error al instalar $pkg ($current/$total_steps)"               >> "$LOG"
        fi
        sleep 0.2
    done

    echo                                                    >> "$LOG"
    echo "== Instalación de paquetes PIP =="                 >> "$LOG"
    for pkg in "${pip_packages[@]}"; do
        echo "[${spinner_next}] Instalando $pkg (pip) ($((current+1))/$total_steps)" >> "$LOG"
        if pip install "$pkg" >> "$LOG" 2>&1; then
            current=$((current+1))
            echo "[✔] $pkg instalado ($current/$total_steps)"                        >> "$LOG"
        else
            current=$((current+1))
            echo "[✖] Error al instalar $pkg ($current/$total_steps)"               >> "$LOG"
        fi
        sleep 0.2
    done

    echo                                                    >> "$LOG"
    echo "[✔] Instalación completada exitosamente ($current/$total_steps)"           >> "$LOG"
}

main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    > "$LOG"
    user_config

    dialog --title "Instalador de Stellar" --tailboxbg "$LOG" 20 70 &
    DLG_PID=$!

    install_tasks

    # damos un segundo para que tailbox bg muestre la última línea
    sleep 1
    kill "$DLG_PID" 2>/dev/null

    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main