<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![Open Source](https://img.shields.io/badge/Open_Source-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![Maintained](https://img.shields.io/badge/Mantido%20(Sim)-2ea44f?style=for-the-badge)

<h4>Feito com</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScript Runtime](https://img.shields.io/badge/JavaScript_Runtime-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellar é um programa feito com `python`, `bash` e `nodejs` para melhorar a aparência monótona do `termux`, dando-lhe um visual novo e adicionando novas funcionalidades.

Embora inclua algumas ferramentas em forma de comandos voltadas para hacking e OSINT, seu foco principal é melhorar a aparência do termux, fornecendo camadas de personalização.

</div>

`Stellar UI no Termux`
<table align="center">
  <tr>
    <td><img src="https://github.com/Keiji821/Stellar/blob/master/resources/images/Stellar.jpg" width="500"></td>
  </tr>
</table>

> Esta foto foi tirada do terminal Termux usando o Stellar.

## `📄` Informações de Status

`✅️` Suporte multilíngue
`✅️` Versão oficial

`📌` Se você deseja contribuir para o Stellar ou relatar um bug no programa, entre em contato comigo no Discord adicionando-me com o nome de usuário `keiji100`

## `📜` Conteúdo

<details>
<summary><b>📑 Detalhes do Programa</b></summary>

```shell script
Nome do programa: Stellar
Data de criação: 01/06/2024
Versão: v1.0.1 Versão oficial
Tamanho do programa: 27.4 MB
Idiomas do programa: Espanhol, Inglês, Japonês, Coreano, Português, Chinês
Criador: Keiji821
```

</details>

<details>
<summary><b>📥 Passos de Instalação</b></summary>

Para instalar o Stellar, você deve seguir estes passos:

```shell script
apt-get update -y && apt-get upgrade -y
```

```shell script
apt-get install git -y
```

```shell script
git clone https://github.com/Keiji821/Stellar
```

```shell script
cd Stellar
```

```shell script
bash init.sh
```

Após executar o bash init.sh, o sistema de instalação do Stellar será iniciado. Certifique-se de ter uma boa conexão com a internet para a correta instalação do Stellar! Após a instalação do Stellar, sua sessão do Termux será reiniciada. É recomendável que você feche o Termux após instalar o Stellar.

</details>

<details>
<summary><b>🧩 Características</b></summary>

Stellar é um programa que extrai o máximo possível do Bash sem usar Zsh como provedor para a personalização do Termux. Inclui diferentes modificações e dependências, que são as seguintes:

Características e mudanças

```shell script
• Capacidade de personalizar um banner e suas cores, bem como seu fundo
• Tabela abaixo do banner com informações do seu dispositivo
• Segurança, fornece uma camada de proteção com TOR
• Capacidade de personalizar a cor de fundo do Termux
• Comandos e utilitários básicos para o sistema Stellar
• Termux-properties melhorado aplicado
• Um novo command-not-found nativo do Stellar
• Bloqueio de segurança de tela por impressão digital para Termux
• Integração com a API do Termux
• Importação padrão das variáveis do Termux-X11
```

Dependências APT

```shell script
• python
• cloudflared 
• tor
• nmap
• exiftool
• nodejs
• dnsutils
• lsd
```

Dependências PIP

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
<summary><b>🔨 Plugins</b></summary>

Como usar? Você pode criar seus próprios comandos para o Stellar em qualquer linguagem de programação. Ao iniciar o Stellar, ele carregará automaticamente cada comando/plugin que você criou para uso.

Como crio um plugin? Você pode fazer um plugin para qualquer coisa. No seguinte caminho >>> Stellar/plugins, use cd ou sua ferramenta favorita para ir ao caminho e colocar seu plugin. Depois disso, reinicie seu terminal e o Stellar o carregará. Você pode fazê-lo em Bash, Python ou JavaScript, pois são as linguagens que o Stellar instala por padrão e você não precisará instalar nada de última hora, embora também possa criar na linguagem que desejar instalando o compilador da sua linguagem de programação favorita.

</details>

<details>
<summary><b>📀 Comandos</b></summary>

Stellar inclui uma seleção de comandos para uso, que são:

SISTEMA

```bash
menu         | Visualiza os comandos disponíveis do Stellar e seu status
reload       | Recarrega o banner do sistema
user-config  | Personaliza banner e perfil
manager      | Gerencia, instala e atualiza o Stellar
my           | Mostra seu perfil do Stellar
uninstall    | Desinstala o Stellar completamente
x11          | alias de termux-x11 :0 & export DISPLAY=:0
```

OSINT

```bash
ipinfo        | Obtém informações de um IP
urlinfo       | Analisa URLs
phoneinfo     | Informações de número telefônico
metadatainfo  | Extrai metadados de arquivos
```

</details>

<details>
<summary><b>📄 Guia de Uso</b></summary>

O uso é simples: instale e comece a usar seu termux como normalmente faz. Com o comando user-config você pode modificar aspectos do banner, seja para exibir a arte ascii que desejar, bem como adicionar cor e também um fundo, seja branco ou qualquer outra cor.

O comando user-config também permite modificar o tema de fundo do termux, seja para mudar o fundo escuro para um branco ou azul.

</details>

<details>
<summary><b>🌹 Autores</b></summary>

```diff
+ Keiji821 (Desenvolvedor)
```

Contate-me para dúvidas e colaborações.

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

❤️ Doações

Se você gostou deste projeto e o achou útil, considere apoiar este projeto e seu desenvolvimento doando a quantia que desejar.

https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=Donate&labelColor=black&message=763579717

https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white&label=Donate&labelColor=003087&message=felixdppdcg69@gmail.com

</details>