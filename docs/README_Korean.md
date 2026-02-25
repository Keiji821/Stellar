<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![Open Source](https://img.shields.io/badge/Open_Source-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![Maintained](https://img.shields.io/badge/유지보수%20(예)-2ea44f?style=for-the-badge)

<h4>사용된 기술</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScript Runtime](https://img.shields.io/badge/JavaScript_Runtime-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellar는 `python`, `bash` 및 `nodejs`로 만들어진 프로그램으로, `termux`의 지루한 외관을 개선하고 새로운 모양과 기능을 추가합니다.

해킹 및 OSINT 중심의 도구를 명령어 형태로 포함하고 있지만, 주된 초점은 맞춤 설정 레이어를 제공하여 termux의 외관을 개선하는 것입니다.

</div>

`Stellar UI in Termux`
<table align="center">
  <tr>
    <td><img src="https://github.com/Keiji821/Stellar/blob/master/resources/images/Stellar.jpg" width="500"></td>
  </tr>
</table>

> 이 사진은 Stellar를 사용하여 Termux 터미널에서 촬영되었습니다.

## `📄` 상태 정보

`✅️` 다국어 지원
`✅️` 공식 버전

`📌` Stellar에 기여하거나 프로그램 내 버그를 신고하려면 사용자 이름 `keiji100`으로 Discord에 추가하여 연락해 주세요.

## `📜` 내용

<details>
<summary><b>📑 프로그램 세부 정보</b></summary>

```shell script
프로그램 이름: Stellar
생성 날짜: 2024년 6월 1일
버전: v1.0.1 공식 버전
프로그램 크기: 27.4 MB
지원 언어: 스페인어, 영어, 일본어, 한국어, 포르투갈어, 중국어
제작자: Keiji821
```

</details>

<details>
<summary><b>📥 설치 단계</b></summary>

Stellar를 설치하려면 다음 단계를 따르세요:

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

bash init.sh를 실행하면 Stellar 설치 시스템이 시작됩니다. Stellar의 올바른 설치를 위해 좋은 인터넷 연결을 확인하세요! Stellar가 설치된 후 Termux 세션이 다시 시작됩니다. Stellar 설치 후 Termux를 닫는 것이 좋습니다.

</details>

<details>
<summary><b>🧩 기능</b></summary>

Stellar는 Termux 사용자 정의를 위해 Zsh를 제공자로 사용하지 않고 Bash를 최대한 활용하는 프로그램입니다. 다음과 같은 다양한 수정 사항과 종속성이 포함되어 있습니다:

기능 및 변경 사항

```shell script
• 배너와 그 색상 및 배경 사용자 정의 기능
• 장치 정보를 표시하는 배너 아래 테이블
• 보안 - TOR를 통한 보호 계층 제공
• Termux 배경색 사용자 정의 기능
• Stellar 시스템의 기본 명령어 및 유틸리티
• 개선된 termux-properties 적용
• 새로운 네이티브 Stellar command-not-found
• Termux용 지문 화면 보안 잠금
• Termux API와의 통합
• Termux-X11 변수의 기본 가져오기
```

APT 종속성

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

PIP 종속성

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
<summary><b>🔨 플러그인</b></summary>

사용 방법: 모든 프로그래밍 언어로 Stellar용 자체 명령어를 만들 수 있습니다. Stellar를 시작하면 생성한 각 명령어/플러그인이 자동으로 로드되어 사용할 수 있습니다.

플러그인 생성 방법: 무엇이든 플러그인으로 만들 수 있습니다. 다음 경로 >>> Stellar/plugins에서 cd하거나 선호하는 도구를 사용하여 해당 경로로 이동한 후 플러그인을 배치합니다. 그런 다음 터미널을 다시 시작하면 Stellar가 로드합니다. Bash, Python 또는 JavaScript로 만들 수 있습니다. 이들은 Stellar가 기본적으로 설치하는 언어이므로 마지막 순간에 아무것도 설치할 필요가 없습니다. 물론 선호하는 프로그래밍 언어의 컴파일러를 설치하여 해당 언어로 만들 수도 있습니다.

</details>

<details>
<summary><b>📀 명령어</b></summary>

Stellar에는 사용할 수 있는 다양한 명령어가 포함되어 있습니다:

시스템 명령어

```bash
menu         | 사용 가능한 Stellar 명령어 및 상태 표시
reload       | 시스템 배너 다시 로드
user-config  | 배너 및 프로필 사용자 정의
manager      | Stellar 관리, 설치 및 업데이트
my           | Stellar 프로필 표시
uninstall    | Stellar 완전 제거
x11          | termux-x11 :0 & export DISPLAY=:0의 별칭
```

OSINT 명령어

```bash
ipinfo        | IP 정보 가져오기
urlinfo       | URL 분석
phoneinfo     | 전화번호 정보
metadatainfo  | 파일에서 메타데이터 추출
```

</details>

<details>
<summary><b>📄 사용 가이드</b></summary>

사용법은 간단합니다: 설치한 후 평소처럼 termux를 사용하기 시작하면 됩니다. user-config 명령어를 사용하면 배너의 여러 측면을 수정할 수 있습니다. 원하는 ASCII 아트를 표시하거나, 색상을 추가하거나, 배경(흰색 또는 다른 색상)을 설정할 수 있습니다.

user-config 명령어를 사용하면 termux의 배경 테마도 수정할 수 있습니다. 어두운 배경을 흰색이나 파란색으로 변경할 수 있습니다.

</details>

<details>
<summary><b>🌹 저자</b></summary>

```diff
+ Keiji821 (개발자)
```

질문이나 협업이 있으면 연락해 주세요.

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

❤️ 기부

이 프로젝트가 마음에 들고 유용하다고 생각하신다면, 원하는 금액을 기부하여 이 프로젝트와 그 개발을 지원해 주시기 바랍니다.

https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=Donate&labelColor=black&message=763579717


</details>