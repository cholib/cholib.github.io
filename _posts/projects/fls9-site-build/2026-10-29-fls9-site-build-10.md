---
layout: post
title: "폴스나인 사이트 제작기 10편 | 하루 만에 블로그에서 사이트로 — 회고와 다음 계획"
categories:
  - projects
  - fls9-site-build
tags: [fls9-site-build, 개인프로젝트, 사이트제작, 자동화, 회고]
description: >
  폴스나인 사이트 제작기 10편. 하루 만에 블로그에서 사이트로 — 회고와 다음 계획
date: 2026-10-29 19:18:28 +0900
permalink: /projects/fls9-site-build/10/
---
자! 마지막 편이다. 아침에 '티스토리 보안문자 너무 귀찮다'에서 시작해서, 저녁엔 내 도메인에 댓글·조회수·예약 발행까지 붙은 사이트가 돌아가고 있었다. 하루를 돌아보며 정리해 본다.

## 하루 동안 만든 것

- 가비아 도메인 → Cloudflare DNS 이전
- 파이썬 사이트 생성기 + Cloudflare Pages 자동 배포
- 루트·www 도메인 연결, HTTPS
- contact@ 도메인 메일 전달
- 구글·네이버 검색 등록(사이트맵·RSS)
- 자체 댓글(답글·@멘션·IP 앞자리)·조회수·최신순/인기순 정렬
- 15시 예약 발행
- 카드형 디자인, 모바일 한글 줄바꿈, 읽기 진행 막대, 맨 위로 버튼, 파비콘 세트

## 제일 어려웠던 것 TOP 5

1. **Cloudflare 화면 찾기**: Workers와 Pages가 섞인 메뉴, 프로젝트 안에 숨은 Custom domains 탭. 기능보다 메뉴 위치가 더 어려웠다
2. **로그인 확인(Turnstile)**: 앱 내장 브라우저에선 끝까지 안 됐다. 평소 쓰는 브라우저로 바꾸는 게 답
3. **DNSSEC 창**: 네임서버 바꾸고 뜬 창에 뭘 넣어야 하나 고민했는데, 그냥 닫는 게 정답이었다
4. **모바일 한글**: keep-all, justify, text-wrap… 크롬과 사파리가 다르게 그린다
5. **스팸 필터 부작용**: 막으려던 패턴이 정상 기능(@멘션)까지 막았다

## 잘한 선택

- **서버를 안 빌린 것**: 정적 사이트 + 서버리스 함수로 비용 0원, 관리할 서버도 0대
- **원고를 GitHub에 둔 것**: 모든 수정 기록이 남고, 망쳐도 되돌릴 수 있다
- **개인정보를 처음부터 최소로**: IP는 암호화 값과 앞 두 자리만. 나중에 고치려면 훨씬 어렵다

## 다음 계획

- 글이 10편 넘게 쌓이면 최신순/인기순 정렬이 자동으로 열린다(이미 만들어 둠)
- 방문자가 늘면 회원·커뮤니티 게시판
- 애드센스 신청
- 맥미니가 GitHub와 알아서 동기화하게 만들기

그리고 이 티스토리는 이제 축구 대신 이런 **만들고 삽질한 기록**을 쌓는 곳이 된다. 축구 분석은 fls9.kr에서 계속된다. 혹시 같은 길을 가는 분이 있으면, 이 연재가 하루를 반나절로 줄여 주면 좋겠다.

> 📚 **폴스나인 사이트 제작기**
>
> 1. [티스토리를 떠나 내 사이트를 만들기로 한 이유](/projects/fls9-site-build/01/)
> 2. [가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경](/projects/fls9-site-build/02/)
> 3. [Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지](/projects/fls9-site-build/03/)
> 4. [Pages에 내 도메인 붙이기 — 루트와 www, SSL까지](/projects/fls9-site-build/04/)
> 5. [무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing](/projects/fls9-site-build/05/)
> 6. [구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기](/projects/fls9-site-build/06/)
> 7. [서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1](/projects/fls9-site-build/07/)
> 8. [예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포](/projects/fls9-site-build/08/)
> 9. [모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대](/projects/fls9-site-build/09/)
> 10. **하루 만에 블로그에서 사이트로 — 회고와 다음 계획 (지금 글)**

이상으로 폴스나인 사이트 제작기를 마칩니다~~ 끝까지 읽어 주셔서 감사합니다. 궁금한 점, 틀린 내용은 댓글로 꼭 알려 주세요!

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-10%ED%8E%B8-%ED%95%98%EB%A3%A8-%EB%A7%8C%EC%97%90-%EB%B8%94%EB%A1%9C%EA%B7%B8%EC%97%90%EC%84%9C-%EC%82%AC%EC%9D%B4%ED%8A%B8%EB%A1%9C-%E2%80%94-%ED%9A%8C%EA%B3%A0%EC%99%80-%EB%8B%A4%EC%9D%8C-%EA%B3%84%ED%9A%8D -->
