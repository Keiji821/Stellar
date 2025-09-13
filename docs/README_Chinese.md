<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![开源项目](https://img.shields.io/badge/开源-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![维护中](https://img.shields.io/badge/持续维护中(是)-2ea44f?style=for-the-badge)

<h4>开发语言</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell脚本-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScript运行时](https://img.shields.io/badge/JavaScript运行时-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellar 是一个基于 `Python`、`Bash` 和 `NodeJS` 开发的程序，旨在为单调的 `Termux` 终端赋予全新外观并增加实用功能。

虽然包含部分黑客和OSINT工具命令，但其核心目标是提供多层级个性化定制，全面提升Termux的视觉体验。

</div>

## `🗃️` 文档 

- [英文文档](https://github.com/Keiji821/Stellar/blob/master/docs/README_English.md)

- [日语文档](https://github.com/Keiji821/Stellar/blob/master/docs/README_Japanese.md)

- [中文文档](https://github.com/Keiji821/Stellar/blob/master/docs/README_Chinese.md)

- [韩文文档](https://github.com/Keiji821/Stellar/blob/master/docs/README_Korean.md)

- [葡萄牙语文档](https://github.com/Keiji821/Stellar/blob/master/docs/README_Portuguese.md)

## `📄` 状态信息

`⚠️` 即将内置支持日语、中文、韩语、英语和葡萄牙语界面。

`⚠️` 程序仍在持续开发中，可能存在运行异常。

`📌` 如需贡献代码或提交错误报告，请通过Discord联系开发者：`keiji100`

## `📜` 项目内容

<details>
<summary><b>📑 程序详情</b></summary>

```shell
程序名称: Stellar
创建日期: 2024/06/01
当前版本: v0.0.0 (开发中)
程序大小: 17MB
支持语言: 仅西班牙语
开发者: Keiji821
```
</details>

<details>
<summary><b>📥 安装指南</b></summary>

请按顺序执行以下命令：

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

执行`bash install.sh`后将启动安装程序。为确保完整安装，请保持网络畅通。安装完成后Termux会自动重启，建议完全关闭Termux以保障`TOR`功能正常运作。

</details>

<details>
<summary><b>🧩 功能特性</b></summary>

Stellar在不依赖`Zsh`的情况下，通过纯`Bash`实现Termux深度定制，包含以下功能模块：

> 核心特性
```shell
• 可定制横幅图案/颜色及背景
• 设备信息状态栏
• 集成TOR匿名网络
• Termux背景色自定义
• 专用工具命令集
• 增强型termux-properties配置
• 原生command-not-found提示系统
• 指纹锁屏安全模块
• Termux-API深度集成
• Termux-X11环境变量预配置
```

> APT依赖
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

> PIP依赖
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
<summary><b>📀 命令列表</b></summary>

> **🔧 系统命令**  
```bash
reload       │ 重载横幅系统  
user-config  │ 个性化配置中心
my           │ 显示Stellar个人资料
uninstall    │ 完全卸载程序  
update       │ 从GitHub更新  
bash         │ 重启终端会话   
reset        │ 恢复初始状态
dstr         | rm -rf快捷命令
move         | mv快捷命令
copy         | cp快捷命令
x11          | termux-x11 :0 & export DISPLAY=:0快捷命令
```

> **🛠️ 实用工具**  
```bash
ia           │ 免费API人工智能服务  
ia-image     │ AI图像生成器  
traductor    │ 实时翻译器  
myip         │ 公网IP查询  
passwordgen  │ 安全密码生成  
encrypt-file │ 文件加密工具  
```

> **🌐 信息收集**  
```bash
ipinfo       │ IP情报分析  
urlinfo      │ URL解析  
userfinder   │ 跨平台用户搜索  
phoneinfo    │ 电话号码溯源  
metadatainfo │ 文件元数据提取  
emailsearch  │ 邮箱地址检索  
```

> **📱 Discord工具**  
```bash
userinfo           │ 用户信息查询(ID)  
serverinfo         │ 服务器信息(ID)  
searchinvites      │ 邀请链接搜索  
inviteinfo         │ 邀请详情分析  
role-mapper        │ 角色权限映射  
mutual-servers     │ 共同服务器查询  
webhook-mass-spam  │ Webhook轰炸  
mass-delete-channels │ 批量删除频道  
```

> **📸 Instagram工具**  
```bash
profileinfo  │ 个人资料元数据提取  
```

> **⚡ 渗透测试**  
```bash
ddos        │ DDoS攻击(IP+端口)  
tunnel      │ 访客IP捕获  
```
</details>

<details>
<summary><b>📄 使用指南</b></summary>

安装完成后，通过`user-config`命令可自定义：
- 横幅ASCII艺术图案
- 颜色主题方案
- 终端背景色（支持浅色/深色切换）
- 其他视觉元素

该命令提供交互式界面引导完成所有个性化设置。
</details>

<details>
<summary><b>🌹 开发团队</b></summary>

```diff
+ Keiji821 (主开发者)
```

##### 合作与咨询

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

##### `❤️` 支持项目

如果您认可这个项目，欢迎通过以下方式支持开发：

[![Binance捐赠](https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=捐赠&labelColor=black&message=763579717)](https://pay.binance.com/en)

[![PayPal捐赠](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white&label=捐赠&labelColor=003087&message=felixdppdcg69@gmail.com)](https://paypal.me/felixdppdcg69)
</details>