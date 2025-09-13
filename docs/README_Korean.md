<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![오픈소스](https://img.shields.io/badge/오픈소스-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![유지보수](https://img.shields.io/badge/유지보수_중(예)-2ea44f?style=for-the-badge)

<h4>개발 언어</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_스크립트-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScript 런타임](https://img.shields.io/badge/JavaScript_런타임-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellar은 `Python`, `Bash`, `NodeJS`로 개발된 프로그램으로, 지루한 `Termux`의 외관을 새롭게 바꾸고 새로운 기능을 추가합니다.

해킹 및 OSINT 도구 명령어를 포함하고 있지만, 주된 목적은 다층적인 커스터마이징으로 Termux의 시각적 경험을 향상시키는 것입니다.

</div>

## `🗃️` 문서 

- [영어 문서](https://github.com/Keiji821/Stellar/blob/master/docs/README_English.md)
- [일본어 문서](https://github.com/Keiji821/Stellar/blob/master/docs/README_Japanese.md)
- [중국어 문서](https://github.com/Keiji821/Stellar/blob/master/docs/README_Chinese.md)
- [한국어 문서](https://github.com/Keiji821/Stellar/blob/master/docs/README_Korean.md)
- [포르투갈어 문서](https://github.com/Keiji821/Stellar/blob/master/docs/README_Portuguese.md)

## `📄` 상태 정보

`⚠️` 곧 제공 예정: 일본어, 중국어, 한국어, 영어, 포르투갈어 UI 지원

`⚠️` 현재 개발 중 - 버그가 있을 수 있음

`📌` 기여 또는 버그 리포트는 Discord로 문의: `keiji100`

## `📜` 내용

<details>
<summary><b>📑 프로그램 상세</b></summary>

```shell
프로그램 이름: Stellar
제작일: 2024/06/01
버전: v0.0.0 (개발 중)
크기: 17MB
지원 언어: 스페인어만
제작자: Keiji821
```
</details>

<details>
<summary><b>📥 설치 방법</b></summary>

다음 명령어를 순서대로 실행:

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

`bash install.sh` 실행 후 설치 시스템이 시작됩니다. 안정적인 인터넷 연결이 필요합니다. 설치 완료 후 Termux가 재시작되며, `TOR` 기능을 위해 완전히 종료하는 것을 권장합니다.

</details>

<details>
<summary><b>🧩 기능</b></summary>

Stellar은 `Zsh` 없이 순수 `Bash`로 Termux 커스터마이징:

> 주요 기능
```shell
• 커스터마이즈 가능한 배너/배경색
• 디바이스 정보 패널
• TOR 보안 계층
• Termux 배경색 커스터마이징
• 필수 유틸리티 명령어
• 강화된 termux-properties
• 기본 command-not-found 핸들러
• 지문 잠금 화면
• Termux-API 통합
• Termux-X11 환경 변수
```

> APT 의존성
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

> PIP 의존성
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
<summary><b>📀 명령어 목록</b></summary>

> **🔧 시스템**  
```bash
reload       │ 배너 시스템 재로드  
user-config  │ 커스터마이즈 센터
my           │ Stellar 프로필 표시
uninstall    │ 완전 제거  
update       │ GitHub에서 업데이트  
bash         │ 터미널 세션 재시작   
reset        │ 기본 상태로 복원
dstr         | rm -rf 단축 명령
move         | mv 단축 명령
copy         | cp 단축 명령
x11          | termux-x11 :0 & export DISPLAY=:0 단축 명령
```

> **🛠️ 유틸리티**  
```bash
ia           │ 무료 API AI 서비스  
ia-image     │ AI 이미지 생성기  
traductor    │ 실시간 번역기  
myip         │ 공인 IP 확인  
passwordgen  │ 안전한 비밀번호 생성  
encrypt-file │ 파일 암호화  
```

> **🌐 OSINT**  
```bash
ipinfo       │ IP 정보 분석  
urlinfo      │ URL 분석기  
userfinder   │ 크로스 플랫폼 사용자 검색  
phoneinfo    │ 전화번호 조회  
metadatainfo │ 파일 메타데이터 추출  
emailsearch  │ 이메일 검색  
```

> **📱 Discord**  
```bash
userinfo           │ 사용자 정보(ID)  
serverinfo         │ 서버 정보(ID)  
searchinvites      │ 초대 링크 검색  
inviteinfo         │ 초대 분석  
role-mapper        │ 역할 권한 매핑  
mutual-servers     │ 공통 서버  
webhook-mass-spam  │ 웹훅 스팸  
mass-delete-channels │ 채널 대량 삭제  
```

> **📸 Instagram**  
```bash
profileinfo  │ 프로필 메타데이터  
```

> **⚡ 침투 테스트**  
```bash
ddos        │ DDoS 공격(IP+포트)  
```
</details>

<details>
<summary><b>📄 사용 가이드</b></summary>

설치 후 `user-config`로 다음을 커스터마이즈:
- 배너 ASCII 아트
- 컬러 스킴
- 터미널 배경 (라이트/다크 모드)
- 기타 시각 요소

인터랙티브 커스터마이즈 마법사 제공
</details>

<details>
<summary><b>🌹 제작자</b></summary>

```diff
+ Keiji821 (리드 개발자)
```

##### 협업/문의

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

##### `❤️` 후원

프로젝트를 지원하려면:

[![Binance 후원](https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=후원&labelColor=black&message=763579717)](https://pay.binance.com/en)

[![PayPal 후원](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white&label=후원&labelColor=003087&message=felixdppdcg69@gmail.com)](https://paypal.me/felixdppdcg69)
</details>