cp ~/Stellar/config/.bashrc ~/.

preexec() {
    printf "${gris}[INFO] ${blanco}Ejecutando comando: $1"
    echo

}

if [ -n "$BASH_VERSION" ]; then
    trap 'preexec "$BASH_COMMAND"' DEBUG
fi