<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![Open Source](https://img.shields.io/badge/Open_Source-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![Maintained](https://img.shields.io/badge/保守%20(はい)-2ea44f?style=for-the-badge)

<h4>使用言語</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScript Runtime](https://img.shields.io/badge/JavaScript_Runtime-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellarは、`python`、`bash`、`nodejs`で作られたプログラムで、`termux`の退屈な外観を改善し、新しい外観と機能を追加します。

ハッキングやOSINT向けのツールもコマンド形式で含まれていますが、主な焦点はカスタマイズレイヤーを提供してtermuxの外観を改善することです。

</div>

`Stellar UI in Termux`
<table align="center">
  <tr>
    <td><img src="https://github.com/Keiji821/Stellar/blob/master/resources/images/Stellar.jpg" width="500"></td>
  </tr>
</table>

> この写真はStellarを使用してTermuxターミナルから撮影されました。

## `📄` ステータス情報

`✅️` 多言語サポート
`✅️` 公式バージョン

`📌` Stellarに貢献したい場合やプログラム内のバグを報告したい場合は、ユーザー名 `keiji100` で私のDiscordに追加して連絡してください。

## `📜` 内容

<details>
<summary><b>📑 プログラム詳細</b></summary>

```shell script
プログラム名: Stellar
作成日: 2024年6月1日
バージョン: v1.0.1 公式バージョン
プログラムサイズ: 27.4 MB
対応言語: スペイン語、英語、日本語、韓国語、ポルトガル語、中国語
制作者: Keiji821
```

</details>

<details>
<summary><b>📥 インストール手順</b></summary>

Stellarをインストールするには、次の手順に従ってください：

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

bash init.shを実行すると、Stellarのインストールシステムが起動します。Stellarを正しくインストールするために、良好なインターネット接続を確保してください！Stellarのインストール後、Termuxセッションが再起動します。Stellarインストール後はTermuxを閉じることをお勧めします。

</details>

<details>
<summary><b>🧩 特徴</b></summary>

Stellarは、TermuxのカスタマイズのためにZshをプロバイダーとして使用せずにBashを最大限に活用するプログラムです。以下のような様々な修正と依存関係が含まれています：

特徴と変更点

```shell script
• バナーとその色、背景のカスタマイズ機能
• デバイス情報を表示するバナー下のテーブル
• セキュリティ - TORによる保護レイヤー
• Termuxの背景色のカスタマイズ機能
• Stellarシステムの基本コマンドとユーティリティ
• 改善されたtermux-propertiesの適用
• 新しいネイティブStellar command-not-found
• Termuxの指紋認証画面ロック
• Termux APIとの統合
• Termux-X11変数のデフォルトインポート
```

APT依存関係

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

PIP依存関係

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
<summary><b>🔨 プラグイン</b></summary>

使い方： 任意のプログラミング言語でStellar用の独自コマンドを作成できます。Stellarを起動すると、作成した各コマンド/プラグインが自動的に読み込まれて使用可能になります。

プラグインの作成方法： 何でもプラグインにできます。次のパス >>> Stellar/plugins にcdするか、お気に入りのツールを使ってそのパスに移動し、プラグインを配置します。その後、ターミナルを再起動するとStellarが読み込みます。Bash、Python、JavaScriptで作成できます。これらはStellarがデフォルトでインストールする言語なので、急遽何かをインストールする必要はありません。もちろん、お好みのプログラミング言語のコンパイラをインストールして、その言語で作成することもできます。

</details>

<details>
<summary><b>📀 コマンド</b></summary>

Stellarには、使用するためのコマンドが含まれています：

システム

```bash
menu         | 利用可能なStellarコマンドとそのステータスを表示
reload       | システムバナーを再読み込み
user-config  | バナーとプロフィールをカスタマイズ
manager      | Stellarの管理、インストール、更新
my           | Stellarプロフィールを表示
uninstall    | Stellarを完全にアンインストール
x11          | termux-x11 :0 & export DISPLAY=:0のエイリアス
```

OSINT

```bash
ipinfo        | IPから情報を取得
urlinfo       | URLを分析
phoneinfo     | 電話番号情報
metadatainfo  | ファイルからメタデータを抽出
```

</details>

<details>
<summary><b>📄 使用ガイド</b></summary>

使い方は簡単です。インストールして、通常通りtermuxを使い始めるだけです。user-configコマンドを使用すると、バナーの表示（希望するアスキーアートの表示）、色の追加、背景（白または他の色）の設定など、バナーの様々な側面を変更できます。

user-configコマンドを使用すると、termuxの背景テーマを変更することもできます。暗い背景を白や青に変更することができます。

</details>

<details>
<summary><b>🌹 作者</b></summary>

```diff
+ Keiji821 (開発者)
```

質問やコラボレーションについては、私に連絡してください。

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

❤️ 寄付

このプロジェクトを気に入って、役に立つと思われたなら、このプロジェクトとその開発を支援するために、好きな金額を寄付することを検討してください。

https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=Donate&labelColor=black&message=763579717


</details>