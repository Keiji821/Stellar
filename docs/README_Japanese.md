<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![オープンソース](https://img.shields.io/badge/オープンソース-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![メンテナンス中](https://img.shields.io/badge/メンテナンス中(はい)-2ea44f?style=for-the-badge)

<h4>開発言語</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shellスクリプト-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScriptランタイム](https://img.shields.io/badge/JavaScriptランタイム-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellarは`Python`、`Bash`、`NodeJS`で開発されたプログラムで、`Termux`の地味な見た目を刷新し、新しい機能を追加します。

ハッキングやOSINT向けのコマンドツールを含んでいますが、主な目的は多層的なカスタマイズでTermuxのビジュアルを向上させることです。

</div>

## `🗃️` ドキュメント 

- [英語ドキュメント](https://github.com/Keiji821/Stellar/blob/master/docs/README_English.md)
- [日本語ドキュメント](https://github.com/Keiji821/Stellar/blob/master/docs/README_Japanese.md)
- [中国語ドキュメント](https://github.com/Keiji821/Stellar/blob/master/docs/README_Chinese.md)
- [韓国語ドキュメント](https://github.com/Keiji821/Stellar/blob/master/docs/README_Korean.md)
- [ポルトガル語ドキュメント](https://github.com/Keiji821/Stellar/blob/master/docs/README_Portuguese.md)

## `📄` ステータス情報

`⚠️` 近日対応予定：日本語、中国語、韓国語、英語、ポルトガル語のUIサポート

`⚠️` 現在開発中 - バグが含まれる可能性あり

`📌` コントリビューションやバグ報告はDiscordで：`keiji100`

## `📜` コンテンツ

<details>
<summary><b>📑 プログラム詳細</b></summary>

```shell
プログラム名: Stellar
作成日: 2024/06/01
バージョン: v0.0.0 (開発中)
サイズ: 17MB
対応言語: スペイン語のみ
開発者: Keiji821
```
</details>

<details>
<summary><b>📥 インストール手順</b></summary>

以下のコマンドを順に実行:

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

`bash install.sh`実行後、インストールシステムが起動します。安定したインターネット接続が必要です。インストール後Termuxが再起動します - `TOR`機能を正しく動作させるため完全に終了することを推奨します。

</details>

<details>
<summary><b>🧩 機能</b></summary>

Stellarは`Zsh`に依存せず`Bash`の機能を最大限活用：

> 主要機能
```shell
• カスタマイズ可能なバナー/背景色
• デバイス情報パネル
• TORセキュリティ層
• Termux背景色カスタマイズ
• 基本ユーティリティコマンド
• 強化版termux-properties
• ネイティブcommand-not-foundハンドラー
• 指紋認証ロック画面
• Termux-API統合
• Termux-X11環境変数
```

> APT依存関係
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

> PIP依存関係
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
<summary><b>📀 コマンド一覧</b></summary>

> **🔧 システム**  
```bash
reload       │ バナーシステム再読み込み  
user-config  │ カスタマイズセンター
my           │ Stellarプロファイル表示
uninstall    │ 完全アンインストール  
update       │ GitHubから更新  
bash         │ ターミナルセッション再起動   
reset        │ デフォルト状態に復元
delete       | rm -rf ショートカット
move         | mv ショートカット
copy         | cp ショートカット
```

> **🛠️ ユーティリティ**  
```bash
ia           │ 無料API AIサービス  
ia-image     │ AI画像生成  
traductor    │ リアルタイム翻訳  
myip         │ 公開IP確認  
passwordgen  │ 安全なパスワード生成  
encrypt-file │ ファイル暗号化  
```

> **🌐 OSINT**  
```bash
ipinfo       │ IP情報分析  
urlinfo      │ URL解析  
userfinder   │ クロスプラットフォームユーザー検索  
phoneinfo    │ 電話番号調査  
metadatainfo │ ファイルメタデータ抽出  
emailsearch  │ メール検索  
```

> **📱 Discord**  
```bash
userinfo           │ ユーザー情報(ID)  
serverinfo         │ サーバー情報(ID)  
searchinvites      │ 招待リンク検索  
inviteinfo         │ 招待分析  
role-mapper        │ ロール権限マッピング  
mutual-servers     │ 共通サーバー  
webhook-mass-spam  │ Webhookスパム  
mass-delete-channels │ チャンネル一括削除  
```

> **📸 Instagram**  
```bash
profileinfo  │ プロフィールメタデータ  
```

> **⚡ ペネトレーションテスト**  
```bash
ddos        │ DDoS攻撃(IP+ポート)  
tunnel      │ 訪問者IP取得  
```
</details>

<details>
<summary><b>📄 使用ガイド</b></summary>

インストール後、`user-config`で以下をカスタマイズ可能:
- バナーASCIIアート
- カラースキーム
- ターミナル背景（ライト/ダークモード）
- その他ビジュアル要素

インタラクティブなカスタマイズウィザードを提供
</details>

<details>
<summary><b>🌹 作者</b></summary>

```diff
+ Keiji821 (リード開発者)
```

##### コラボレーション/相談

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

##### `❤️` 寄付

プロジェクトを支援したい場合:

[![Binance寄付](https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=寄付&labelColor=black&message=763579717)](https://pay.binance.com/en)

[![PayPal寄付](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white&label=寄付&labelColor=003087&message=felixdppdcg69@gmail.com)](https://paypal.me/felixdppdcg69)
</details>