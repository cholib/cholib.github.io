---
layout: post
title: "폴스나인 사이트 제작기 1편 | 티스토리를 떠나 내 사이트를 만들기로 한 이유"
categories:
  - archives
  - fls9-site-build
tags: [fls9-site-build, 개인도메인, 사이트제작, 정적사이트, 티스토리]
description: >
  폴스나인 사이트 제작기 1편. 티스토리를 떠나 내 사이트를 만들기로 한 이유
date: 2026-10-29 19:16:03 +0900
permalink: /projects/fls9-site-build/01/
---
자! 오늘부터 새 연재다. 이름하여 **폴스나인 사이트 제작기**. 축구 분석 블로그를 티스토리에서 굴리다가, 하루 만에 내 도메인(fls9.kr)으로 독립한 과정을 처음부터 끝까지 적어 본다. 개발 블로그라기보다는 '삽질 일지'에 가깝다. 막혔던 화면, 헤맸던 메뉴까지 솔직하게 다 적을 거다. 레스고~

## 왜 떠났나

티스토리는 시작하기엔 정말 편하다. 그런데 글을 매일 자동으로 올리기 시작하니까 벽이 하나씩 보였다.

- **보안문자**: 예약 발행을 걸어 둘 때마다 사람 확인 문자가 튀어나온다. 자동화하는 입장에선 이게 제일 큰 벽이었다.
- **디자인 한계**: 스킨을 아무리 고쳐도 '티스토리 느낌'이 남는다. 카드형 목록, 읽기 진행 막대 같은 걸 마음대로 넣기 어렵다.
- **하고 싶은 게 많아졌다**: 댓글을 내 방식대로, 나중엔 회원·커뮤니티까지. 남의 플랫폼 위에선 한계가 분명하다.

## 그래서 만든 구조

결론부터 말하면 **서버를 하나도 안 빌렸다**. 전부 무료 요금제로 돌아간다.

```text
글 원고(JSON) ─▶ GitHub 저장소 ─▶ Cloudflare Pages(자동 빌드) ─▶ fls9.kr
                                   └▶ Pages Functions + D1 (댓글·조회수)
```

- **가비아**: 도메인(fls9.kr)만 산 곳. 관리는 Cloudflare로 넘겼다.
- **GitHub**: 글 원고와 사이트 코드를 보관하는 '원고 보관함'.
- **Cloudflare Pages**: GitHub에 뭔가 올라가면 알아서 사이트를 다시 만들어 배포한다.
- **Cloudflare D1**: 댓글과 조회수를 저장하는 작은 데이터베이스.
- **파이썬 스크립트 하나**: 원고를 HTML 페이지로 바꾸는 사이트 생성기. 설치 없이 python3만 있으면 돈다.

> 💡 **한 줄 정리**
>
> 정적 사이트 + 서버리스 함수 구성이면 개인 블로그는 서버비 0원으로 충분히 굴러간다.

## 이 연재에서 다룰 것

하루 동안 한 일을 순서대로 쪼갰다. 가비아 네임서버 바꾸기부터 Cloudflare 배포, 도메인 메일, 검색엔진 등록, 댓글 서버, 예약 발행, 모바일 디자인 다듬기까지. 각 편마다 **막혔던 지점**을 따로 박스로 표시해 뒀다. 같은 길을 가는 분들은 그 박스만 봐도 시간 꽤 아낄 거다.

다음 편은 가비아에서 산 도메인을 Cloudflare로 옮기는 이야기다. 네임서버 바꾸는 거, 생각보다 화면이 헷갈린다..ㅎㅎ

> 📚 **폴스나인 사이트 제작기**
>
> 1. **티스토리를 떠나 내 사이트를 만들기로 한 이유 (지금 글)**
> 2. [가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경](/projects/fls9-site-build/02/)
> 3. [Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지](/projects/fls9-site-build/03/)
> 4. [Pages에 내 도메인 붙이기 — 루트와 www, SSL까지](/projects/fls9-site-build/04/)
> 5. [무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing](/projects/fls9-site-build/05/)
> 6. [구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기](/projects/fls9-site-build/06/)
> 7. [서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1](/projects/fls9-site-build/07/)
> 8. [예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포](/projects/fls9-site-build/08/)
> 9. [모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대](/projects/fls9-site-build/09/)
> 10. [하루 만에 블로그에서 사이트로 — 회고와 다음 계획](/projects/fls9-site-build/10/)

이상으로 1편을 마칩니다~~ 궁금한 점은 댓글로 편하게 남겨 주세요!

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-1%ED%8E%B8-%ED%8B%B0%EC%8A%A4%ED%86%A0%EB%A6%AC%EB%A5%BC-%EB%96%A0%EB%82%98-%EB%82%B4-%EC%82%AC%EC%9D%B4%ED%8A%B8%EB%A5%BC-%EB%A7%8C%EB%93%A4%EA%B8%B0%EB%A1%9C-%ED%95%9C-%EC%9D%B4%EC%9C%A0 -->
