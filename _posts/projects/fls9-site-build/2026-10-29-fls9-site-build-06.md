---
layout: post
title: "폴스나인 사이트 제작기 6편 | 구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기"
categories:
  - projects
  - fls9-site-build
tags: [fls9-site-build, RSS, SEO, 네이버서치어드바이저, 사이트맵, 서치콘솔]
description: >
  폴스나인 사이트 제작기 6편. 구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기
date: 2026-10-29 19:17:45 +0900
permalink: /projects/fls9-site-build/06/
---
사이트를 열었으면 검색엔진에 '나 여기 있어요' 하고 알려 줘야 한다. 구글과 네이버 둘 다 했는데, 둘의 인증 방식이 달라서 따로 적는다.

## 구글 서치콘솔 — 도메인 속성 + Cloudflare 자동 인증

1. 속성 추가에서 **도메인** 유형을 고르고 도메인만 입력(https 없이)
2. DNS 인증 화면에서 공급업체로 **Cloudflare**를 고르면 승인 창이 뜬다 → **Authorize**. TXT 레코드가 자동으로 들어가서 손댈 게 없다
3. 인증 후 왼쪽 **Sitemaps**에 사이트맵 제출

> ⚠️ **삽질 포인트**
>
> 도메인 속성은 사이트맵 칸에 **전체 주소**(https://fls9.kr/sitemap.xml)를 넣어야 한다. 제출 직후 '가져올 수 없음'이 떠도 몇 시간 뒤 '성공'으로 바뀌니 놀라지 말 것.

## 네이버 서치어드바이저 — HTML 태그

1. 사이트 등록 칸에 https://도메인 입력
2. 소유확인 방법은 **HTML 태그** → meta 태그 한 줄을 복사
3. 사이트 생성기의 head 부분에 그 한 줄을 넣고 배포(1~2분)
4. 네이버 화면에서 **소유확인** 클릭
5. **요청 → 사이트맵 제출**에 sitemap.xml, **RSS 제출**에 rss.xml

메타 태그는 모든 페이지에 들어가야 해서, 글 하나에 넣는 게 아니라 사이트 생성기의 공통 head에 넣었다. RSS까지 제출해 두면 새 글이 더 빨리 수집된다고 해서 같이 넣었다.

## 사이트맵·RSS는 생성기가 자동으로

글을 쓸 때마다 sitemap.xml, rss.xml을 손으로 고칠 순 없으니까 빌드할 때 자동으로 만들게 했다. 리그별 목록 페이지가 새로 생기면 그것도 자동으로 사이트맵에 들어간다.

> 💡 **한 줄 정리**
>
> 구글은 Cloudflare 버튼 한 번, 네이버는 메타 태그 한 줄. 둘 다 사이트맵 + (네이버는) RSS까지!

> 📚 **폴스나인 사이트 제작기**
>
> 1. [티스토리를 떠나 내 사이트를 만들기로 한 이유](/projects/fls9-site-build/01/)
> 2. [가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경](/projects/fls9-site-build/02/)
> 3. [Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지](/projects/fls9-site-build/03/)
> 4. [Pages에 내 도메인 붙이기 — 루트와 www, SSL까지](/projects/fls9-site-build/04/)
> 5. [무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing](/projects/fls9-site-build/05/)
> 6. **구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기 (지금 글)**
> 7. [서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1](/projects/fls9-site-build/07/)
> 8. [예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포](/projects/fls9-site-build/08/)
> 9. [모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대](/projects/fls9-site-build/09/)
> 10. [하루 만에 블로그에서 사이트로 — 회고와 다음 계획](/projects/fls9-site-build/10/)

이상으로 6편을 마칩니다~~ 다음 편은 서버 없이 댓글 달기다. 이번 연재에서 제일 재밌었던 부분이다 햐~

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-6%ED%8E%B8-%EA%B5%AC%EA%B8%80-%EC%84%9C%EC%B9%98%EC%BD%98%EC%86%94%C2%B7%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%84%9C%EC%B9%98%EC%96%B4%EB%93%9C%EB%B0%94%EC%9D%B4%EC%A0%80%EC%97%90-%EC%83%88-%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%93%B1%EB%A1%9D%ED%95%98%EA%B8%B0 -->
