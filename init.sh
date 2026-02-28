#!/bin/bash

export Gris="\033[1;30m"
export Negro="\033[0;30m"
export Rojo="\033[0;31m"
export Verde="\033[0;32m"
export Amarillo="\033[0;33m"
export Azul="\033[0;34m"
export Magenta="\033[0;35m"
export Cian="\033[0;36m"
export Blanco="\033[0;37m"

export Negro_Brillante="\033[1;30m"
export Rojo_Brillante="\033[1;31m"
export Verde_Brillante="\033[1;32m"
export Azul_Brillante="\033[1;34m"
export Magenta_Brillante="\033[1;35m"
export Amarillo_Brillante="\033[1;33m"
export Cian_Brillante="\033[1;36m"
export Blanco_Brillante="\033[1;37m"

export Fondo_Negro="\033[40m"
export Fondo_Rojo="\033[41m"
export Fondo_Verde="\033[42m"
export Fondo_Amarillo="\033[43m"
export Fondo_Azul="\033[44m"
export Fondo_Magenta="\033[45m"
export Fondo_Cian="\033[46m"
export Fondo_Blanco="\033[47m"

export Fondo_Negro_Brillante="\033[0;100m"
export Fondo_Rojo_Brillante="\033[0;101m"
export Fondo_Verde_Brillante="\033[0;102m"
export Fondo_Amarillo_Brillante="\033[0;103m"
export Fondo_Azul_Brillante="\033[0;104m"
export Fondo_Magenta_Brillante="\033[0;105m"
export Fondo_Cian_Brillante="\033[0;106m"
export Fondo_Blanco_Brillante="\033[0;107m"

export Reset="\033[0m"
export Negrita="\033[1m"
export Atenuado="\033[2m"
export Italico="\033[3m"
export Subrayado="\033[4m"
export Parpadeo="\033[5m"
export Invertido="\033[7m"
export Oculto="\033[8m"
export Tachado="\033[9m"

