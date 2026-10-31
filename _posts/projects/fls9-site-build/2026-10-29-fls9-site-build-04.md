---
layout: post
title: "폴스나인 사이트 제작기 4편 | Pages에 내 도메인 붙이기 — 루트와 www, SSL까지"
categories:
  - projects
  - fls9-site-build
tags: [fls9-site-build, CloudflarePages, dns, SSL, WWW, 커스텀도메인]
description: >
  폴스나인 사이트 제작기 4편. Pages에 내 도메인 붙이기 — 루트와 www, SSL까지
date: 2026-10-29 19:17:07 +0900
permalink: /projects/fls9-site-build/04/
---
4편은 짧고 굵다. xxx.pages.dev로 열리던 사이트를 fls9.kr로 열리게 만드는 단계다. 2편에서 네임서버를 Cloudflare로 넘겨 놨으니 버튼 몇 번이면 끝난다.

## 순서

1. **Compute → Workers & Pages** → 내 프로젝트 클릭
2. 위쪽 탭 **Custom domains** → **Set up a custom domain**
3. 루트 도메인(fls9.kr) 입력 → Continue → **Activate domain**
4. 같은 방법으로 **www.fls9.kr**도 따로 추가

> ⚠️ **삽질 포인트**
>
> **Custom domains 탭이 어디 있냐**로 한참 헤맸다. 왼쪽 'Domains' 메뉴(도메인 목록)에는 없다. 반드시 **Workers & Pages → 프로젝트 안**으로 들어가야 탭이 보인다.
>
> **www는 자동으로 안 붙는다.** 루트만 추가해 두고 www가 왜 안 열리나 했는데, www도 하나 더 추가해야 한다. 인증서 발급에 10~30분 걸렸다.
>
> 그동안 목록이 텅 비어 보인 적도 있었다. 프로젝트가 지워진 게 아니라 화면을 잘못 불러온 거라 새로고침하니 돌아왔다.

## SSL은 신경 쓸 게 없다

도메인을 붙이면 Cloudflare가 HTTPS 인증서를 알아서 발급하고 갱신한다. 상태가 Verifying → Active로 바뀌면 끝. 몇 분 걸렸다.

## 정본 주소는 하나로

fls9.kr과 www.fls9.kr이 둘 다 열리면 검색엔진이 같은 글을 두 번 볼 수 있다. 그래서 사이트의 모든 페이지에 **canonical(정본 주소)**을 fls9.kr 쪽으로 박아 뒀다. 이러면 중복 문제는 없다.

```text
<link rel="canonical" href="https://fls9.kr/posts/...">
```

> 💡 **한 줄 정리**
>
> 도메인 추가는 루트 하나, www 하나. 각각 따로!

> 📚 **폴스나인 사이트 제작기**
>
> 1. [티스토리를 떠나 내 사이트를 만들기로 한 이유](/projects/fls9-site-build/01/)
> 2. [가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경](/projects/fls9-site-build/02/)
> 3. [Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지](/projects/fls9-site-build/03/)
> 4. **Pages에 내 도메인 붙이기 — 루트와 www, SSL까지 (지금 글)**
> 5. [무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing](/projects/fls9-site-build/05/)
> 6. [구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기](/projects/fls9-site-build/06/)
> 7. [서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1](/projects/fls9-site-build/07/)
> 8. [예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포](/projects/fls9-site-build/08/)
> 9. [모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대](/projects/fls9-site-build/09/)
> 10. [하루 만에 블로그에서 사이트로 — 회고와 다음 계획](/projects/fls9-site-build/10/)

이상으로 4편을 마칩니다~~ 다음 편은 contact@ 도메인 메일 만들기다. 이거 무료다 진짜..

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-4%ED%8E%B8-Pages%EC%97%90-%EB%82%B4-%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%B6%99%EC%9D%B4%EA%B8%B0-%E2%80%94-%EB%A3%A8%ED%8A%B8%EC%99%80-www-SSL%EA%B9%8C%EC%A7%80 -->
