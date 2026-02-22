translate() {
    local value=$1
    local lang=$(cat ~/Stellar/configs/selected_lang.txt)
    awk -F': ' -v clave="$value" '$1==clave {print $2}' ~/Stellar/langs/"$lang".yml
}

execute_command_message=$(translate execute_command_message)

eval "execute_command_message=\"$execute_command_message\""


command cp ~/Stellar/termux/system/.bashrc ~/.

preexec() {
    printf "${Gris}[INFO] ${Blanco_Brillante}$execute_command_message: $1"
    echo

}

if [ -n "$BASH_VERSION" ]; then
    trap 'preexec "$BASH_COMMAND"' DEBUG
fi

source .bashrc