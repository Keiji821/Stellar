<p align="center"> <kbd> <img src="https://i.pinimg.com/originals/02/87/d3/0287d3ba8b3330fca99f69e2001d3168.gif?semt=ais_hybrid&w=740" width="420"> </kbd><br><br>

<div align="center">

![오픈소스](https://img.shields.io/badge/오픈소스-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white) ![유지보수중](https://img.shields.io/badge/유지보수중(예)-2ea44f?style=for-the-badge)

<h4>제작 기술:</h4>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Shell_스크립트-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
[![JavaScript Runtime](https://img.shields.io/badge/JavaScript_런타임-Node.js-yellow?style=for-the-badge&logo=javascript&logoColor=white&color=f7df1e&labelColor=000000)](https://nodejs.org/)

</div>

<div align="center">
    <img src="https://img.shields.io/badge/Stellar-6C00FF?style=for-the-badge&logo=stellar&logoColor=white&labelColor=121212"><br>
    <strong></strong>
</div>

<div align="center">

Stellar는 `Python`, `Bash`, `Node.js`로 개발된 프로그램으로, `Termux`의 기본적인 인터페이스를 개선하고 새로운 기능을 추가합니다.

해킹과 OSINT에 초점을 둔 몇 가지 도구를 포함하고 있지만, 주된 목적은 다양한 커스터마이징 옵션으로 Termux의 시각적 인터페이스를 향상시키는 것입니다.

</div>

#

⚠️ `출시 예정: 일본어, 중국어, 한국어, 영어, 포르투갈어 지원`

⚠️ `현재도 활발히 개발 중 - 일부 버그가 있을 수 있음`

`📌` Stellar에 기여하거나 버그/문제를 보고하려면 Discord에서 `keiji100`으로 연락주세요

#

<details>
<summary><b>🔖 설치 단계</b></summary>

##### Stellar를 설치하려면 다음 단계를 따르세요:

```shell script
git clone https://github.com/Keiji821/Stellar
```

```shell script
cd Stellar
```

```shell script
bash install.sh
```

##### `bash install.sh`를 실행하면 모든 것이 자동으로 설치됩니다(안정적인 인터넷 연결이 필요합니다). 설치가 완료되면 Termux 세션이 재시작됩니다. TOR가 정상적으로 작동하려면 Termux를 완전히 종료한 후 다시 여는 것이 좋습니다.

</details>

<details>
<summary><b>📑 기능 목록</b></summary>

##### Stellar OS는 OSINT와 해킹에 초점을 둔 명령어 세트를 제공합니다(모두 선택사항). 주된 목표는 여전히 Termux 커스터마이징입니다.

#### `🔧` 시스템
| 명령어       | 설명 |  
|--------------|-------------|  
| `reload`     | 시스템 배너 다시 불러오기 |  
| `ui`         | 배너 모양과 색상 커스터마이징 |  
| `uninstall`  | Stellar 완전히 제거 |  
| `update`     | GitHub에서 Stellar 업데이트 |  
| `bash`       | 터미널 세션 재시작 |  
| `history -c` | 명령어 기록 삭제 |  
| `reset`      | 터미널을 기본 상태로 초기화 |  
| `my`         | Stellar 프로필 표시 |  
| `userconf`   | Stellar 프로필 설정 |  

#### `🛠️` 유틸리티
| 명령어         | 설명 |  
|----------------|-------------|  
| `ia`           | 무료 AI API 서비스 |  
| `ia-image`     | AI 이미지 생성기 |  
| `translator`   | 실시간 번역 |  
| `myip`         | 공인 IP 표시 |  
| `passwordgen`  | 안전한 비밀번호 생성 |  
| `encrypt-file` | 파일 암호화 도구 |  

#### `📡` OSINT (정보 수집)  
| 명령어         | 설명 |  
|----------------|-------------|  
| `ipinfo`       | IP 주소 정보 조회 |  
| `urlinfo`      | URL 분석 도구 |  
| `userfinder`   | 여러 플랫폼에서 사용자 검색 |  
| `phoneinfo`    | 전화번호 조회 |  
| `metadatainfo` | 파일 메타데이터 추출 |  
| `emailsearch`  | 이메일 검색 도구 |  

#### `📱` Discord
| 명령어                | 설명 |  
|-----------------------|-------------|  
| `userinfo`            | 사용자 정보 조회(ID 사용) |  
| `serverinfo`          | 서버 정보 조회(ID 사용) |  
| `searchinvites`       | Discord 초대 링크 검색 |  
| `inviteinfo`          | 초대 링크 분석 |  
| `role-mapper`         | 서버 역할 매핑(서버 ID 필요) |  
| `mutual-servers`      | 사용자 간 공통 서버 확인 |  
| `webhook-mass-spam`   | 웹훅 대량 스팸 도구 |  
| `mass-delete-channels`| 채널 대량 삭제(자신의 서버만) |  

#### `📸` Instagram OSINT 
| 명령어        | 설명 |  
|---------------|-------------|  
| `profileinfo` | Instagram 프로필 메타데이터 추출 |  

#### `🛡️` 침투 테스트 
| 명령어    | 설명 |  
|-----------|-------------|  
| `ddos`    | DDoS 공격 도구(IP+포트) |  
| `tunnel`  | 방문자 IP를 캡처하는 이미지 호스팅 |  

##### Stellar는 백그라운드에서 TOR를 지속적으로 실행하여 익명성을 보호합니다.

</details>

<details>
<summary><b>📄 사용 가이드</b></summary>

##### 사용법은 간단합니다. 설치 후 평소처럼 Termux를 사용하면 됩니다. `ui` 명령어로 다음을 커스터마이징할 수 있습니다:
- ASCII 아트 표시
- 색상 구성
- 배경 색상(라이트/다크 테마 포함)

##### `ui` 명령어는 Termux 테마 전체를 커스터마이징할 수 있으며, 다크에서 라이트/블루 배경 등으로 변경할 수 있습니다.

</details>

#

# `🖋️` 제작자

```diff
+ Keiji821 (개발자)
```

##### 질문이나 협업 요청은 아래로 연락주세요

<p align="left">
  <a href="https://discord.com/users/983476283491110932">
<img src="https://img.shields.io/badge/Discord-Keiji-%235865F2?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</p>

##### `❤️` 후원 안내

이 프로젝트가 마음에 드시고 유용하게 사용하셨다면, 개발을 지원해주세요. 금액은 자유롭게 정하실 수 있습니다.

[![Binance 후원](https://img.shields.io/badge/Binance%20Pay-F0B90B?style=for-the-badge&logo=binance&logoColor=white&label=후원하기&labelColor=black&message=763579717)](https://pay.binance.com/en)

[![PayPal 후원](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white&label=후원하기&labelColor=003087&message=felixdppdcg69@gmail.com)](https://paypal.me/felixdppdcg69)
