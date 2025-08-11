<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![Código Aberto](https://img.shields.io/badge/Código_Aberto-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![Mantido](https://img.shields.io/badge/Mantido_(Sim)-2ea44f?style=for-the-badge)

<h4>Construído com</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![Runtime JavaScript](https://img.shields.io/badge/Runtime_JavaScript-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellar é um programa desenvolvido em `Python`, `Bash` e `NodeJS` projetado para melhorar a aparência básica do `Termux` com um visual renovado e novas funcionalidades.

Embora inclua algumas ferramentas de comandos para hacking e OSINT, seu foco principal é oferecer múltiplas camadas de personalização para aprimorar a experiência visual do Termux.

</div>

## `🗃️` Documentação 

- [Documentação em Inglês](https://github.com/Keiji821/Stellar/blob/master/docs/README_English.md)
- [Documentação em Japonês](https://github.com/Keiji821/Stellar/blob/master/docs/README_Japanese.md)
- [Documentação em Chinês](https://github.com/Keiji821/Stellar/blob/master/docs/README_Chinese.md)
- [Documentação em Coreano](https://github.com/Keiji821/Stellar/blob/master/docs/README_Korean.md)
- [Documentação em Português](https://github.com/Keiji821/Stellar/blob/master/docs/README_Portuguese.md)

## `📄` Informações de Status

`⚠️` Em breve: Suporte para japonês, chinês, coreano, inglês e português na interface

`⚠️` Em desenvolvimento ativo - pode conter bugs

`📌` Para contribuir ou reportar bugs, contate via Discord: `keiji100`

## `📜` Conteúdo

<details>
<summary><b>📑 Detalhes do Programa</b></summary>

```shell
Nome do Programa: Stellar
Data de Criação: 01/06/2024
Versão: v0.0.0 (Em Desenvolvimento)
Tamanho: 17MB
Idiomas: Apenas espanhol
Criador: Keiji821
```
</details>

<details>
<summary><b>📥 Passos de Instalação</b></summary>

Execute estes comandos sequencialmente:

```shell
pkg update && pkg upgrade
```

```shell
pkg install git -y
```

```shell
git clone https://github.com/Keiji821/Stellar
```

```shell
cd Stellar
```

```shell
bash install.sh
```

Após executar `bash install.sh`, o sistema de instalação será iniciado. Garanta conexão estável à internet. O Termux reiniciará após a instalação - recomenda-se fechar completamente para o correto funcionamento do `TOR`.

</details>

<details>
<summary><b>🧩 Funcionalidades</b></summary>

Stellar maximiza capacidades do `Bash` sem depender do `Zsh`:

> Principais Recursos
```shell
• Banner personalizável/cores de fundo
• Painel de informações do dispositivo
• Camada de segurança TOR
• Personalização de cor de fundo
• Comandos utilitários essenciais
• termux-properties aprimorado
• Sistema nativo command-not-found
• Bloqueio por impressão digital
• Integração Termux-API
• Variáveis Termux-X11 pré-configuradas
```

> Dependências APT
```shell
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

> Dependências PIP
```shell   
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
<summary><b>📀 Lista de Comandos</b></summary>

> **🔧 SISTEMA**  
```bash
reload       │ Recarregar sistema de banner  
user-config  │ Central de personalização
my           │ Exibir perfil Stellar
uninstall    │ Desinstalar completamente  
update       │ Atualizar do GitHub  
bash         │ Reiniciar sessão terminal   
reset        │ Restaurar estado padrão
delete       | atalho para rm -rf
move         | atalho para mv
copy         | atalho para cp
```

> **🛠️ UTILITÁRIOS**  
```bash
ia           │ Serviço de IA com API gratuita  
ia-image     │ Gerador de imagens por IA  
traductor    │ Tradutor em tempo real  
myip         │ Verificar IP público  
passwordgen  │ Gerador de senhas seguras  
encrypt-file │ Criptografar arquivos  
```

> **🌐 OSINT**  
```bash
ipinfo       │ Analisar informações de IP  
urlinfo      │ Analisador de URLs  
userfinder   │ Busca de usuários multiplataforma  
phoneinfo    │ Consulta de número telefônico  
metadatainfo │ Extrair metadados de arquivos  
emailsearch  │ Busca de emails  
```

> **📱 DISCORD**  
```bash
userinfo           │ Informações de usuário (ID)  
serverinfo         │ Informações de servidor (ID)  
searchinvites      │ Buscar convites  
inviteinfo         │ Analisar convites  
role-mapper        │ Mapear permissões de cargos  
mutual-servers     │ Servidores em comum  
webhook-mass-spam  │ Spam em webhooks  
mass-delete-channels │ Excluir canais em massa  
```

> **📸 INSTAGRAM**  
```bash
profileinfo  │ Metadados de perfil  
```

> **⚡ TESTES DE PENETRAÇÃO**  
```bash
ddos        │ Ataque DDoS (IP+porta)  
tunnel      │ Capturar IPs de visitantes  
```
</details>

<details>
<summary><b>📄 Guia de Uso</b></summary>

Após instalação, use `user-config` para personalizar:
- Arte ASCII do banner
- Esquemas de cores
- Fundo do terminal (modos claro/escuro)
- Outros elementos visuais

Oferece assistente interativo de personalização.
</details>

<details>
<summary><b>🌹 Autores</b></summary>

```diff
+ Keiji821 (Desenvolvedor Principal)
```

##### Colaboração/Consultas

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

##### `❤️` Doações 

Se desejar apoiar o projeto:

[![Doação Binance](https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=Doar&labelColor=black&message=763579717)](https://pay.binance.com/en)

[![Doação PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white&label=Doar&labelColor=003087&message=felixdppdcg69@gmail.com)](https://paypal.me/felixdppdcg69)
</details>