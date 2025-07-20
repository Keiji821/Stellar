<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![オープンソース](https://img.shields.io/badge/オープンソース-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![メンテナンス中](https://img.shields.io/badge/メンテナンス中(はい)-2ea44f?style=for-the-badge)

<h4>使用技術:</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScript Runtime](https://img.shields.io/badge/JavaScript_Runtime-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellarは`Python`、`Bash`、`Node.js`で開発されたプログラムで、`Termux`の見た目を改善し、新しい機能を追加します。

ハッキングやOSINT向けのツールも含まれていますが、主な目的はTermuxのカスタマイズ性を高めることです。

</div>

#

⚠️ `近日対応予定: 日本語、中国語、韓国語、英語、ポルトガル語のサポート`

⚠️ `現在も開発中です - バグが含まれている可能性があります`

`📌` Stellarへの貢献やバグ報告は、Discordで`keiji100`までご連絡ください

#

<details>
<summary><b>🔖 インストール方法</b></summary>

##### Stellarをインストールする手順:

```shell script
git clone https://github.com/Keiji821/Stellar
```

```shell script
cd Stellar
```

```shell script
bash install.sh
```

##### `bash install.sh`を実行すると自動的にインストールされます（安定したインターネット接続が必要です）。インストール後、Termuxセッションが再起動します。TORを正しく機能させるため、Termuxを完全に閉じてから再度開くことを推奨します。

</details>

<details>
<summary><b>📑 機能一覧</b></summary>

##### Stellar OSはOSINTやハッキング向けのコマンドを提供します（全てオプション）。主な目的はTermuxのカスタマイズです。

#### `🔧` システム
| コマンド       | 説明 |  
|--------------|-------------|  
| `reload`     | システムバナーを再読み込み |  
| `user-config`| Stellarのインターフェースとプロフィールをカスタマイズする |  
| `uninstall`  | Stellarを完全にアンインストール |  
| `update`     | GitHubからStellarを更新 |  
| `bash`       | ターミナルセッションを再起動 |  
| `history -c` | コマンド履歴を消去 |  
| `reset`      | ターミナルを初期状態にリセット |  
| `my`         | Stellarプロフィールを表示 |    

#### `🛠️` ユーティリティ
| コマンド         | 説明 |  
|----------------|-------------|  
| `ia`           | 無料AI APIサービス |  
| `ia-image`     | AI画像生成ツール |  
| `translator`   | リアルタイム翻訳 |  
| `myip`         | 公開IPを表示 |  
| `passwordgen`  | 安全なパスワード生成 |  
| `encrypt-file` | ファイル暗号化ツール |  

#### `📡` OSINT (情報収集)  
| コマンド         | 説明 |  
|----------------|-------------|  
| `ipinfo`       | IPアドレス情報の取得 |  
| `urlinfo`      | URL分析ツール |  
| `userfinder`   | 複数プラットフォームでのユーザー検索 |  
| `phoneinfo`    | 電話番号検索 |  
| `metadatainfo` | ファイルメタデータ抽出 |  
| `emailsearch`  | メール検索ツール |  

#### `📱` Discord
| コマンド                | 説明 |  
|-----------------------|-------------|  
| `userinfo`            | ユーザー情報取得(ID使用) |  
| `serverinfo`          | サーバー情報取得(ID使用) |  
| `searchinvites`       | Discord招待リンク検索 |  
| `inviteinfo`          | 招待リンク分析 |  
| `role-mapper`         | サーバーロールマッピング(サーバーID必要) |  
| `mutual-servers`      | ユーザー間の共通サーバー確認 |  
| `webhook-mass-spam`   | Webhookスパムツール |  
| `mass-delete-channels`| チャンネル一括削除(所有サーバーのみ) |  

#### `📸` Instagram OSINT 
| コマンド        | 説明 |  
|---------------|-------------|  
| `profileinfo` | Instagramプロフィールメタデータ抽出 |  

#### `🛡️` ペネトレーションテスト 
| コマンド    | 説明 |  
|-----------|-------------|  
| `ddos`    | DDoS攻撃ツール(IP+ポート) |  
| `tunnel`  | 訪問者のIPを取得する画像をホスト |  

##### StellarはバックグラウンドでTORを実行し、匿名性を保護します。

</details>

<details>
<summary><b>📄 使用ガイド</b></summary>

##### 使い方は簡単です。インストール後、通常通りTermuxを使用できます。`user-config`コマンドで以下をカスタマイズ可能:
- ASCIIアートの表示
- カラースキーム
- 背景色（ライト/ダークテーマ含む）
- ユーザーと検証方法 

##### `user-config`コマンドではTermuxのテーマ全体をカスタマイズでき、ダークからライト/ブルー背景などに変更できます。

</details>

#

# `🖋️` 作者

```diff
+ Keiji821 (開発者)
```

##### 質問や協力の依頼はこちらまで

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

##### `❤️` 寄付のお願い

このプロジェクトが気に入り、役に立った場合は、任意の金額で開発をサポートしていただけると幸いです。

[![Binance Donate](https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=寄付&labelColor=black&message=763579717)](https://pay.binance.com/en)

[![PayPal Donate](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white&label=寄付&labelColor=003087&message=felixdppdcg69@gmail.com)](https://paypal.me/felixdppdcg69)