export stellar_banner="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣶⠶⣶⣶⣶⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Stellar⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⢟⣵⣿⡿⠛⠛⠛⠛⠛⠻⠿⣷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣼⣿⠏⢠⣾⣿⣿⣿⣿⣿⣷⣶⣬⣝⡛⢷⣦⣄⠀⠀⠀⠀⣀⣤⢤⣴⣶⡶⠛⣛⢫⣿⣶⣾⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⢻⢻⣿⠀⣿⣿⣿⡿⣭⣶⠾⠟⠺⠿⢿⣿⣷⣦⠝⣫⡴⢺⣿⢿⡇⢻⣿⢿⣧⠀⢿⣮⡿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⡏⣾⣿⡄⢻⣿⣿⢱⣿⠁⡔⠋⠉⠉⠐⠀⣩⡴⠋⢹⠁⢸⣿⣜⢿⡌⢻⣦⣿⣷⣄⠙⠦⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⡸⣿⣷⠈⣿⣿⣟⣿⠀⠀⠀⠀⠀⣠⣾⣇⠀⠀⠈⠀⠸⣿⣿⣿⣾⡢⠙⠻⣿⣿⣿⣦⣈⠙⠛⠿⢶⣭⣍⠉⠯⠭⠔⠃⠈⣻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣇⢻⣿⣇⠸⣿⣿⣿⡀⠇⠀⠀⡼⣿⣿⡇⠀⠀⠀⡀⠀⠻⣟⢿⣿⣿⣤⡀⠘⢿⣿⣿⣿⣿⣤⣄⣀⠀⠀⠀⠠⠄⠀⣀⣠⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣇⠻⣿⣄⠻⣿⣿⣷⡈⠀⠞⡁⣿⡜⣿⣶⢦⠀⠐⠀⠀⠙⢮⡛⢿⣿⣿⣷⣦⣌⡙⠻⢿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⡿⡩⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢧⣭⠡⣤⢿⣿⣟⣷⡀⠀⢧⣻⡇⠘⣿⣟⡇⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⢿⣿⣿⣷⣤⣈⠙⠿⠿⣿⣿⣿⣥⣯⣤⣾⡿⠚⠁⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢻⣷⡉⣤⠻⣿⣿⣿⣄⠈⣿⡿⡌⢾⣿⣧⡀⠀⠀⡀⠀⠀⠀⠀⠀⠙⠷⣮⣙⠛⠿⣿⣿⣿⣿⣿⣿⣿⠿⠟⣋⡀⠀⠀⠁⣠⣾⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⡄⣒⠈⣿⣯⡻⣦⡈⢻⣎⠈⠻⣿⣿⣦⣄⠈⠢⣤⡀⠀⠀⠀⠀⠀⢌⡙⠒⠀⠈⠙⠛⠛⠛⠛⠛⠉⣠⣤⣦⣤⣤⣿⠟⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣧⡈⢿⣿⣝⢷⣄⠙⢧⡀⣈⠻⣿⣿⣵⠀⠈⠛⠦⡀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⣠⢤⣦⣄⣸⣿⡿⣫⣽⣿⣯⠟⠀⣸⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡄⠻⣿⣄⠙⣿⣷⡹⣦⡈⠻⣿⣷⡌⠙⢿⣷⣦⣀⠂⢄⣀⡀⠀⠀⠀⡉⠲⠶⠶⠟⠻⠿⣷⣾⣿⣿⣱⠟⠉⠉⠐⢀⣴⢯⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠱⠀⠈⠻⣷⣌⠻⣿⣮⡻⣦⡈⠻⣿⣦⡈⠻⢿⣿⣿⣶⣍⣙⠷⠾⣿⣿⣷⣶⣶⣾⣿⠿⠿⠋⡩⠽⠛⠒⠁⠀⢀⣨⣴⢏⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⠁⠀⠀⠉⢿⣧⡈⠻⣿⣮⡻⣦⡈⠻⣿⣦⣕⡿⢿⣶⣭⣉⡛⠒⠦⠄⠉⠉⠑⠛⠻⠗⠒⠀⢀⣤⠶⢀⣴⡾⣿⠟⣡⠏⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣦⡀⠀⠀⠀⠙⢛⣦⡈⠻⣷⣎⡻⣦⡈⠻⣿⣿⣶⣯⣝⣿⣿⣿⣖⣲⣶⣤⣤⣤⣄⣤⣤⣴⣶⣶⣶⠻⣉⣠⡴⠟⠁⡰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢷⠻⣯⢦⠀⠀⠀⠀⠙⢿⣦⡈⠻⣿⣮⡻⣦⣀⠙⠪⠝⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣻⣿⣿⣷⠿⢛⠉⠀⠀⠈⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡎⢇⢻⣿⣇⠘⠆⠱⢄⠀⠙⢿⣦⣈⠻⣿⣮⣛⣷⣄⠑⠶⣶⣦⣐⣮⣽⣿⣿⣿⣯⣶⣾⠻⡿⢟⡹⠃⠀⢁⠀⠀⠀⣠⣶⠇⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠈⠢⡙⢿⢷⣤⣄⡀⠑⠠⡀⠛⢿⣷⣌⠛⢿⣷⣝⢿⣦⡈⠙⠛⠛⠛⠒⠒⠂⠀⠀⠈⠛⠛⠉⡠⠒⡉⠉⣦⣴⡴⠋⡾⣀⢿⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠹⡀⠙⠲⣬⣛⢦⡀⠀⠀⠀⠈⠻⣷⣄⠙⠻⣿⣮⡻⣶⣄⡉⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠰⠏⢂⣼⠟⠋⠀⣼⢡⣿⣦⠻⣮⣳⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣯⠀⠀⢀⠰⣤⠙⣿⣷⣤⣀⠀⠀⠀⠀⠉⢳⣶⣌⠻⢿⣷⣽⡿⣦⣄⠀⠀⠀⣀⣠⣤⣤⣥⡴⣾⠿⠒⠁⣠⣾⠃⢂⢻⣿⣧⡙⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠈⠢⣙⢷⡜⢧⡉⠛⠿⣦⡀⠀⢄⠈⠛⢧⡷⢆⡙⠻⣿⣿⣿⣿⣦⣄⡉⠉⠉⠉⠀⠈⠀⣠⠴⠋⡴⠁⠀⠀⡄⣿⣿⣧⠘⣿⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡄⠀⠀⠉⠁⠀⠙⣦⠀⠂⡍⠑⠀⠉⠀⠀⠉⢻⠓⣶⡄⠈⠹⣿⣿⣿⣿⣶⣤⠀⠀⠐⠉⠀⢠⡞⠁⠀⠀⠀⡇⢸⣿⡟⣧⢱⢸⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠂⠀⠀⠀⠀⠀⠀⠛⢿⣿⣷⡽⡢⠙⢿⣿⣿⣿⣶⣤⣀⠀⠬⢄⣀⣀⣠⠔⢁⣾⣿⠇⣰⡄⢿⢀⡏⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡈⠐⠠⣑⠢⢤⣄⣀⠁⠒⠒⠲⠦⠄⠀⠀⠀⠈⠛⢿⣷⣦⣌⠛⢿⣾⣿⣻⣿⣿⣿⣶⣦⡤⠤⠒⣐⣴⣿⡏⣿⡇⢸⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⡀⠉⠓⠢⣭⣿⣷⣶⣾⣿⣟⣛⣓⣀⣀⣀⣠⡌⠙⠻⣿⣦⣤⠙⠛⠿⣶⣭⣿⣛⡿⠿⠿⠿⠟⣫⣾⡿⠁⣼⡿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠦⣤⣀⠀⠉⠉⠉⠀⠀⠉⠉⠉⠍⠀⠀⣀⣤⠴⠀⠉⠛⠂⢿⣷⣦⣌⣙⠛⠻⠿⠿⠿⠷⠙⠛⢁⣴⣿⣷⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠒⠲⠒⠶⠒⠒⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⢿⣿⣶⣶⣶⣶⣶⡿⠿⣿⡿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠉⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                                   @By Keiji821"""

