---
layout: post
title: "폴스나인 사이트 제작기 5편 | 무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing"
categories:
  - archives
  - fls9-site-build
tags: [fls9-site-build, EmailRouting, mx레코드, 도메인메일, 스팸방지]
description: >
  폴스나인 사이트 제작기 5편. 무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing
date: 2026-10-29 19:17:38 +0900
permalink: /projects/fls9-site-build/05/
---
사이트 소개·문의 페이지에 연락처를 넣으려니 고민이 됐다. 전화번호는 스팸 전화 지옥이 될 거고, 개인 지메일을 그대로 쓰기도 싫었다. 그래서 만든 게 **contact@fls9.kr**. 메일함을 새로 만드는 게 아니라, 이 주소로 온 메일을 내 지메일로 **전달만** 해 주는 방식이다. 비용 0원!

## 설정 순서

1. Cloudflare → **Email → Email Routing** → **Onboard Domain** → 도메인 선택
2. MX 3개 + TXT 2개 레코드를 추가하겠다는 화면 → **Activate**
3. **Destination addresses** 탭 → 받을 지메일 추가 → 지메일로 온 인증 메일에서 **Verify**
4. **Routing rules** 탭 → **Create routing rule** → Email pattern에 contact, 도메인 선택, Action은 **Send to an email**, 받을 주소 선택 → Save
5. 다른 메일 계정에서 contact@으로 테스트 메일 보내 보기

레코드 의미도 짧게 적어 두면, **MX**는 '이 도메인으로 오는 메일은 Cloudflare가 받는다', **TXT**(SPF 등)는 '전달된 메일이 스팸으로 안 빠지게 보증한다'는 뜻이다. 사이트 접속용 레코드는 건드리지 않아서 사이트에는 영향이 없다.

> ⚠️ **삽질 포인트**
>
> **Catch-all은 꺼 두자.** 켜면 contact 말고 아무 주소(asdf@, admin@ …)로 온 메일까지 전부 들어와서 스팸이 폭증한다.
>
> **테스트는 다른 계정에서.** 같은 지메일에서 자기 자신에게 보내면 받은편지함에 안 뜰 수 있다.

## 페이지에 주소를 그대로 쓰면 안 되는 이유

페이지에 메일 주소를 글자 그대로 박아 두면 스팸 봇이 긁어 간다. 그래서 HTML에는 앞뒤를 쪼개 두고, 화면에 보일 때만 스크립트로 합쳤다. 문의 페이지엔 아예 'E-mail 문의' 버튼을 달아서 누르면 제목까지 채워진 메일 쓰기 창이 열리게 했다.

```html
<a class="mail" data-u="contact" data-d="fls9.kr">contact [at] fls9.kr</a>
<!-- 스크립트가 mailto:contact@fls9.kr?subject=[폴스나인 문의] 로 바꿔 준다 -->
```

> 💡 **한 줄 정리**
>
> 도메인 메일은 Email Routing으로 '전달'만. Catch-all은 끄고, 페이지엔 주소를 쪼개서.

> 📚 **폴스나인 사이트 제작기**
>
> 1. [티스토리를 떠나 내 사이트를 만들기로 한 이유](/projects/fls9-site-build/01/)
> 2. [가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경](/projects/fls9-site-build/02/)
> 3. [Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지](/projects/fls9-site-build/03/)
> 4. [Pages에 내 도메인 붙이기 — 루트와 www, SSL까지](/projects/fls9-site-build/04/)
> 5. **무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing (지금 글)**
> 6. [구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기](/projects/fls9-site-build/06/)
> 7. [서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1](/projects/fls9-site-build/07/)
> 8. [예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포](/projects/fls9-site-build/08/)
> 9. [모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대](/projects/fls9-site-build/09/)
> 10. [하루 만에 블로그에서 사이트로 — 회고와 다음 계획](/projects/fls9-site-build/10/)

이상으로 5편을 마칩니다~~ 다음 편은 구글·네이버에 사이트 등록하기!

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-5%ED%8E%B8-%EB%AC%B4%EB%A3%8C%EB%A1%9C-contact%EB%82%B4%EB%8F%84%EB%A9%94%EC%9D%B8-%EB%A9%94%EC%9D%BC-%EB%A7%8C%EB%93%A4%EA%B8%B0-%E2%80%94-Cloudflare-Email-Routing -->
