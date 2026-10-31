---
layout: post
title: "폴스나인 사이트 제작기 2편 | 가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경"
categories:
  - projects
  - fls9-site-build
tags: [fls9-site-build, dns, DNSSEC, 가비아, 개인도메인, 네임서버]
description: >
  폴스나인 사이트 제작기 2편. 가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경
date: 2026-10-29 19:16:53 +0900
permalink: /projects/fls9-site-build/02/
---
자! 2편은 도메인이다. fls9.kr은 가비아에서 샀는데, 사이트는 Cloudflare에서 돌릴 거라 **도메인 관리(DNS)를 Cloudflare로 넘겨야** 했다. 방법은 간단하다. 가비아에 적힌 '네임서버'를 Cloudflare가 주는 주소로 바꾸면 끝. 말은 쉬운데 화면이 좀 헷갈린다.

## 1. Cloudflare에 도메인 추가

1. Cloudflare 대시보드 → **Domains → Add a domain**에 도메인 입력
2. AI 크롤러 설정 화면이 나오면 **Search: Allow**는 꼭 유지(검색 노출·애드센스 심사 봇이 읽어야 한다)
3. 요금제는 맨 왼쪽 **Free**. 파란색으로 강조된 Pro는 안 골라도 된다
4. DNS 레코드 확인 화면 → **Continue**
5. 마지막에 나오는 **네임서버 두 개**(xxx.ns.cloudflare.com)를 메모

> ⚠️ **삽질 포인트**
>
> 내 도메인은 원래 티스토리에 연결돼 있어서, Cloudflare가 기존 레코드 두 줄(루트·www → host.tistory.io)을 가져왔다. 새 사이트로 옮길 거라 **두 줄 다 지웠다**. 새 레코드는 나중에 Pages에 도메인을 붙일 때 Cloudflare가 알아서 만든다.

## 2. 가비아에서 네임서버 바꾸기

1. 가비아 로그인 → **My가비아 → 도메인** → 해당 도메인 **관리**
2. 위쪽 탭 **네임서버/DNS호스트/DNSSEC** → 네임서버 **설정**
3. 기존 값(ns.gabia.co.kr 등)을 전부 지우고 Cloudflare가 준 두 개만 1차·2차에 입력
4. 소유자 인증(문자·메일)을 하라고 하면 하고 **적용**

> ⚠️ **삽질 포인트**
>
> 저장하고 나니 DNSSEC 입력 창이 떴다. 여기에 뭔가 넣어야 하나 싶었는데 **그냥 닫는 게 정답**이다. DNSSEC은 꺼져 있어야 하고, 여기에 값을 잘못 넣으면 오히려 연결이 깨진다. '기관이전 잠금 On'도 그대로 두면 된다. 네임서버 변경과는 상관없는, 도메인을 지켜 주는 설정이다.

## 3. Cloudflare에서 확인 요청

Cloudflare 화면으로 돌아와 **I updated my nameservers**를 누르면 상태가 Pending이 된다. 보통 몇 시간, 길면 하루라는데 나는 생각보다 빨리 **Active**가 됐다. 활성화되면 메일도 온다.

## 4. 잊지 말 것 — 티스토리 개인 도메인 해제

네임서버를 바꾸는 순간 그 도메인으로는 티스토리가 안 열린다. 티스토리 **관리 → 블로그 → 개인 도메인 설정**에서 연결을 해제해 두면 블로그는 원래 주소(xxx.tistory.com)로 계속 잘 열린다.

> 💡 **한 줄 정리**
>
> 가비아는 '도메인 산 곳', Cloudflare는 '도메인 관리하는 곳'. 둘을 잇는 게 네임서버 두 줄이다.

> 📚 **폴스나인 사이트 제작기**
>
> 1. [티스토리를 떠나 내 사이트를 만들기로 한 이유](/projects/fls9-site-build/01/)
> 2. **가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경 (지금 글)**
> 3. [Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지](/projects/fls9-site-build/03/)
> 4. [Pages에 내 도메인 붙이기 — 루트와 www, SSL까지](/projects/fls9-site-build/04/)
> 5. [무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing](/projects/fls9-site-build/05/)
> 6. [구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기](/projects/fls9-site-build/06/)
> 7. [서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1](/projects/fls9-site-build/07/)
> 8. [예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포](/projects/fls9-site-build/08/)
> 9. [모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대](/projects/fls9-site-build/09/)
> 10. [하루 만에 블로그에서 사이트로 — 회고와 다음 계획](/projects/fls9-site-build/10/)

이상으로 2편을 마칩니다~~ 가비아 화면에서 막히시면 댓글로 물어봐 주세요!

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-2%ED%8E%B8-%EA%B0%80%EB%B9%84%EC%95%84-%EB%8F%84%EB%A9%94%EC%9D%B8%EC%9D%84-Cloudflare%EB%A1%9C-%EC%98%AE%EA%B8%B0%EA%B8%B0-%E2%80%94-%EB%84%A4%EC%9E%84%EC%84%9C%EB%B2%84-%EB%B3%80%EA%B2%BD -->
