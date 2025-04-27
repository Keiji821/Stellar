#!/bin/bash

PROGRESO_CANAL="$HOME/.progress_pipe"

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
    if [[ -e "$PROGRESO_CANAL" ]]; then
        rm -f "$PROGRESO_CANAL"
    fi

    mkfifo "$PROGRESO_CANAL"

    dialog --title "Instalador de Stellar" --programbox 20 70 < "$PROGRESO_CANAL" &
    exec 3>"$PROGRESO_CANAL"

    apt_packages=(python tor cloudflared exiftool nmap termux-api dnsutils nodejs)
    pip_packages=(beautifulsoup4 pyfiglet phonenumbers psutil PySocks requests rich "rich[jupyter]" lolcat discord)

    echo "➔ Preparando la instalación..." >&3
    sleep 1

    echo "➔ Actualizando lista de paquetes..." >&3
    if apt update -y >/dev/null 2>&1; then
        echo "✔ Lista de paquetes actualizada." >&3
    else
        echo "✘ Error al actualizar lista de paquetes." >&3
    fi
    sleep 0.5

    echo "➔ Actualizando sistema..." >&3
    if apt upgrade -y >/dev/null 2>&1; then
        echo "✔ Sistema actualizado." >&3
    else
        echo "✘ Error al actualizar el sistema." >&3
    fi
    sleep 0.5

    for pkg in "${apt_packages[@]}"; do
        echo "➔ Instalando $pkg (APT)..." >&3
        if apt install -y "$pkg" >/dev/null 2>&1; then
            echo "✔ $pkg instalado correctamente." >&3
        else
            echo "✘ Error al instalar $pkg." >&3
        fi
        sleep 0.3
    done

    for pkg in "${pip_packages[@]}"; do
        echo "➔ Instalando $pkg (pip)..." >&3
        if pip install "$pkg" >/dev/null 2>&1; then
            echo "✔ $pkg instalado correctamente." >&3
        else
            echo "✘ Error al instalar $pkg (pip)." >&3
        fi
        sleep 0.3
    done

    echo "✔ ¡Instalación completada exitosamente!" >&3
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