translate() {
    local value=$1
    local lang=$(cat ~/Stellar/configs/selected_lang.txt)
    awk -F': ' -v clave="$value" '$1==clave {print $2}' ~/Stellar/langs/"$lang".yml
}

command_not_found_message=$(translate command_not_found_message)
execute_command_message=$(translate execute_command_message)
install_message=$(translate install_message)
reinstall_message=$(translate reinstall_message)
update_message=$(translate update_message)
exit_message=$(translate exit_message)
input_message=$(translate input_message)
info_message=$(translate info_message)
cache_clear_message=$(translate cache_clear_message)
solve_problems_message=$(translate solve_problems_message)
verify_packages_message=$(translate verify_packages_message)
invalid_data_message=$(translate invalid_data_message)
reset_message=$(translate reset_message)
verify_message=$(translate verify_message)
success_verify_message=$(translate success_verify_message)
installing_dependencies_message=$(translate installing_dependencies_message)
success_installing_dependencies_message=$(translate success_installing_dependencies_message)
on_message=$(translate on_message)
prepare_install_message=$(translate prepare_install_message)
init_install_message=$(translate init_install_message)
install_alert_message=$(translate install_alert_message)
success_install_message=$(translate success_install_message)
on_install_message=$(translate on_install_message)
package_install_message=$(translate package_install_message)
failed_install_message=$(translate failed_install_message)
success_install_package_message=$(translate success_install_package_message)
success_apply_configs_message=$(translate success_apply_configs_message)
on_stellar_message=$(translate on_stellar_message)
update_action_message=$(translate update_action_message)
success_update_message=$(translate success_update_message)
cache_clear_action_message=$(translate cache_clear_action_message)
success_cache_clear_message=$(translate success_cache_clear_message)
info_descr_message=$(translate info_descr_message)
execute_solve_problems_message=$(translate execute_solve_problems_message)
success_solve_problems_message=$(translate success_solve_problems_message)

