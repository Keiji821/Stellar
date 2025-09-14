<p align= "center"> <kbd> <img  src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740"width="420"> </kbd><br><br>

<div align="center">

![Open Source](https://img.shields.io/badge/Open_Source-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![Maintained](https://img.shields.io/badge/Mantenido%20(Sí)-2ea44f?style=for-the-badge)


<h4>Hecho en</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScript Runtime](https://img.shields.io/badge/JavaScript_Runtime-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)


</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
  </div>

<div align="center">

Stellar, es un programa hecho en `python`, `bash` y `nodejs` para mejorar la aburrida apariencia de `termux` para darle una apariencia nueva añadiendo nuevas funcionalidades.

Aunque incluye algunas herramientas en forma de comandos orientadas al hacking y osint se centra en mejorar la apariencia de termux otorgando capas de personalización.

</div>

<table align="center">
  <tr>
    <td><img src="https://cdn.discordapp.com/attachments/1202078440371789884/1404344345305284661/Screenshot_20250811-0159123.jpg?ex=689ad917&is=68998797&hm=07e3faa38dbbb41dae7ea0a14f584281f5a6c4fd0c27a09dac33c1757906724f&" width="500"></td>
    <td><img src="https://cdn.discordapp.com/attachments/1202078440371789884/1404344344990842960/Screenshot_20250811-0157413.jpg?ex=689ad917&is=68998797&hm=66c48b9d67e2735dc24de4154b13571f611212686dfeaa6c429e5ed22e47bf45&" width="500"></td>
  </tr>
</table>

## `🗃️` Documentation 

- [Documentation in English](https://github.com/Keiji821/Stellar/blob/master/docs/README_English.md)

- [日本語のドキュメント](https://github.com/Keiji821/Stellar/blob/master/docs/README_Japanese.md)

- [中文文檔](https://github.com/Keiji821/Stellar/blob/master/docs/README_Chinese.md)

- [한국어 문서](https://github.com/Keiji821/Stellar/blob/master/docs/README_Korean.md)

- [Documentação em português](https://github.com/Keiji821/Stellar/blob/master/docs/README_Portuguese.md)

## `📄` Información de estado

`⚠️` Próximamente soporte dentro del programa para el idioma japonés, chino, coreano, ingles y portugués.

`⚠️` In-program support for Japanese, Chinese, Korean, English, and Portuguese is coming soon.

`⚠️` Aún en constante desarrollo, pueden haber fallos.

`⚠️` Still under constant development, there may be errors.

`📌` Si desea aportar a Stellar o reportar un error dentro del programa contacteme a mi Discord agregandome por el nombre de usuario de `keiji100`

## `📜` Contenido

<details>
<summary><b>📑 Detalles del programa</b></summary>

```shell script
Nombre del programa: Stellar
Fecha de creación: 01/06/2024
Versión: v0.0.0 (Aún en desarrollo)
Tamaño del programa: 17mb
Idiomas del programa: Solo español
Creador: Keiji821
```
</details>

<details>
<summary><b>📥 Pasos de instalación</b></summary>

Para instalar Stellar debe seguir los siguientes pasos:

```shell script
pkg update && pkg upgrade
```

```shell script
pkg install git -y
```

```shell script
git clone https://github.com/Keiji821/Stellar
```

```shell script
cd Stellar
```

```shell script
bash install.sh
```

Luego de ejecutar el `bash install.sh` se iniciará el sistema de instalación de `Stellar` ¡Asegurese de tener una buena conexión a internet para la correcta instalación de `Stellar`! luego de haberse instalado Stellar su sesión de `Termux` se reiniciará, es recomendable que cierres `Termux` luego de instalar `Stellar` para que funcione correctamente `TOR`

</details>

<details>
<summary><b>🧩 Características</b></summary>


Stellar es un programa que exprime todo lo posible a `Bash` sin usar `Zsh` como proveedor para la personalización de Termux, incluye diferentes modificaciones y dependencias las cuales son las siguientes:

> Características y cambios 

```shell script
• Poder personalizar un banner y sus colores así como el fondo del mismo
• Tabla debajo del banner con información de su dispositivo
• Seguridad, otorga una capa de protección con TOR
• Poder personalizar el color de fondo para Termux
• Comandos y utilidades básicas para el sistema de Stellar
• Se aplica un termux-properties mejorado 
• Un nuevo command-not-found nativo de Stellar 
• Bloqueó de seguridad de pantalla por huella digital para Termux
• Integración con la API de Termux
• Importación predeterminada de las variables de Termux-X11
```

> Dependencias APT

```shell script
• python
• cloudflared 
• tor
• nmap
• exiftool
• nodejs
• termux-api
• dnsutils
• lsd
• x11-repo
• termux-x11-nightly
• root-repo
```

> Dependencias PIP

```shell script   
• beautifulsoup4
• pyfiglet
• phonenumbers
• psutil
• PySocks
• requests
• rich
• "rich[jupyter]"
• lolcat
• discord
• fake_useragent
• pycryptodome
```
</details>

<details>
<summary><b>📀 Comandos</b></summary>

Stellar incluye una selección de comandos para su uso los cuales son:
  
> **SISTEMA**  
```bash
reload       │ Recarga el banner del sistema  
user-config  │ Personaliza banner y perfil
my           │ Muestra tu perfil de Stellar
uninstall    │ Desinstala Stellar completamente  
update       │ Actualiza desde GitHub  
bash         │ Reinicia la sesión de terminal   
reset        │ Restablece terminal a estado inicial
x11          | alias de termux-x11 :0 & export DISPLAY=:0
```


> **UTILIDADES**  
```bash
ia           │ Servicio de IA con API gratuita  
ia-image     │ Generador de imágenes con IA  
traductor    │ Traducción en tiempo real  
myip         │ Muestra tu IP pública  
passwordgen  │ Genera contraseñas seguras  
encrypt-file │ Encripta archivos  
ddos         │ Ataque DDoS (IP + puerto) 
```


> **OSINT**  
```bash
ipinfo        │ Obtiene información de una IP  
urlinfo       │ Analiza URLs  
userfinder    │ Busca usuarios en plataformas  
phoneinfo     │ Información de número telefónico  
metadatainfo  │ Extrae metadatos de archivos  
emailsearch   │ Búsqueda de correos electrónicos  
instagraminfo | Obtiene los metadatos del perfil
```


> **DISCORD**  
```bash
userinfo             │ Info de usuario (ID)  
serverinfo           │ Info de servidor (ID)  
searchinvites        │ Busca invitaciones  
inviteinfo           │ Analiza invitaciones  
role-mapper          │ Mapea roles (Server ID)  
mutual-servers       │ Servidores en común  
webhook-mass-spam    │ Spam a webhooks  
mass-delete-channels │ Elimina canales masivamente  
```

</details>

<details>
<summary><b>📄 Guía de uso</b></summary>

El uso es simple, se instala y empiece a usar su termux como normalmente lo hace y con el comando `user-config` puede modificar aspectos del banner ya sea hacer que se muestre el arte ascii que usted desee así como ponerle color y también un fondo ya sea de color blanco o cualquier otro.

El comando `user-config` también permite modificar el tema de termux el tema de fondo ya sea para cambiar el fondo oscuro que tiene por uno blanco o azul.

</details>

<details>
<summary><b>🌹 Autores</b></summary>

```diff
+ Keiji821 (Desarrollador)
```

##### Contactame, para dudas y colaboraciones.

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

##### `❤️` Donaciones 

Si te gustó y te gusta este proyecto y te resulta útil considera apoyar a este proyecto y a su desarrollo donando la cantidad que desees.


[![Binance Donate](https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=Donate&labelColor=black&message=763579717)](https://pay.binance.com/en)

[![PayPal Donate](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white&label=Donate&labelColor=003087&message=felixdppdcg69@gmail.com)](https://paypal.me/felixdppdcg69)
</details>
