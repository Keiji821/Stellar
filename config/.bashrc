# Definir colores

gris="\033[1;30m"
blanco="\033[0m"
blanco2="\033[1;37m"
rojo="\033[1;31m"
rojo2="\033[31m"
azul="\033[1;34m"
azul2="\033[34m"
azul_agua="\e[1;36m"
azul_agua2="\e[36m"
verde="\033[1;32m"
verde2="\033[32m"
morado="\033[1;35m"
morado2="\033[35m"
amarillo="\033[1;33m"
amarillo2="\033[33m"
cyan="\033[38;2;23;147;209m"

# Personalizar input

input=$(cat .configs_stellar/themes/input.txt)

function cd() {
  builtin cd "$@"
  local pwd_relative="${PWD/#$HOME}"
  pwd_relative=${pwd_relative#/}
  PS1="${gris}╭──────${azul_agua}(${morado}${pwd_relative}${azul_agua})${gris}\n${gris}╰──${azul_agua}[${verde}${input}${azul_agua}]${gris}── ${amarillo}~${verde} $ ${blanco2}"
}

# Iniciar configuración

clear
python Stellar/config/run.py

# Mostrar banner al final

cd
cd .configs_stellar/themes
cp ~/Stellar/config/.bash_profile ~/.
clear
python banner.py
cd

# Osint - main

ipinfo() {
  cd
  cd Stellar/osint/main
  python ipinfo.py
  cd
}

phoneinfo() {
  cd
  cd Stellar/osint/main
  python phoneinfo.py
  cd
}

urlinfo() {
  cd
  cd Stellar/osint/main
  python urlinfo.py
  cd
}

metadatainfo() {
  cd
  cd Stellar/osint/main
  bash metadatainfo.sh
  cd
}

emailsearch() {
 cd
 cd Stellar/osint/main
 python emailfinder.py
 cd
}

userfinder() {
 cd
 cd Stellar/osint/main
 python userfinder.py
 cd
}

# Osint - Discod

userinfo() {
 cd
 cd Stellar/osint/discord
 python userinfo.py
 cd
}

# Pentesting

ddos() {
  cd
  cd Stellar/pentesting
  python ddos.py
 cd
}

# Sistema

menu() {
  cd
  cd Stellar/config
  python menu.py
  cd
}

reload() {
  cd
  cd .configs_stellar/themes
  clear
  python banner.py
  cd
}

ui() {
 cd
rojo="\033[1;31m"
rojo2="\033[31m"
azul="\033[1;34m"
azul2="\033[34m"
azul_agua="\e[1;36m"
azul_agua2="\e[36m"
verde="\033[1;32m"
verde2="\033[32m"
morado="\033[1;35m"
morado2="\033[35m"
amarillo="\033[1;33m"
amarillo2="\033[33m"
cyan="\033[38;2;23;147;209m"

# ui_config.sh

printf "${verde}Ingrese el texto personalizado para su banner de inicio.\n"
read -p "Ingrese el contenido: " banner
echo "${banner}" > .configs_stellar/themes/banner.txt
printf "${verde}Elija la fuente para su banner"
echo " "
printf "${amarillo}

1. 1row


2. 3-d


3. 3x5


4. 5lineoblique


5. acrobatic


6. alligator


7. alligator2


8. alphabet


9. avatar


10. banner


11. banner3-D


12. banner3


13. banner4


14. barbwire


15. basic


16. bell


17. big


18. bigchief


19. binary


20. block


21. bubble


22. bulbhead


23. calgphy2


24. caligraphy


25. catwalk


26. chunky


27. coinstak


28. colossal


29. computer


30. contessa


31. contrast


32. cosmic


33. cosmike


34. crawford


35. crazy


36. cricket


37. cursive


38. cyberlarge


39. cybermedium


40. cybersmall


41. diamond


42. digital


43. doh


44. doom


45. dotmatrix


46. drpepper


47. eftichess


48. eftifont


49. eftipiti


50. eftirobot


51. eftitalic


52. eftiwall


53. eftiwater


54. epic


55. fender


56. fourtops


57. fraktur


58. funface


59. funfaces


60. fuzzy


61. georgi16


62. ghost


63. ghoulish


64. glenyn


65. goofy


66. gothic


67. graffiti


68. hex


69. hollywood


70. invita


71. isometric1


72. isometric2


73. isometric3


74. isometric4


75. italic


76. ivrit


77. jazmine


78. jerusalem


79. katakana


80. kban


81. lcd


82. lean


83. letters


84. linux


85. lockergnome


86. madrid


87. marquee


88. maxfour


89. merlin1


90. merlin2


91. mike


92. mini


93. mirror


94. mnemonic


95. morse


96. moscow


97. nipples


98. ntgreek


99. o8


100. octal


101. ogre


102. pawp


103. pebbles


104. pepper


105. poison


106. puffy


107. pyramid


108. rectangles


109. relief


110. relief2


111. rev


112. roman


113. rot13


114. rounded


115. rowancap


116. rozzo


117. runic


118. runyc


119. sblood


120. script


121. serifcap


122. shadow


123. shimrod


124. short


125. slant


126. slide


127. slscript


128. small


129. smisome1


130. smkeyboard


131. smscript


132. smshadow


133. smslant


134. smtengwar


135. soft


136. speed


137. spliff


138. stacey


139. stampatello


140. standard


141. starstrips


142. starwars


143. stellar


144. stforek


145. stop


146. straight


147. striped


148. sub-zero


149. swampland


150. swan


151. sweet


152. threepoint


153. ticks


154. ticksslant


155. tinker-toy


156. tombstone


157. trek


158. tsalagi


159. twopoint


160. univers


161. usaflag


162. wavy


163. weird

"
echo " "
printf "${verde}"
read -p 'Fuente: ' font
echo "${font}" > .configs_stellar/themes/banner_font.txt
echo " "
printf "${verde}Configure el texto de la input"
echo " "
printf "${verde}"
read -p 'Ingrese el contenido: ' input
echo "${input}" > .configs_stellar/themes/input.txt
echo " "
printf "${gris}[$verde2✔$gris]${blanco2} Su banner personalizado se ha configurado correctamente!"
echo " "
echo " "
printf "${gris}[${verde}+${gris}] ${blanco2}Escriba ${verde}reload ${blanco2}para aplicar los cambios del banner."
echo " "
echo " "
printf "${gris}[${verde}+${gris}] ${blanco2}Escriba ${verde}bash ${blanco2}para aplicar correctamente el texto personalizado de la input."
echo " "
echo " "
cd
}

# Utilidades - herramientas

ia() {
 cd
 cd Stellar/misc/tools
 python iahttp.py
 cd
}

traductor() {
 cd
 cd Stellar/misc/tools
 python traductor.py
 cd
}

myip() {
 cd
 cd Stellar/misc/tools
 python myip.py
 cd
}
