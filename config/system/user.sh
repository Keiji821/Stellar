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
    sleep 2
}

success() {
    echo -e "${Verde_Brillante}$1${Reset}"
    sleep 1
}

check_termux_api() {
    if ! pkg list-installed | grep -q 'termux-api'; then
        error "Termux-API no está instalado. Instálelo con: pkg install termux-api"
        return 1
    fi
    return 0
}


configure_user() {
    if [ -f "user.txt" ]; then
        return 0
    fi

    while true; do
        echo -e "${Verde_Brillante}No tiene un usuario configurado"
        read -p "¿Desea configurarlo? (y/n): ${Reset}" response_user

        case $response_user in
            [yY]*)
                while true; do
                    read -p "$(echo -e ${Verde_Brillante}Ingrese un nombre de usuario: ${Reset})" response_user_config
                    response_user_config=$(echo "$response_user_config" | xargs)  # Trim spaces
                    
                    if [ -z "$response_user_config" ]; then
                        error "Error: No se puede dejar en blanco. Intente de nuevo."
                        continue
                    fi
                    
                    if echo "$response_user_config" > "user.txt"; then
                        success "✓ Usuario configurado correctamente"
                        return 0
                    else
                        error "Error al guardar el usuario"
                        continue
                    fi
                done
                ;;
            [nN]*)
                return 0
                ;;
            *)
                error "Error: Opción no válida. Por favor ingrese 'y' o 'n'."
                ;;
        esac
    done
}

configure_auth() {
    if [ -f "login_method.txt" ]; then
        return 0
    fi

    while true; do
        echo -e "${Verde_Brillante}No tiene un método de bloqueo configurado"
        read -p "¿Desea configurar uno? (y/n/no para desactivar): ${Reset}" login_method_response
        login_method_response=$(echo "$login_method_response" | tr '[:upper:]' '[:lower:]')

        case $login_method_response in
            y)
                while true; do
                    echo -e "\n${Negrita}${Verde}Métodos disponibles:${Reset}"
                    echo -e "${Verde}1. Huella dactilar${Reset}"
                    echo -e "${Rojo}ADVERTENCIA: Requiere Termux-API instalado${Reset}"
                    read -p "$(echo -e ${Verde_Brillante}Seleccione un método (1) o escribe no para desactivar: ${Reset})" login_method_response_list

                    if [ "$login_method_response_list" == "1" ]; then

                        if ! check_termux_api; then
                            continue
                        fi
                        method="termux-fingerprint"
                        break
                    elif [ "$login_method_response_list" == "no" ]; then
                        method="no"
                        break
                    else
                        error "Error: Opción no válida. Intente nuevamente."
                        continue
                    fi
                done

                
                if echo "$method" > "login_method.txt"; then
                    if [ "$method" == "no" ]; then
                        success "✓ Método de desbloqueo desactivado"
                    else
                        success "✓ Método de desbloqueo configurado correctamente"
                    fi
                    return 0
                else
                    error "Error al guardar el método"
                    continue
                fi
                ;;
            n)
                return 0
                ;;
            no)
                if echo "no" > "login_method.txt"; then
                    success "✓ Método de desbloqueo desactivado"
                    return 0
                else
                    error "Error al desactivar el método"
                    continue
                fi
                ;;
            *)
                error "Error: Opción no válida. Por favor ingrese 'y', 'n' o 'no'."
                ;;
        esac
    done
}

main() {
    cd ~/Stellar/config/system || {
        error "Error: No se pudo acceder al directorio ~/Stellar/config/system"
        exit 1
    }

    configure_user

    configure_auth

    echo -e "\n${Verde_Brillante}Configuración completada. Presione Enter para continuar...${Reset}"
    read
}

main