eval "command_not_found_message=\"$command_not_found_message\""
eval "execute_command_message=\"$execute_command_message\""
eval "install_message=\"$install_message\""
eval "reinstall_message=\"$reinstall_message\""
eval "update_message=\"$update_message\""
eval "exit_message=\"$exit_message\""
eval "input_message=\"$input_message\""
eval "info_message=\"$info_message\""
eval "cache_clear_message=\"$cache_clear_message\""
eval "solve_problems_message=\"$solve_problems_message\""
eval "verify_packages_message=\"$verify_packages_message\""
eval "invalid_data_message=\"$invalid_data_message\""
eval "reset_message=\"$reset_message\""
eval "verify_message=\"$verify_message\""
eval "success_verify_message=\"$success_verify_message\""
eval "installing_dependencies_message=\"$installing_dependencies_message\""
eval "success_installing_dependencies_message=\"$success_installing_dependencies_message\""
eval "on_message=\"$on_message\""
eval "prepare_install_message=\"$prepare_install_message\""
eval "init_install_message=\"$init_install_message\""
eval "install_alert_message=\"$install_alert_message\""
eval "success_install_message=\"$success_install_message\""
eval "on_install_message=\"$on_install_message\""
eval "package_install_message=\"$package_install_message\""
eval "failed_install_message=\"$failed_install_message\""
eval "success_install_package_message=\"$success_install_package_message\""
eval "success_apply_configs_message=\"$success_apply_configs_message\""
eval "on_stellar_message=\"$on_stellar_message\""
eval "update_action_message=\"$update_action_message\""
eval "success_update_message=\"$success_update_message\""
eval "cache_clear_action_message=\"$cache_clear_action_message\""
eval "success_cache_clear_message=\"$success_cache_clear_message\""
eval "info_descr_message=\"$info_descr_message\""
eval "execute_solve_problems_message=\"$execute_solve_problems_message\""
eval "success_solve_problems_message=\"$success_solve_problems_message\""

apt_packages=(
    python
    tor 
    exiftool 
    nmap 
    dnsutils 
    nodejs 
    lsd
)
pip_packages=(
    setuptools
    beautifulsoup4
    pyfiglet
    phonenumbers
    psutil
    PySocks
    requests
    rich
    "rich[jupyter]"
    lolcat
    discord
    fake_useragent
    pycryptodome
)

