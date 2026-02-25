<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![Open Source](https://img.shields.io/badge/Open_Source-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![Maintained](https://img.shields.io/badge/维护%20(是)-2ea44f?style=for-the-badge)

<h4>使用技术</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScript Runtime](https://img.shields.io/badge/JavaScript_Runtime-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellar是一个用`python`、`bash`和`nodejs`开发的程序，旨在改善`termux`枯燥的外观，为其增添新的界面和功能。

虽然它包含一些以命令形式提供的黑客和OSINT工具，但其主要重点是提供自定义层来改善termux的外观。

</div>

`Stellar UI in Termux`
<table align="center">
  <tr>
    <td><img src="https://github.com/Keiji821/Stellar/blob/master/resources/images/Stellar.jpg" width="500"></td>
  </tr>
</table>

> 这张照片是使用Stellar在Termux终端中拍摄的。

## `📄` 状态信息

`✅️` 多语言支持
`✅️` 官方版本

`📌` 如果您想为Stellar做出贡献或报告程序中的错误，请通过用户名 `keiji100` 添加我的Discord联系我。

## `📜` 内容

<details>
<summary><b>📑 程序详情</b></summary>

```shell script
程序名称：Stellar
创建日期：2024年6月1日
版本：v1.0.1 官方版本
程序大小：27.4 MB
支持语言：西班牙语、英语、日语、韩语、葡萄牙语、中文
创建者：Keiji821
```

</details>

<details>
<summary><b>📥 安装步骤</b></summary>

要安装Stellar，请按照以下步骤操作：

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

执行bash init.sh后，Stellar的安装系统将启动。请确保您有良好的互联网连接以确保Stellar正确安装！Stellar安装完成后，您的Termux会话将重新启动。建议您在安装Stellar后关闭Termux。

</details>

<details>
<summary><b>🧩 功能特点</b></summary>

Stellar是一个充分利用Bash的程序，不使用Zsh作为Termux自定义的提供者。它包括以下不同的修改和依赖项：

功能和更改

```shell script
• 自定义横幅及其颜色和背景的功能
• 设备信息显示在横幅下方的表格中
• 安全性 - 通过TOR提供保护层
• 自定义Termux背景颜色的功能
• Stellar系统的基本命令和实用程序
• 应用改进的termux-properties
• 新的原生Stellar command-not-found
• Termux的指纹屏幕安全锁
• 与Termux API的集成
• 默认导入Termux-X11变量
```

APT依赖项

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

PIP依赖项

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
<summary><b>🔨 插件</b></summary>

如何使用： 您可以用任何编程语言为Stellar创建自己的命令。启动Stellar时，它会自动加载您创建的每个命令/插件以供使用。

如何创建插件： 您可以为任何功能创建插件。在以下路径 >>> Stellar/plugins，使用cd或您喜欢的工具进入该路径并放置您的插件。之后，重新启动您的终端，Stellar将加载它。您可以使用Bash、Python或JavaScript创建，因为这些是Stellar默认安装的语言，您无需在最后一刻安装任何东西。当然，您也可以通过安装您喜欢的编程语言的编译器来用该语言创建插件。

</details>

<details>
<summary><b>📀 命令列表</b></summary>

Stellar包含一系列可供使用的命令：

系统命令

```bash
menu         | 显示可用的Stellar命令及其状态
reload       | 重新加载系统横幅
user-config  | 自定义横幅和个人资料
manager      | 管理、安装和更新Stellar
my           | 显示您的Stellar个人资料
uninstall    | 完全卸载Stellar
x11          | termux-x11 :0 & export DISPLAY=:0的别名
```

OSINT命令

```bash
ipinfo        | 获取IP信息
urlinfo       | 分析URL
phoneinfo     | 电话号码信息
metadatainfo  | 提取文件元数据
```

</details>

<details>
<summary><b>📄 使用指南</b></summary>

使用方法很简单：安装后像平常一样开始使用termux。使用user-config命令可以修改横幅的各个方面，无论是显示您想要的ASCII艺术，还是添加颜色，以及设置背景（白色或其他颜色）。

user-config命令还允许您修改termux的背景主题，将深色背景更改为白色或蓝色。

</details>

<details>
<summary><b>🌹 作者</b></summary>

```diff
+ Keiji821 (开发者)
```

如有疑问或合作意向，请联系我。

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

❤️ 捐赠

如果您喜欢这个项目并觉得它有用，请考虑捐赠任意金额来支持这个项目及其开发。

https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=Donate&labelColor=black&message=763579717


</details>