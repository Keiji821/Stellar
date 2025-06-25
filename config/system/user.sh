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

if [ ! -f "user.txt" ]; then
    while true; do
        echo -e "${Verde_Brillante}No tiene un usuario configurado ¿Desea configurarlo? (y/n):${Reset}"
        read -p "" response_user

        case $response_user in
            [yY])
                while true; do
                    echo -e "${Verde_Brillante}Ingrese un nombre de usuario:${Reset}"
                    read -p "" response_user_config
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
if [ ! -f "login_method.txt" ]; then
    while true; do
        echo -e "${Verde_Brillante}No tiene un método de bloqueo configurado"
        echo -e "¿Desea configurar uno? (y/n/no para desactivar):${Reset}"
        read -p "" login_method_response
        login_method_response=$(echo "$login_method_response" | tr '[:upper:]' '[:lower:]')

        case $login_method_response in
            y)
                while true; do
                    echo
                    echo -e "${Negrita}${Verde}Métodos disponibles:${Reset}"
                    echo -e "${Verde}1. Huella dactilar (requiere termux-api)${Reset}"
                    echo -e "${Rojo}ADVERTENCIA: Si procede con este método, su Termux podría tener comportamiento inesperado${Reset}"
                    echo
                    echo -e "${Verde_Brillante}Seleccione un método (1) o 'no' para desactivar:${Reset}"
                    read -p "" login_method_response_list

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