install() {
    printf "\a\n${Cian_Brillante} ! ${Reset} ${prepare_install_message}\n"
    sleep 2
    cd ~/Stellar/resources/libraries/stellar-package-translate
    pip install setuptools && pip install . > stellar_verify.log
    wait
    cd $HOME
    if [[ -d ".termux" ]]; then
        printf "\a\n${Cian_Brillante} ! ${Reset} ${on_install_message}\n"
        for package in $apt_packages; do
            printf "\a\n${Amarillo_Brillante}   > ${Reset} ${package_install_message}: ${Subrayado}${package}${Reset}\n"
            sleep 1
            apt-get install $package -y > stellar_verify.log
            wait
            verify=$(dpkg --get-selections | grep -v deinstall | grep $package | awk '{print $1}')
            if [[ $verify =~ $package ]]; then
                printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_install_message}: ${Subrayado}${package}${Reset}\n"
            else
                printf "\a\n${Rojo_Brillante}   X ${Reset} ${failed_install_message}: ${Subrayado}${package}${Reset}\n"
            fi
            for package in $pip_packages; do
                pip install $package > stellar_verify.log
                wait
                verify=$(pip list | grep -i "^$package " | awk '{print $1}')
                if [[ $verify =~ ^$package$ ]]; then
                    printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_install_message}: ${Subrayado}${package}${Reset}\n"
                else
                    printf "\a\n${Rojo_Brillante}   X ${Reset} ${failed_install_message}: ${Subrayado}${package}${Reset}\n"
                fi
            done
        done
        platform="termux"
    else
        printf "\a\n${Cian_Brillante} ! ${Reset} ${on_install_message}\n"
        for package in $apt_packages; do
            printf "\a\n${Amarillo_Brillante}   > ${Reset} ${package_install_message}: ${Subrayado}${package}${Reset}\n"
            sleep 1
            apt-get install $package -y > stellar_verify.log
            wait
            verify=$(dpkg --get-selections | grep -v deinstall | grep $package | awk '{print $1}')
            if [[ $verify =~ $package ]]; then
                printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_install_message}: ${Subrayado}${package}${Reset}\n"            
            else
                printf "\a\n${Rojo_Brillante}   X ${Reset} ${failed_install_message}: ${Subrayado}${package}${Reset}\n"
            fi
            for package in $pip_packages; do
                pip install $package > stellar_verify.log
                wait
                verify=$(pip list | grep -i "^$package " | awk '{print $1}')
                if [[ $verify =~ ^$package$ ]]; then
                    printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_install_message}: ${Subrayado}${package}${Reset}\n"
                else
                    printf "\a\n${Rojo_Brillante}   X ${Reset} ${failed_install_message}: ${Subrayado}${package}${Reset}\n"
                fi
            done            
        done
    fi   

    if [[ $platform == "termux" ]]; then
        printf "\a\n${Amarillo_Brillante}   ! ${Reset} Aplicando configuraciones...\n"
        command cp ~/Stellar/termux/system/.bashrc ~/
        command cp ~/Stellar/termux/system/.bash_profile ~/
        command cp ~/Stellar/resources/fonts/fira-mono/font.ttf ~/.termux
        theme=$(cat ~/Stellar/resources/themes/stellar.stel)
        echo $theme > ~/.termux/color.properties
        termux-reload-settings
        printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_apply_configs_message}\n"
    else
        printf "\a\n${Amarillo_Brillante}   ! ${Reset} Aplicando configuraciones...\n"
        command cp ~/Stellar/linux/system/.bashrc ~/
        command cp ~/Stellar/linux/system/.bash_profile ~/
        source ~/Stellar/resources/themes/stellar.stel
        echo -en "\033]11;${background}\007"
        echo -en "\033]10;${foreground}\007"
        echo -en "\033]4;0;${color0}\007"
        echo -en "\033]4;1;${color1}\007"
        echo -en "\033]4;2;${color2}\007"
        echo -en "\033]4;3;${color3}\007"
        echo -en "\033]4;4;${color4}\007"
        echo -en "\033]4;5;${color5}\007"
        echo -en "\033]4;6;${color6}\007"
        echo -en "\033]4;7;${color7}\007"
        echo -en "\033]4;8;${color8}\007"
        echo -en "\033]4;9;${color9}\007"
        echo -en "\033]4;10;${color10}\007"
        echo -en "\033]4;11;${color11}\007"
        echo -en "\033]4;12;${color12}\007"
        echo -en "\033]4;13;${color13}\007"
        echo -en "\033]4;14;${color14}\007"
        echo -en "\033]4;15;${color15}\007"
        printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_apply_configs_message}\n"
    fi
    printf "\a\n${Verde_Brillante} ✓ ${Reset} ${success_install_message}\n" 
    printf "\a\n${Cian_Brillante} ! ${Reset} ${on_stellar_message}\n"  
    sleep 2
    bash
}

