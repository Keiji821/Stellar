command cp ~/Stellar/termux/lang_es/config/.bashrc ~/.

preexec() {
    printf "${Gris}[INFO] ${Blanco_Brillante}Ejecutando comando: $1"
    echo

}

if [ -n "$BASH_VERSION" ]; then
    trap 'preexec "$BASH_COMMAND"' DEBUG
fi
