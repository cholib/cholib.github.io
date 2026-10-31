---
layout: post
title: "폴스나인 사이트 제작기 9편 | 모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대"
categories:
  - archives
  - fls9-site-build
tags: [fls9-site-build, CSS, UX, word-break, 모바일, 반응형, 한글줄바꿈]
description: >
  폴스나인 사이트 제작기 9편. 모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대
date: 2026-10-29 19:18:21 +0900
permalink: /projects/fls9-site-build/09/
---
기능을 다 붙이고 폰으로 열어 보니... 어색한 데가 한두 군데가 아니었다. 이번 편은 CSS로 하나씩 고친 기록이다. 특히 **한글 줄바꿈**은 꼭 보고 가시길.

## 1. 문단 오른쪽이 들쭉날쭉

한글은 `word-break: keep-all`을 주면 단어(어절) 중간에서 안 끊겨서 PC에선 깔끔하다. 그런데 폰처럼 좁은 화면에선 '10라운드경기다.' 같은 긴 어절이 통째로 다음 줄로 넘어가서 앞줄 오른쪽에 큰 구멍이 생긴다.

```css
@media (max-width: 600px) {
  .entry p { word-break: normal; line-break: strict; text-align: justify; }
}
```

좁은 화면에서만 글자 단위로 줄을 채우고(word-break: normal) 양쪽 정렬을 줬다. 마침표·쉼표가 줄 맨 앞으로 오는 건 `line-break: strict`로 막았다. 신문·뉴스 앱에서 쓰는 방식이다.

> ⚠️ **삽질 포인트**
>
> 처음엔 `text-wrap: pretty`도 같이 넣었다. 마지막 줄이 외롭지 않게 해 준다길래. 그런데 **아이폰 사파리**에선 이게 앞줄들을 일부러 짧게 끊어서 오히려 더 들쭉날쭉해졌다. 빼니까 해결. 크롬 미리보기만 믿으면 안 된다!

## 2. 제목은 반대로 — 단어를 지키고 균형 있게

제목은 팀 이름이 잘리면 안 되니까 keep-all을 유지하고, 대신 `text-wrap: balance`로 두 줄의 길이를 비슷하게 맞췄다. 제목 앞의 [리그명] 같은 꼬리표는 글 화면에선 작은 칩으로 빼서 제목 줄을 짧게 만들었다.

## 3. 표 폭이 제각각

같은 '점유율 50%'인데 표마다 칸 폭이 달라서 숫자가 막대 아래로 밀려나 있었다. 범인은 가로 스크롤을 주려고 표에 걸어 둔 `display: block`. 이러면 표가 '표'가 아니라 그냥 상자가 돼서 width: 100%가 먹지 않는다.

```text
<div class="tbl"><table>...</table></div>
.tbl { overflow-x: auto; }          /* 스크롤은 바깥 상자가 */
.tbl table { width: 100%; }        /* 표는 꽉 채우기 */
```

막대 그래프가 든 비교표는 `table-layout: fixed`로 양쪽 칸을 똑같이 만들고, 칸이 6개 넘는 순위표는 `:has(tr > :nth-child(6))`로 골라 글자를 줄였다. :has() 선택자, 이럴 때 진짜 편하다.

## 4. 읽기 편의 장치

- **읽기 진행 막대**: 헤더 아래 4px 코랄색 막대가 본문(.entry)을 읽은 만큼 찬다. 페이지 전체가 아니라 본문 기준이라 댓글 영역은 계산에서 빠진다
- **맨 위로 버튼**: 한 화면쯤 내려가면 오른쪽 아래에 나타난다. 둘레 고리가 읽은 만큼 차오른다. 아이폰 홈 바에 안 가리게 `env(safe-area-inset-bottom)`을 썼다
- **파비콘 세트**: SVG 하나로는 부족해서 favicon.ico(16·32·48), 아이폰 홈 화면용 180px, 안드로이드용 192·512px, 웹 매니페스트까지 만들었다

> 💡 **한 줄 정리**
>
> 한글 본문: 좁은 화면은 글자 단위 + 양쪽 정렬. 제목: 단어 단위 + balance. 그리고 꼭 실제 아이폰으로 확인!

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
> 9. **모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대 (지금 글)**
> 10. [하루 만에 블로그에서 사이트로 — 회고와 다음 계획](/projects/fls9-site-build/10/)

이상으로 9편을 마칩니다~~ 마지막 편은 하루를 돌아보는 회고다.

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-9%ED%8E%B8-%EB%AA%A8%EB%B0%94%EC%9D%BC%EC%97%90%EC%84%9C-%ED%95%9C%EA%B8%80%EC%9D%B4-%EC%98%88%EC%81%98%EA%B2%8C-%EB%B3%B4%EC%9D%B4%EA%B2%8C-%E2%80%94-%EC%A4%84%EB%B0%94%EA%BF%88%C2%B7%ED%91%9C%C2%B7%EC%9D%BD%EA%B8%B0-%EC%A7%84%ED%96%89-%EB%A7%89%EB%8C%80 -->