reinstall () {
    printf "${Cian_Brillante} ! ${Reset} $verify_message"
    sleep 2
    cd ~/Stellar/resources/libraries/stellar-package-translate
    pip install setuptools && pip install . > stellar_verify.log
    wait
    cd $HOME
    if [[ -d ".termux" ]]; then
        printf "\a\n${Cian_Brillante} ! ${Reset} ${on_install_message}\n"
        for package in $apt_packages; do
            printf "\a\n${Amarillo_Brillante}   > ${Reset} ${package_install_message}: ${Subrayado}${package}${Reset}\n"
            sleep 1
            apt-get install $package -y > stellar_verify.log
            wait
            verify=$(dpkg --get-selections | grep -v deinstall | grep $package | awk '{print $1}')
            if [[ $verify =~ $package ]]; then
                printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_install_message}: ${Subrayado}${package}${Reset}\n"
            else
                printf "\a\n${Rojo_Brillante}   X ${Reset} ${failed_install_message}: ${Subrayado}${package}${Reset}\n"
            fi    
            for package in $pip_packages; do
                pip install $package > stellar_verify.log
                wait
                verify=$(pip list | grep -i "^$package " | awk '{print $1}')
                if [[ $verify =~ ^$package$ ]]; then
                    printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_install_message}: ${Subrayado}${package}${Reset}\n"
                else
                    printf "\a\n${Rojo_Brillante}   X ${Reset} ${failed_install_message}: ${Subrayado}${package}${Reset}\n"
                fi
            done       
        done     
        platform="termux"
    else
        printf "\a\n${Cian_Brillante} ! ${Reset} ${on_install_message}\n"
        for package in $apt_packages; do
            printf "\a\n${Amarillo_Brillante}   > ${Reset} ${package_install_message}: ${Subrayado}${package}${Reset}\n"
            sleep 1
            apt-get install $package -y > stellar_verify.log
            wait
            verify=$(dpkg --get-selections | grep -v deinstall | grep $package | awk '{print $1}')
            if [[ $verify =~ $package ]]; then
                printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_install_message}: ${Subrayado}${package}${Reset}\n"            
            else
                printf "\a\n${Rojo_Brillante}   X ${Reset} ${failed_install_message}: ${Subrayado}${package}${Reset}\n"
            fi
            for package in $pip_packages; do
                pip install $package > stellar_verify.log
                wait
                verify=$(pip list | grep -i "^$package " | awk '{print $1}')
                if [[ $verify =~ ^$package$ ]]; then
                    printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_install_message}: ${Subrayado}${package}${Reset}\n"
                else
                    printf "\a\n${Rojo_Brillante}   X ${Reset} ${failed_install_message}: ${Subrayado}${package}${Reset}\n"
                fi
            done            
        done

    fi   

    if [[ $platform == "termux" ]]; then
        printf "\a\n${Amarillo_Brillante}   ! ${Reset} Aplicando configuraciones...\n"
        command cp ~/Stellar/termux/system/.bashrc ~/
        command cp ~/Stellar/termux/system/.bash_profile ~/
        command cp ~/Stellar/resources/fonts/fira-mono/font.ttf ~/.termux
        theme=$(cat ~/Stellar/resources/themes/stellar.stel)
        echo $theme > ~/.termux/color.properties
        termux-reload-settings
        printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_apply_configs_message}\n"
    else
        printf "\a\n${Amarillo_Brillante}   ! ${Reset} Aplicando configuraciones...\n"
        command cp ~/Stellar/linux/system/.bashrc ~/
        command cp ~/Stellar/linux/system/.bash_profile ~/
        source ~/Stellar/resources/themes/stellar.stel
        echo -en "\033]11;${background}\007"
        echo -en "\033]10;${foreground}\007"
        echo -en "\033]4;0;${color0}\007"
        echo -en "\033]4;1;${color1}\007"
        echo -en "\033]4;2;${color2}\007"
        echo -en "\033]4;3;${color3}\007"
        echo -en "\033]4;4;${color4}\007"
        echo -en "\033]4;5;${color5}\007"
        echo -en "\033]4;6;${color6}\007"
        echo -en "\033]4;7;${color7}\007"
        echo -en "\033]4;8;${color8}\007"
        echo -en "\033]4;9;${color9}\007"
        echo -en "\033]4;10;${color10}\007"
        echo -en "\033]4;11;${color11}\007"
        echo -en "\033]4;12;${color12}\007"
        echo -en "\033]4;13;${color13}\007"
        echo -en "\033]4;14;${color14}\007"
        echo -en "\033]4;15;${color15}\007"
        printf "\a\n${Verde_Brillante}   ✓ ${Reset} ${success_apply_configs_message}\n"
    fi
    printf "\a\n${Verde_Brillante} ✓ ${Reset} ${success_install_message}\n"
}

update() {
    printf "\a\n${Cian_Brillante} ! ${Reset} ${update_action_message}"
    git stash > stellar_verify.log 
    git pull > stellar_verify.log
    sleep 1
    printf "\a\n${Verde_Brillante} ✓ ${Reset} ${success_update_message}\n"
}

