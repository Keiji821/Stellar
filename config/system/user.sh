#!/bin/bash

Gris="\033[1;30m"
Rojo="\033[0;31m"
Verde="\033[0;32m"
Amarillo="\033[0;33m"
Azul="\033[0;34m"
Magenta="\033[0;35m"
Cian="\033[0;36m"
Blanco="\033[0;37m"
Verde_Brillante="\033[1;32m"
Rojo_Brillante="\033[1;31m"
Reset="\033[0m"
Negrita="\033[1m"
Subrayado="\033[4m"

if [ "$user" == "Stellar" ]; then
    while true; do
        read -p "${Verde_Brillante}No tiene un usuario configurado\n¿Desea configurarlo? (y/n): ${Reset}" response_user
        
        case $response_user in
            [yY])
                while true; do
                    read -p "${Verde_Brillante}Ingrese un nombre de usuario: ${Reset}" response_user_config
                    response_user_config=$(echo "$response_user_config" | tr -d '[:space:]')
                    
                    if [ -z "$response_user_config" ]; then
                        echo -e "${Rojo_Brillante}Error: No se puede dejar en blanco. Intente de nuevo.${Reset}"
                        continue
                    fi
                    
                    if echo "$response_user_config" > "user.txt"; then
                        echo -e "${Verde_Brillante}✓ Usuario configurado correctamente${Reset}"
                        break
                    else
                        echo -e "${Rojo_Brillante}Error al guardar el usuario${Reset}"
                        continue
                    fi
                done
                break
                ;;
            [nN])
                break
                ;;
            *)
                echo -e "${Rojo_Brillante}Error: Opción no válida. Por favor ingrese 'y' o 'n'.${Reset}"
                ;;
        esac
    done
fi

# Configuración de método de bloqueo
if [ -z "$login_method" ]; then
    while true; do
        read -p "${Verde_Brillante}No tiene un método de bloqueo\n¿Desea configurar uno? (y/n/no para desactivar): ${Reset}" login_method_response
        login_method_response=$(echo "$login_method_response" | tr '[:upper:]' '[:lower:]')
        
        case $login_method_response in
            y)
                while true; do
                    echo -e "${Negrita}${Verde}Métodos disponibles:${Reset}"
                    echo -e "${Verde}1. Huella dactilar${Reset}"
                    read -p "${Verde_Brillante}Seleccione un método (1) o 'no' para desactivar: ${Reset}" login_method_response_list
                    
                    if [ "$login_method_response_list" == "1" ]; then
                        method="termux-fingerprint"
                        break
                    elif [ "$login_method_response_list" == "no" ]; then
                        method="no"
                        break
                    else
                        echo -e "${Rojo_Brillante}Error: Opción no válida. Intente nuevamente.${Reset}"
                        continue
                    fi
                done
                
                if echo "$method" > "login_method.txt"; then
                    if [ "$method" == "no" ]; then
                        echo -e "${Verde_Brillante}✓ Método de desbloqueo desactivado${Reset}"
                    else
                        echo -e "${Verde_Brillante}✓ Método de desbloqueo configurado correctamente${Reset}"
                    fi
                    break
                else
                    echo -e "${Rojo_Brillante}Error al guardar el método${Reset}"
                    continue
                fi
                ;;
            n)
                break
                ;;
            no)
                echo "no" > "login_method.txt"
                echo -e "${Verde_Brillante}✓ Método de desbloqueo desactivado${Reset}"
                break
                ;;
            *)
                echo -e "${Rojo_Brillante}Error: Opción no válida. Por favor ingrese 'y', 'n' o 'no'.${Reset}"
                ;;
        esac
    done
fi