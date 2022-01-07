---
layout: post
title: "[Tip] 구글 크롬 원격지원"
category: etc
tags: chromeRemoteControl
image: /assets/img/etc/chrome_remote_host/chrome_remote_desktop.jpg
accent_image: 
  background: url('/assets/img/etc/chrome_remote_host/chrome.png') center/cover
  overlay: false
accent_color: '#ccc'
theme_color: '#ccc'
description: >
  Chrome 원격 데스크톱으로 다른 컴퓨터에 액세스하기
invert_sidebar: true  
date: 2022-01-05
last_modified_at: 2022-01-07
---

<details>
<summary>🧾 Prologue (접기/펼치기)</summary>
<div markdown="1">

<br>

민지아빠🙋‍♂️: "와이프 노트북에 OOO프로그램이 없는지 다른 사람한테서 받은 파일이 안 봐지는 것 같다고 하네. 니가 내일 만나서 밥 먹으면서 좀 봐죠."<br>

조연어👨‍💻: "어..원격으로 하까? 🤣"<br>

<br>

</div>
</details>
<br>

__내 PC의 화면을__ <span style="color:skyblue">__구글 원격 데스크톱__</span> __으로 연결하여 원격을 허용한 상대에게 공유 할 수 있습니다.__<br>

__사용 가능한 [🔗구글 계정](https://support.google.com/accounts/answer/27441?hl=ko){:target="_blank"}이 있고, PC에 [🔗크롬](https://www.google.co.kr/chrome/?brand=IBEF&gclid=Cj0KCQiAoNWOBhCwARIsAAiHnEhIcn-j6LTHgXHodIrWuh5b0hUhREEyzZEw1OcuY9twvVRHewBPT7gaApkiEALw_wcB&gclsrc=aw.ds){:target="_blank"}이 설치되어 있다면 아래와 같이 진행하시면 되겠습니다.__<br>

* this unordered seed list will be replaced by the toc
{:toc}

## 🔍 검색 

### 구글에서 원격지원 검색
![search_chrome_remote_access](/assets/img/etc/chrome_remote_host/search_chrome_remote_access.PNG){:.border.lead width="1776" height="258" loading="lazy"}

구글 검색창에서 위와 같이 "***구글원격지원***" 이라고 입력 하신후 엔터키(혹은, 검색입력창 우측의 돋보기 버튼 클릭)를 치면, "***Chrome 원격 데스크톱 - Google***"이라는 검색결과 최상단에 확인 됩니다.<br><br>

## 🚀 내 화면 공유 코드 생성

### 1. 원격지원 화면 진입

"***Chrome 원격 데스크톱 - Google***"을 클릭하여 __[🔗Chrome 원격 데스크톱](https://support.google.com/accounts/answer/27441?hl=ko){:target="_blank"}__ 화면에 진입하고, 아래와 같이 ***내 화면 공유*** (<span style="color:red">__빨간색 테두리 표시__</span>)를 클릭🖱️합니다.<br><br>

![search_chrome_remote_access](/assets/img/etc/chrome_remote_host/select_share.PNG){:.border.lead width="1776" height="258" loading="lazy"}

구글 계정 로그인이 안 된 상태로 __내 화면 공유__ 를 클릭하시면, 아래와 같이 __계정 로그인__ 화면이 나오게 됩니다.<br><br>

|:------:|:------:|
|![First Image](/assets/img/etc/chrome_remote_host/insert_id.PNG){:.border.lead width="400" height="500" loading="lazy"}|![Second Image](/assets/img/etc/chrome_remote_host/insert_pw.PNG){:.border.lead width="400" height="500" loading="lazy"}|
|:------:|:------:|
| <small>[아이디 입력]</small> | <small>[비밀번호 입력]</small> |

당황하지 마시고🙂 등록하신 __구글 아이디__ 와 __비밀번호__ 를 입력하시면 됩니다.<br>

### 2. 공유 프로그램 다운로드 및 설치

로그인이 완료되면, 아래와 같이 상대방과 화면을 공유할 코드를 생성하기 위해 __원격지원__ 화면으로 진입하게 됩니다.<br>

![select_share_screen](/assets/img/etc/chrome_remote_host/select_share_screen.png){:.border.lead width="1776" height="258" loading="lazy"}

그리고 위의 <span style="color:red">__빨간색 테두리 표시__</span>로 된  __이기기 화면 공유__ 모듈에서 체크<span style="color:red">__✔__</span> 표시된 다운로드 버튼을 클릭해 주세요.<br>

체크하시면 아래와 같이 화면공유를 위한 프로그램을 PC에 저장하시면 됩니다.<br>

![download_hostprogram](/assets/img/etc/chrome_remote_host/download_hostprogram.png){:.border.lead width="1776" height="258" loading="lazy"}

다운로드가 완료되면 아래와 같이 *동의 및 설치* 버튼을 클릭해 주세요.🙂<br>

![install](/assets/img/etc/chrome_remote_host/install.png){:.border.lead width="1776" height="258" loading="lazy"}

클릭하시고 나면, 브라우저 상단의 작은 알림창에 __다운로드된 파일 열기__ 를 허용하도록 요청이 표시되는데요. 아래와 같이 <span style="color:skyblue">__예__</span> 를 클릭하시면 됩니다.<br>

![permit](/assets/img/etc/chrome_remote_host/permit.png){:.border.lead width="1776" height="258" loading="lazy"}

설치 완료 후 실행이 되는 동안, 아래처럼 화면 하단 윈도우 작업표시줄에 방패모양으로 노란색으로 깜빡깜빡하는 아이콘을 클릭하시면 원격프로그램 설치 및 설정이 완료됩니다.<br>

![permit](/assets/img/etc/chrome_remote_host/Request_for_permission.png){:.border.lead width="1776" height="258" loading="lazy"}

### 3. 화면 공유 코드 생성 

화면에 있는 ***+ 코드 생성*** 버튼을 을 클릭🖱️하여 코드를 생성합니다.<br>

![complete_install](/assets/img/etc/chrome_remote_host/complete_install.png){:.border.lead width="1776" height="258" loading="lazy"}

그러면 아래 <span style="color:red">__빨간색 테두리 표시__</span> 안에 보시는 것과 같이 일회성 액세스 코드가 생성됩니다.<br>

이 코드를 화면을 공유할 다른 사용자에게 알려주시고, 액세스될 동안 잠시 기다리시면 됩니다.<br>

![share_access_code](/assets/img/etc/chrome_remote_host/share_access_code.png){:.border.lead width="1776" height="258" loading="lazy"}

생성된 코드는 __<u>5분간 유효</u>__ 하므로 5분 이내에 상대방이 접속하지 않으면 코드 생성을 버튼을 다시 클릭해서 전달하시면 되겠습니다.<br><br>

## 🧑‍💻 화면 연결 완료

### 화면 공유 상태로 진입

내 PC의 화면이 상대방에게 성공적으로 공유완료되면, 아래와 같이 화면 하단에 상대방과 화면을 공유하고 있다고 표시됩니다.<br><br>

![complete_connection](/assets/img/etc/chrome_remote_host/complete_connection.PNG){:.border.lead width="1776" height="258" loading="lazy"}

__원거리에 계시는 가족과 친구의 PC 설정을 도와드릴 경우에 가끔 사용하게 되는데, 굉장히 편리한 것 같습니다.__🙂<br><br>

~~*이 글은 삼십년지기의 사소한 부탁을 위해 정성스럽게 작성되었습니다..*🤣~~<br>

"끝"<br><br>

[🔼TOP](#)

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="크리에이티브 커먼즈 라이선스" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>이 저작물은 <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">크리에이티브 커먼즈 저작자표시-비영리-변경금지 4.0 국제 라이선스</a>에 따라 이용할 수 있습니다.


<!--link address-->

