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
    echo -e "${Rojo_Brillante}✖ $1${Reset}"
    sleep 1
}

exito() {
    echo -e "${Verde_Brillante}✓ $1${Reset}"
    sleep 0.7
}

pregunta() {
    echo -e "${Amarillo_Brillante}? $1${Reset}"
}

informacion() {
    echo -e "${Azul_Brillante}→ $1${Reset}"
}

verificar_termux_api() {
    pkg list-installed | grep -q 'termux-api' || {
        error "Termux-API no está instalado"
        informacion "Instale con: pkg install termux-api"
        return 1
    }
    return 0
}

configurar_usuario() {
    if [ -f "user.txt" ]; then
        usuario_actual=$(cat user.txt)
        if [ "$usuario_actual" = "Stellar" ]; then
            error "No tiene un usuario configurado"
            configurar_nuevo_usuario
        else
            pregunta "Usuario actual: $usuario_actual"
            read -p "$(echo -e "${Amarillo_Brillante}¿Reemplazar usuario? (s/n): ${Reset}")" respuesta
            [[ "$respuesta" =~ ^[Ss]$ ]] && configurar_nuevo_usuario || informacion "Usuario no modificado"
        fi
    else
        error "No tiene un usuario configurado"
        configurar_nuevo_usuario
    fi
}

configurar_nuevo_usuario() {
    while true; do
        read -p "$(echo -e "${Amarillo_Brillante}Ingrese nuevo usuario: ${Reset}")" nuevo_usuario
        nuevo_usuario=$(echo "$nuevo_usuario" | xargs)
        [ -z "$nuevo_usuario" ] && error "Nombre vacío no permitido" && continue
        echo "$nuevo_usuario" > "user.txt" && exito "Usuario configurado" && break || error "Error al guardar"
    done
}

configurar_autenticacion() {
    if [ -f "login_method.txt" ]; then
        metodo_actual=$(cat login_method.txt)
        if [ "$metodo_actual" = "no" ]; then
            error "No tiene método de desbloqueo"
            configurar_nuevo_metodo
        else
            [ "$metodo_actual" = "termux-fingerprint" ] && metodo="Huella digital" || metodo="Desconocido"
            pregunta "Método actual: $metodo"
            read -p "$(echo -e "${Amarillo_Brillante}¿Reemplazar método? (s/n): ${Reset}")" respuesta
            [[ "$respuesta" =~ ^[Ss]$ ]] && configurar_nuevo_metodo || informacion "Método no modificado"
        fi
    else
        error "No tiene método de desbloqueo"
        configurar_nuevo_metodo
    fi
}

configurar_nuevo_metodo() {
    while true; do
        echo -e "\n${Cian_Brillante}Opciones:"
        echo -e " ${Verde_Brillante}1) Huella digital"
        echo -e " ${Verde_Brillante}2) Desactivar protección${Reset}"
        
        read -p "$(echo -e "${Amarillo_Brillante}Seleccione [1-2]: ${Reset}")" opcion
        
        case "$opcion" in
            1)
                verificar_termux_api && echo "termux-fingerprint" > "login_method.txt" && exito "Huella activada" && break
                ;;
            2)
                echo "no" > "login_method.txt" && exito "Protección desactivada" && break
                ;;
            *)
                error "Opción inválida"
                ;;
        esac
    done
}

menu_principal() {
    while true; do
        clear
        echo -e "${Blanco_Brillante}${Negrita}${Fondo_Azul} CONFIGURACIÓN STELLAR ${Reset}\n"
        
        [ -f "user.txt" ] && echo -e "${Magenta_Brillante}Usuario: ${Blanco_Brillante}$(cat user.txt)${Reset}"
        [ -f "login_method.txt" ] && {
            metodo=$(cat login_method.txt)
            [ "$metodo" = "termux-fingerprint" ] && estado="${Verde_Brillante}Huella activada" || estado="${Amarillo_Brillante}Protección desactivada"
            echo -e "${Magenta_Brillante}Seguridad: ${estado}${Reset}"
        }
        
        echo -e "\n${Cian_Brillante}Menú:"
        echo -e " ${Verde_Brillante}1) Configurar usuario"
        echo -e " ${Verde_Brillante}2) Configurar seguridad"
        echo -e " ${Verde_Brillante}3) Probar sistema"
        echo -e " ${Verde_Brillante}4) Salir${Reset}"
        
        read -p "$(echo -e "\n${Amarillo_Brillante}Seleccione opción [1-4]: ${Reset}")" opcion
        
        case "$opcion" in
            1) configurar_usuario ;;
            2) configurar_autenticacion ;;
            3)
                if [ -f "login_method.txt" ] && [ "$(cat login_method.txt)" = "termux-fingerprint" ]; then
                    echo -e "\n${Amarillo_Brillante}Probando autenticación...${Reset}"
                    termux-fingerprint && exito "Autenticación exitosa" || error "Autenticación fallida"
                    read -p "$(echo -e "${Amarillo_Brillante}Presione Enter...${Reset}")"
                else
                    error "Método de huella no configurado"
                    sleep 1.5
                fi
                ;;
            4) 
                echo -e "\n${Verde_Brillante}Saliendo del sistema...${Reset}"
                exit 0
                ;;
            *) 
                error "Opción no válida"
                sleep 1
                ;;
        esac
    done
}

inicio() {
    clear
    echo -e "${Blanco_Brillante}${Negrita}${Fondo_Magenta} INICIO DEL SISTEMA STELLAR ${Reset}\n"
    
    [ ! -f "user.txt" ] && error "No tiene usuario configurado" && configurar_usuario
    [ ! -f "login_method.txt" ] && error "No tiene método de autenticación" && configurar_autenticacion
    
    sleep 1.2
    menu_principal
}

inicio