verify_packages () {
    printf "\a\n${Cian_Brillante} ! ${Reset} ${verify_message}"
    for package in $apt_packages; do 
        verify=$(dpkg --get-selections | grep -v deinstall | grep $package | awk '{print $1}')
        if [[ $verify =~ $package ]]; then
            printf "\a\n${Verde_Brillante} ✓ ${Reset} {success_verify_message}"
        else
            printf "\a\n${Cian_Brillante} ! ${Reset} ${installing_dependencies_message}...."
            for dependencie in $apt_packages; do
                apt-get install $dependencie > stellar_verify.log
                wait
            done
            printf "\a\n${Verde_Brillante} ✓ ${Reset} ${success_apply_configs_message}"
        fi
    done
}

cache_clear() {
    printf "\a\n${Cian_Brillante} ! ${Reset} ${cache_clear_action_message}"
    sleep 2
    apt-get autoclean > stellar_verify.log
    wait
    pip cache purge > stellar_verify.log
    wait 
    printf "\a\n${Verde_Brillante} ✓ ${Reset} ${success_cache_clear_message}\n"
}

solve_problems() {
    printf "${Cian_Brillante} ! ${Reset} ${execute_solve_problems_message}"
    if [[ -d ".termux" ]]; then
        pkg upgrade -y && pkg update -y > stellar_verify.log
        wait
        pkg autoclean > stellar_verify.log
        wait
        pip cache purge > stellar_verify.log
        wait
        pip list --outdated | awk 'NR>2 {print $1}' | xargs -n1 pip install -U
        wait
        reset
        wait
    else
        apt-get update -y && apt-get upgrade -y > stellar_verify.log
        wait
        apt-get autoremove > stellar_verify.log
        wait
        pip cache purge > stellar_verify.log
        wait
        pip list --outdated | awk 'NR>2 {print $1}' | xargs -n1 pip install -U
        wait
        reset
        wait
        pritf "${Verde_Brillante} ✓ ${Reset} ${success_solve_problems_message}"
    fi
}

info() {
    printf "${Subrayado}${info_descr_message}${Reset}"
}

banner() {
        printf "${Verde_Brillante}${stellar_banner}${Reset}\n"
        printf "\n"

        printf "\n${Cian_Brillante}╭──────────────────────────╮${Reset}\n"                         
        printf "${Cian_Brillante}│ ${Gris}[${Amarillo_Brillante}1${Gris}]${Reset} ${install_message}             ${Cian_Brillante}│\n"
        printf "${Cian_Brillante}│ ${Gris}[${Amarillo_Brillante}2${Gris}]${Reset} ${reinstall_message}           ${Cian_Brillante}│\n"
        printf "${Cian_Brillante}│ ${Gris}[${Amarillo_Brillante}3${Gris}]${Reset} ${update_message}           ${Cian_Brillante}│\n"
        printf "${Cian_Brillante}╰──────────────────────────╯${Reset}\n"

        printf "\n${Cian_Brillante}╭────────────────────────────────────────╮${Reset}\n"
        printf "${Cian_Brillante}│ ${Gris}[${Verde_Brillante}4${Gris}]${Reset} ${verify_packages_message}   ${Cian_Brillante}│\n"
        printf "${Cian_Brillante}│ ${Gris}[${Verde_Brillante}5${Gris}]${Reset} ${cache_clear_message}          ${Cian_Brillante}│\n"
        printf "${Cian_Brillante}│ ${Gris}[${Verde_Brillante}6${Gris}]${Reset} ${solve_problems_message}      ${Cian_Brillante}│\n"
        printf "${Cian_Brillante}│ ${Gris}[${Cian_Brillante}7${Gris}]${Reset} ${reset_message}                  ${Cian_Brillante}│\n"
        printf "${Cian_Brillante}│ ${Gris}[${Cian_Brillante}8${Gris}]${Reset} ${info_message}                        ${Cian_Brillante}│\n"
        printf "${Cian_Brillante}╰────────────────────────────────────────╯${Reset}\n"

        printf "\n${Cian_Brillante}╭────────────╮${Reset}\n"        
        printf "${Cian_Brillante}│ ${Gris}[${Rojo_Brillante}0${Gris}]${Reset} ${exit_message}  ${Cian_Brillante}│\n"
        printf "${Cian_Brillante}╰────────────╯${Reset}\n"    
}

