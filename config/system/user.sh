#!/bin/bash

Gris="\033[1;30m"
Negro="\033[0;30m"
Rojo="\033[0;31m"
Verde="\033[0;32m"
Amarillo="\033[0;33m"
Azul="\033[0;34m"
Magenta="\033[0;35m"
Cian="\033[0;36m"
Blanco="\033[0;37m"

Negro_Brillante="\033[1;30m"
Rojo_Brillante="\033[1;31m"
Verde_Brillante="\033[1;32m"
Amarillo_Brillante="\033[1;33m"
Azul_Brillante="\033[1;34m"
Magenta_Brillante="\033[1;35m"
Cian_Brillante="\033[1;36m"
Blanco_Brillante="\033[1;37m"

Fondo_Negro="\033[40m"
Fondo_Rojo="\033[41m"
Fondo_Verde="\033[42m"
Fondo_Amarillo="\033[43m"
Fondo_Azul="\033[44m"
Fondo_Magenta="\033[45m"
Fondo_Cian="\033[46m"
Fondo_Blanco="\033[47m"

Fondo_Negro_Brillante="\033[0;100m"
Fondo_Rojo_Brillante="\033[0;101m"
Fondo_Verde_Brillante="\033[0;102m"
Fondo_Amarillo_Brillante="\033[0;103m"
Fondo_Azul_Brillante="\033[0;104m"
Fondo_Magenta_Brillante="\033[0;105m"
Fondo_Cian_Brillante="\033[0;106m"
Fondo_Blanco_Brillante="\033[0;107m"

Reset="\033[0m"
Negrita="\033[1m"
Atenuado="\033[2m"
Italico="\033[3m"
Subrayado="\033[4m"
Parpadeo="\033[5m"
Invertido="\033[7m"
Oculto="\033[8m"
Tachado="\033[9m"

error() {
    echo -e "${Rojo_Brillante}$1${Reset}"
    sleep 1
}

success() {
    echo -e "${Verde_Brillante}$1${Reset}"
    sleep 1
}

check_termux_api() {
    if ! pkg list-installed | grep -q 'termux-api'; then
        error "Termux-API no está instalado. Instale con: pkg install termux-api"
        return 1
    fi
    return 0
}

configure_user() {
    [ -f "user.txt" ] && return 0

    while true; do
        read -p "$(echo -e "${Verde_Brillante}No tiene usuario configurado\n¿Desea configurarlo? (y/n): ${Reset}")" response

        case $response in
            [yY]*)
                while true; do
                    read -p "$(echo -e "${Verde_Brillante}Ingrese nombre de usuario: ${Reset}")" username
                    username=$(echo "$username" | xargs)
                    
                    [ -z "$username" ] && error "No puede estar vacío" && continue
                    
                    if echo "$username" > "user.txt"; then
                        success "✓ Usuario configurado"
                        return 0
                    else
                        error "Error al guardar"
                        continue
                    fi
                done
                ;;
            [nN]*) return 0 ;;
            *) error "Opción no válida. Use 'y' o 'n'" ;;
        esac
    done
}

configure_auth() {
    [ -f "login_method.txt" ] && return 0

    while true; do
        read -p "$(echo -e "${Verde_Brillante}No tiene método de bloqueo\n¿Desea configurarlo? (y/n/no): ${Reset}")" response
        response=$(echo "$response" | tr '[:upper:]' '[:lower:]')
        
        case $response in
            y)
                echo -e "\n${Verde}Métodos disponibles:${Reset}"
                echo -e "${Verde}1. Huella dactilar${Reset}"
                echo -e "${Rojo}ADVERTENCIA: Requiere Termux-API${Reset}"
                
                while true; do
                    read -p "$(echo -e "${Verde_Brillante}Seleccione (1) o 'no': ${Reset}")" option
                    
                    if [ "$option" = "1" ]; then
                        check_termux_api || continue
                        echo "termux-fingerprint" > "login_method.txt"
                        success "✓ Método configurado"
                        return 0
                    elif [ "$option" = "no" ]; then
                        echo "no" > "login_method.txt"
                        success "✓ Método desactivado"
                        return 0
                    else
                        error "Opción no válida"
                        continue
                    fi
                done
                ;;
            no)
                echo "no" > "login_method.txt"
                success "✓ Método desactivado"
                return 0
                ;;
            n) return 0 ;;
            *) error "Opción no válida. Use 'y', 'n' o 'no'" ;;
        esac
    done
}

main() {
    cd ~/Stellar/config/system || {
        error "Error: No se pudo acceder al directorio"
        exit 1
    }

    configure_user || exit 1
    configure_auth || exit 1

    echo -e "\n${Verde_Brillante}Configuración completada${Reset}"
    read -p "$(echo -e "${Amarillo}Presione Enter para continuar...${Reset}")"
}

main