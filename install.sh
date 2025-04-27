#!/bin/bash
PIPE="$HOME/.stellar_pipe"
trap 'cleanup' EXIT

cleanup(){
    [[ -n "$DIALOG_PID" ]] && kill $DIALOG_PID 2>/dev/null
    exec 3>&- 2>/dev/null
    rm -f "$PIPE"
}

user_config(){
    while true; do
        username=$(dialog --title "Configuración de Usuario" \
                          --inputbox "Usuario (4–15 caracteres, letras/números/_):" 10 60 3>&1 2>&1)
        [[ $? -ne 0 ]] && { clear; echo "Instalación cancelada."; exit 1; }
        [[ ${#username} -ge 4 && ${#username} -le 15 && "$username" =~ ^[a-zA-Z0-9_]+$ ]] && break
    done
    mkdir -p ~/Stellar/config/system
    echo "$username" > ~/Stellar/config/system/user.txt
}

iniciar_instalacion(){
    rm -f "$PIPE"
    mkfifo "$PIPE"
    dialog --title "Instalador de Stellar" --programbox 20 70 < "$PIPE" &
    DIALOG_PID=$!
    exec 3> "$PIPE"
    # espera a que dialog esté leyendo
    sleep 0.2

    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    total=$(( ${#apt_packages[@]} + ${#pip_packages[@]} + 2 ))
    step=0
    spinner=('|' '/' '-' '\\')
    idx=0
    spin(){ printf "%s" "${spinner[idx]}"; idx=$(( (idx+1)%4 )); }

    echo "== Instalador de Stellar ==" >&3
    echo "" >&3

    echo "Preparando actualización... (0/$total)" >&3
    sleep 0.3

    ((step++))
    echo "[$(spin)] Actualizando APT... ($step/$total)" >&3
    apt update -y >/dev/null 2>&1
    echo "[✔] APT actualizado. ($step/$total)" >&3
    sleep 0.3

    ((step++))
    echo "[$(spin)] Upgrade de sistema... ($step/$total)" >&3
    apt upgrade -y >/dev/null 2>&1
    echo "[✔] Sistema upgraded. ($step/$total)" >&3
    sleep 0.3

    echo "" >&3
    echo "== Paquetes APT ==" >&3
    for pkg in "${apt_packages[@]}"; do
        ((step++))
        echo "[$(spin)] Instalando $pkg... ($step/$total)" >&3
        if apt install -y "$pkg" >/dev/null 2>&1; then
            echo "[✔] $pkg instalado. ($step/$total)" >&3
        else
            echo "[✖] Error con $pkg. ($step/$total)" >&3
        fi
        sleep 0.2
    done

    echo "" >&3
    echo "== Paquetes PIP ==" >&3
    for pkg in "${pip_packages[@]}"; do
        ((step++))
        echo "[$(spin)] Instalando $pkg... ($step/$total)" >&3
        if pip install "$pkg" >/dev/null 2>&1; then
            echo "[✔] $pkg instalado. ($step/$total)" >&3
        else
            echo "[✖] Error con $pkg. ($step/$total)" >&3
        fi
        sleep 0.2
    done

    echo "" >&3
    echo "[✔] Instalación completa. ($step/$total)" >&3
    sleep 1

    exec 3>&-
}

main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    user_config
    iniciar_instalacion
    dialog --title "Instalación Completa" \
           --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main