main() {
    clear
    banner
    while true
    do
        printf "\n ${Rojo_Brillante}➤ ${Verde_Brillante}${input_message}${Reset}:"
        read -p " " option

        if [[ "${option}" == "1" ]]; then
            clear
            install

        elif [[ "${option}" == "2" ]]; then
            clear
            reinstall

        elif [[ "${option}" == "3" ]]; then
            clear
            update

        elif [[ "${option}" == "4" ]]; then
            clear 
            verify_packages  

        elif [[ "${option}" == "5" ]]; then
            clear   
            cache_clear

        elif [[ "${option}" == "6" ]]; then
            clear
            solve_problems 

        elif [[ "${option}" == "7" ]]; then
            cd ~/Stellar
            bash init.sh

        elif [[ "${option}" == "8" ]]; then
            info            

        elif [[ "${option}" == "0" ]]; then
            clear
            reload() {
                cd ~/Stellar/termux/system
                python banner.py
                cd
            }
            reload
            break  

        elif [[ "${option}" == "" ]]; then
            printf "\n${Gris}[${Rojo_Brillante}!${Gris}]${Reset} ${invalid_data_message}\n"
            continue

        else
            printf "\n"
            eval $option
        fi

    done
}

prepare() {
    apply_lang=$(getprop persist.sys.locale | cut -d'-' -f1)
    if [[ $apply_lang = "es" ]]; then
        echo spanish > ~/Stellar/configs/selected_lang.txt
    elif [[ $apply_lang = "en" ]]; then
        echo english > ~/Stellar/configs/selected_lang.txt
    elif [[ $apply_lang = "ja" ]]; then
        echo japanese > ~/Stellar/configs/selected_lang.txt
    elif [[ $apply_lang = "zh" ]]; then
        echo chinese > ~/Stellar/configs/selected_lang.txt                
    elif [[ $apply_lang = "ko" ]]; then
        echo korean > ~/Stellar/configs/selected_lang.txt
    elif [[ $apply_lang = "pt" ]]; then
        echo portuguese > ~/Stellar/configs/selected_lang.txt       
    else
        echo english > ~/Stellar/configs/selected_lang.txt
    fi
    sleep 0.1
    printf "\r${Cian_Brillante}︕ ${Reset} ${verify_message}\n"
    sleep 0.1
    verify_apt=$(dpkg --get-selections | grep -v deinstall | grep lsd | awk '{print $1}')
    verify_pip=$(pip list 2>/dev/null | grep lolcat | awk '{print $1}')
    if [[ $verify_apt == "lsd" ]] && [[ $verify_pip == "lolcat" ]]; then
        printf "\n"
        printf "\n${on_message}\n" | lolcat -a -d 20
        printf "\n"
        printf "\a\r${Verde_Brillante} ✓ ${Reset} ${success_verify_message}\n"
        sleep 2
        main
    else
        printf "\r${Cian_Brillante}︕ ${Reset} ${installing_dependencies_message}\n"
        sleep 2
        apt-get install lsd -y > stellar_verify.log
        wait
        apt-get install python -y > stellar_verify.log
        wait
        pip install lolcat > stellar_verify.log
        wait
        printf "\a\r${Verde_Brillante} ✓ ${Reset} ${success_installing_dependencies_message}\n"
        sleep 2
        main
    fi
}

ls() {
    lsd --icon-theme unicode
}

command_not_found_handle() {
    echo -e "${Gris}[INFO] ${Reset}${command_not_found_message}: $1"
    return 127
}

preexec() {
    printf "${Gris}[INFO] ${Reset}${execute_command_message}: $1\n"

}

if [ -n "$BASH_VERSION" ]; then
    trap 'preexec "$BASH_COMMAND"' DEBUG
fi

prepare