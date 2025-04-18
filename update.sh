#!/bin/bash

update_repo() {
if! git pull --force; then
exit 1
fi
}

show_lolcat_message() {
local message="$1"
local delay="${2:-20}"
printf "$message
" | lolcat -a -d "$delay"
}

show_lolcat_message "Actualizando..."
update_repo
show_lolcat_message "¡Todo actualizado!"