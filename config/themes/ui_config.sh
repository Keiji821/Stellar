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

# ui_config.sh

printf "${verde}"
read -p 'Ingrese el contenido: ' banner
echo "${banner}" > banner.txt
printf "${verde} Elija la fuente para su banner"
echo " "
printf "${amarillo}

Font Name	Author	Font Creation Date
3-d	Daniel Henninger	
3x5	Richard Kirk & Daniel Cabeza Gras	
5lineoblique		1995/01
acrobatic	Randy Ransom	1994/08
alligator	Simon Bradley	1994/06
alligator2	Daniel Wiz	1994/07
alphabet	Wendell Hicken	1993/11
avatar	Claude Martins	1995/02
banner	Ryan Youck	1994/08
banner3-D	Merlin Greywolf	1994/08
banner3	Merlin Greywolf	1994/08
banner4	Merlin Greywolf	1994/08
barbwire	Ron Fritz	1994/08
basic	Craig O'Flaherty	1994/08
bell	Joshua Bell	1994/03
big	Glenn Chappell	1993/04
bigchief		1994/10
binary	Victor Parada	1994/12
block	Glenn Chappell	1993/04
bubble	Glenn Chappell	1993/04
bulbhead	Jef Poskanzer	1994/06
calgphy2	Vinney Thai	1994/10
caligraphy	Vinney Thai	1994/10
catwalk	Ron Fritz	1994/08
chunky	Chris Gill	1994/06
coinstak	Ron Fritz	1994/08
colossal	Jonathon	1994/06
computer	Mike Rosulek	1994/12
contessa	Christopher Joseph Pirillo	
contrast	Dennis Monk	1994/07
cosmic	Mike Rosulek	1995/07
cosmike	Mike Rosulek	1995/11
cricket	Leslie Bates	1996/01
cursive	Jerrad Pierce	1985
cyberlarge	Kent Nassen	1994/10
cybermedium	Kent Nassen	1994/10
cybersmall	Kent Nassen	1994/10
diamond	Ron Fritz	1994/08
digital	Glenn Chappell	1994/01
doh	Curtis Wanner	1995/04
doom	Frans P. de Vries	1996/06
dotmatrix	Curtis Wanner	1995/08
drpepper	Eero Tamminen	
eftichess	Michel Eftimakis	1995/05
eftifont	Michel Eftimakis	1995/01
eftipiti	Michel Eftimakis	1995/02
eftirobot	Michel Eftimakis	1995/05
eftitalic	Michel Eftimakis	1995/01
eftiwall	Michel Eftimakis	1995/02
eftiwater	Michel Eftimakis	1995/08
epic	Claude Martins	1994/12
fender	Scooter	1994/08
fourtops	Randall Ransom	1994/04
fuzzy	Juan Car	1994/02
goofy	Steven de Brouwer	
gothic	Wendell Hicken	1993/11
graffiti	Leigh Purdie and Tim Maggio	1994/03
hollywood	Juan Car	1994/03
invita		1994/06
isometric1	Kent Nassen	1994/10
isometric2	Kent Nassen	1994/10
isometric3	Kent Nassen	1994/10
isometric4	Kent Nassen	1994/10
italic	Bas Meijer	
ivrit	John Cowan	
jazmine	Eamon Daly	
jerusalem	Gedaliah Friedenberg	1994/02
katakana	Vinney Thai	1994/08
kban	Randy Jae Weinstein	1994/05
larry3d	Larry Gelberg	1994/02
lcd	Karl von Laudermann	1993/11
lean	Glenn Chappell	1993/04
letters	Sriram J. Gollapalli	1994/07
linux	Larry Smith	1995/12
lockergnome	Simon Bradley	
madrid	Juan Car	1993/11
marquee	Ron Fritz	1994/08
maxfour	Randall Ransom	1994/01
mike	Michael Sullivan	1994/09
mini	Glenn Chappell	1993/04
mirror	David Walton	1994/08
mnemonic	John Cowan	
morse	Glenn Chappell	1995/10
moscow	Tracy Schuhwerk	1993/11
nancyj-fancy	Eamon Daly	
nancyj-underlined	Eamon Daly	
nancyj	Eamon Daly	
nipples	Ron Fritz	1994/08
ntgreek	Bruce Jakeway	1994/04
o8	Gordon Lee	
ogre	Glenn Chappell & Ian Chai	1993/03
pawp	Curtis Wanner	1994
peaks	Ron Fritz	1994/08
pebbles	Ryan Youck	1994/08
pepper	Juan Car	1994/01
poison	Vinney Thai	1994/10
puffy	Juan Car	1994/03
pyramid	Claude Martins	1995/02
rectangles	David Villegas	1994/12
relief	Nick Miners	1994/06
relief2	Merlin Greywolf	1994/08
rev	Matt E. Thurston	
roman	Nick Miners	1994/06
rot13	Victor Parada	1994/12
rounded	Nick Miners	1994/05
rowancap	Kent Nassen	1995/01
rozzo	Mike Rosulek	1995/12
runic	Bryan Alexander	1994/08
runyc	Bryan Alexander	1994/08
sblood	Kent Nassen	1994/11
script	Glenn Chappell	1993/04
serifcap	Bruce M. Binder	
shadow	Glenn Chappell	1993/06
short	Juan Car	
slant	Glenn Chappell	1993/03
slide	Victor Parada	1994/08
slscript	Wendell Hicken	1994/03
small	Glenn Chappell	1996/03
smisome1	M. Lindsey	1996/02
smkeyboard	Kent Nassen	1994/11
smscript	Glenn Chappell	1996/03
smshadow	Glenn Chappell	1996/03
smslant	Glenn Chappell	1996/03
smtengwar	Belinda Asbell	1996/02
speed	Claude Martins	1995/02
stampatello	Marco Bodrato	1996/02
standard	Glenn Chappell & Ian Chai	1993/03
starwars	Ryan Youck	1994/12
stellar	Ron Fritz	1994/08
stop	David Walton	1994/08
straight	Bas Meijer	
tanja	Christopher J. Pirillo	
tengwar	Belinda Asbell	1996/02
term	Glenn Chappell	1993/04
thick	Randall Ransom	1994/02
thin	Wendell Hicken	1993/11
threepoint	Randall Ransom	1994/04
ticks	Victor Para
"
read -p 'Fuente: ' font
echo "${font}" > banner_font.txt
echo " "
printf "${gris}[$verde2✔$gris]${blanco2} Su banner personalizado se ha configurado correctamente!"
echo " "
echo " "
printf "${gris}[${verde}+${gris}] ${blanco2}Escriba ${verde}reload ${blanco2}para aplicar los cambios."
echo " " 
echo " "