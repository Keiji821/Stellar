#!/bin/bash
PROGRESO_CANAL="$HOME/.progress_pipe"
trap 'exec 3>&-; [[ -p "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"' EXIT

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
    [[ -p "$PROGRESO_CANAL" ]] && rm -f "$PROGRESO_CANAL"
    mkfifo "$PROGRESO_CANAL"
    dialog --title "Instalador de Stellar" --programbox 20 70 < "$PROGRESO_CANAL" &
    exec 3> "$PROGRESO_CANAL"

    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)
    total_steps=$(( ${#apt_packages[@]} + ${#pip_packages[@]} + 2 ))
    current=0
    spinner=('|' '/' '-' '\\')
    idx=0

    spinner_next(){
        char="${spinner[idx]}"
        idx=$(( (idx+1) % 4 ))
        echo "$char"
    }

    echo "== Actualización del sistema ==" >&3
    char=$(spinner_next)
    echo "[$char] Actualizando lista de paquetes... ($((current+1))/$total_steps)" >&3
    apt update -y >/dev/null 2>&1; ((current++))
    echo "[✔] Lista de paquetes actualizada. ($current/$total_steps)" >&3
    sleep 0.2

    char=$(spinner_next)
    echo "[$char] Actualizando sistema... ($((current+1))/$total_steps)" >&3
    apt upgrade -y >/dev/null 2>&1; ((current++))
    echo "[✔] Sistema actualizado. ($current/$total_steps)" >&3
    sleep 0.2

    echo "== Instalación de paquetes APT ==" >&3
    for pkg in "${apt_packages[@]}"; do
        char=$(spinner_next)
        echo "[$char] Instalando $pkg (APT) ($((current+1))/$total_steps)" >&3
        if apt install -y "$pkg" >/dev/null 2>&1; then status="✔"; else status="✖"; fi
        ((current++))
        echo "[$status] $pkg. ($current/$total_steps)" >&3
        sleep 0.2
    done

    echo "== Instalación de paquetes PIP ==" >&3
    for pkg in "${pip_packages[@]}"; do
        char=$(spinner_next)
        echo "[$char] Instalando $pkg (pip) ($((current+1))/$total_steps)" >&3
        if pip install "$pkg" >/dev/null 2>&1; then status="✔"; else status="✖"; fi
        ((current++))
        echo "[$status] $pkg. ($current/$total_steps)" >&3
        sleep 0.2
    done

    echo "[✔] Instalación completada. ($current/$total_steps)" >&3
    echo -e "\a" >&3
    sleep 1
    exec 3>&-
    rm -f "$PROGRESO_CANAL"
}

main(){
    [[ ! -d ~/Stellar ]] && mkdir -p ~/Stellar
    user_config
    iniciar_instalacion
    dialog --title "Instalación Completa" --msgbox "¡Todos los componentes se instalaron correctamente!" 8 50
    clear
}

main