---
layout: post
title: "폴스나인 사이트 제작기 3편 | Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지"
categories:
  - archives
  - fls9-site-build
tags: [fls9-site-build, CloudflarePages, Github, Python, 배포자동화, 정적사이트]
description: >
  폴스나인 사이트 제작기 3편. Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지
date: 2026-10-29 19:17:00 +0900
permalink: /projects/fls9-site-build/03/
---
3편은 사이트를 실제로 인터넷에 올리는 단계다. 사이트 코드는 GitHub 저장소에 있고, Cloudflare Pages가 그걸 가져다 빌드해서 배포한다. 한 번 연결해 두면 **GitHub에 올리기만 하면 1~2분 뒤 사이트가 바뀐다**. 이게 진짜 편하다.

## 사이트 생성기는 파이썬 한 파일

Hugo, Next.js 같은 도구도 있지만 나는 **python3만으로 도는 생성기**를 택했다. 글 원고(JSON) 폴더를 읽어서 홈·카테고리·글 페이지, 사이트맵, RSS를 site/dist 폴더에 만들어 낸다. Cloudflare 빌드 환경에 python3가 기본으로 있어서 따로 설치할 게 없다.

```text
빌드 명령:      python3 site/build.py
빌드 결과 폴더: site/dist
```

## Pages 프로젝트 만들기

1. **Compute → Workers & Pages** → Create
2. 위쪽 버튼들은 Workers용이다. **맨 아래 'Continue to Pages' 링크**를 눌러야 한다
3. **Import an existing Git repository** → GitHub 연결 승인(저장소는 필요한 것 하나만 선택)
4. 저장소 선택 → Framework preset **None**, 빌드 명령·결과 폴더 입력 → **Save and Deploy**
5. 끝나면 xxx.pages.dev 주소가 생긴다

> ⚠️ **삽질 포인트**
>
> **① Workers와 Pages가 한 화면에 섞여 있다.** 처음 화면의 큰 버튼(Connect GitHub)은 Workers용이라 빌드 설정이 다르다. Pages는 맨 아래 작은 링크로 들어가야 한다.
>
> **② 이메일 인증을 안 하면 Git 연결이 막힌다.** 가입하고 인증 메일을 안 눌러 둬서 한 번 헛돌았다. 화면 위 파란 배너가 그 신호다.
>
> **③ 앱 안의 브라우저에서는 로그인 확인(Turnstile)이 계속 실패했다.** 'There was a problem with verification'만 반복. 평소 쓰는 크롬에서 하니 바로 됐다.
>
> **④ 브랜치 칸의 빨간 오류**는 GitHub 승인 직후 목록을 못 불러온 것뿐이었다. 배포에는 영향이 없었다.

## 재배포하고 싶을 때

설정(환경변수·DB 연결)을 바꾸면 다시 배포해야 반영된다. Deployments 탭의 ⋯ 메뉴에 Retry deployment가 있다는데 그 메뉴를 한참 찾았다..ㅎㅎ 더 쉬운 방법은 **GitHub에 빈 커밋을 하나 올리는 것**이다. 그러면 Pages가 알아서 새로 빌드한다.

```text
git commit --allow-empty -m "재배포"
git push
```

> 💡 **한 줄 정리**
>
> GitHub = 원고 보관함, Pages = 자동 인쇄소. 보관함에 원고를 넣으면 인쇄소가 알아서 새로 찍는다.

> 📚 **폴스나인 사이트 제작기**
>
> 1. [티스토리를 떠나 내 사이트를 만들기로 한 이유](/projects/fls9-site-build/01/)
> 2. [가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경](/projects/fls9-site-build/02/)
> 3. **Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지 (지금 글)**
> 4. [Pages에 내 도메인 붙이기 — 루트와 www, SSL까지](/projects/fls9-site-build/04/)
> 5. [무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing](/projects/fls9-site-build/05/)
> 6. [구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기](/projects/fls9-site-build/06/)
> 7. [서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1](/projects/fls9-site-build/07/)
> 8. [예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포](/projects/fls9-site-build/08/)
> 9. [모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대](/projects/fls9-site-build/09/)
> 10. [하루 만에 블로그에서 사이트로 — 회고와 다음 계획](/projects/fls9-site-build/10/)

이상으로 3편을 마칩니다~~ 다음 편은 이 pages.dev 사이트에 진짜 도메인을 붙이는 이야기다.

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-3%ED%8E%B8-Cloudflare-Pages%EB%A1%9C-%EC%A0%95%EC%A0%81-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0-%E2%80%94-GitHub-%EC%97%B0%EA%B2%B0%EB%B6%80%ED%84%B0-%EC%B2%AB-%EB%B0%B0%ED%8F%AC%EA%B9%8C%EC%A7%80 -->
