command cp ~/Stellar/linux/lang_es/config/.bashrc ~/.
source venv/bin/activate

preexec() {
    printf "${Gris}[INFO] ${Blanco_Brillante}Ejecutando comando: $1"
    echo

}

if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

if [ -n "$BASH_VERSION" ]; then
    trap 'preexec "$BASH_COMMAND"' DEBUG
fi
