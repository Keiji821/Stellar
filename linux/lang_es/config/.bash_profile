command cp ~/Stellar/linux/lang_es/config/.bashrc ~/.
source venv/bin/activate

if [ -n "$PS1" ]; then

preexec() {
    printf "${Gris}[INFO] ${Blanco_Brillante}Ejecutando comando: $1"
    echo
}

if [ -n "$BASH_VERSION" ]; then
    trap 'preexec "$BASH_COMMAND"' DEBUG
fi

fi

if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi