---
layout: post
title: "폴스나인 사이트 제작기 7편 | 서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1"
categories:
  - projects
  - fls9-site-build
tags: [fls9-site-build, cloudflared1, PagesFunctions, 댓글, 서버리스, 스팸방지, 조회수]
description: >
  폴스나인 사이트 제작기 7편. 서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1
date: 2026-10-29 19:17:51 +0900
permalink: /projects/fls9-site-build/07/
---
정적 사이트의 약점은 '저장'이 안 된다는 거다. 댓글을 받으려면 어딘가에 데이터를 써야 한다. 외부 댓글 서비스도 봤는데 Giscus는 GitHub 로그인이 필요해서 축구 팬들은 못 쓰고, Disqus 무료판은 광고가 붙는다. 그래서 **직접 만들었다**. Cloudflare에 이미 다 있다.

## 구조

- **Pages Functions**: 저장소에 `functions/api/comments.js` 파일을 두면 /api/comments 주소에서 돌아가는 작은 서버 함수가 된다. 따로 서버를 안 띄워도 된다.
- **D1**: Cloudflare의 무료 SQLite 데이터베이스. 댓글과 조회수를 여기에 저장한다.

## Cloudflare에서 할 일 (클릭 몇 번)

1. **Storage & databases → D1 → Create** → 이름 정해서 생성(위치는 기본값)
2. 프로젝트 **Settings → Bindings → Add → D1 database** → 변수 이름 **DB**로 연결
3. **Settings → Variables and Secrets** → 관리자 키를 **Secret** 종류로 추가(값은 나만 아는 긴 문자열)
4. 재배포(3편의 빈 커밋 방법)

테이블은 SQL을 따로 넣지 않고, 첫 요청이 들어올 때 함수가 `CREATE TABLE IF NOT EXISTS`로 알아서 만들게 했다. 나중에 칸을 추가할 때도 `ALTER TABLE`을 한 번 시도하고 이미 있으면 넘어가게 해 두니 편했다.

> ⚠️ **삽질 포인트**
>
> **비회원 댓글 = 스팸 표적.** 특히 스포츠 사이트는 사설 도박 홍보가 바로 몰린다. 그래서 막는 장치를 겹겹이 넣었다.

- 링크·연락처가 든 댓글 차단(도메인 패턴, @아이디 패턴)
- 도박 홍보 단어 필터. 단, '슬롯(감독 자리)', '출장 정지'처럼 축구 얘기와 겹치는 단어는 일부러 뺐다
- 같은 사람 30초 안 연속 작성 금지, 하루 30개 제한
- 사람 눈엔 안 보이는 칸을 하나 숨겨 두고, 그 칸을 채운 요청(봇)은 조용히 무시
- '관리자', '폴스나인' 같은 닉네임 금지

## 개인정보는 최소로

도배를 막으려면 같은 사람인지 알아야 하는데, IP를 그대로 저장하긴 싫었다. 그래서 **IP + 날짜를 섞어 암호화한 값**만 저장한다. 하루가 지나면 값이 바뀌어서 추적이 안 된다. 사칭 방지용으로 닉네임 옆엔 **IP 앞 두 자리만**(211.234.\*\*\*.\*\*\*) 보여 주고, 저장도 앞 두 자리만 한다. 삭제용 비밀번호는 복원할 수 없는 해시로만.

> ⚠️ **삽질 포인트**
>
> **@멘션이 스팸 필터에 걸렸다.** 텔레그램 아이디를 막으려고 '@영문 4자 이상'을 차단했더니, 답글의 @john\_park 같은 영문 닉네임 멘션까지 막혔다. 같은 댓글 묶음에 실제로 있는 닉네임일 때만 검사에서 빼는 걸로 해결했다.

## 조회수도 같은 방식

글을 열면 `/api/views`에 한 번 기록한다. 같은 사람(하루 단위 암호화 값)이 같은 날 몇 번을 열어도 1회, 검색 로봇은 제외. 테이블의 기본키를 (글, 날짜, 사람)으로 잡고 `INSERT OR IGNORE` 한 줄이면 중복이 자동으로 걸러진다.

```sql
CREATE TABLE views (slug TEXT, day TEXT, who TEXT, PRIMARY KEY (slug, day, who));
INSERT OR IGNORE INTO views VALUES (?, ?, ?);
```

> 💡 **한 줄 정리**
>
> Pages Functions + D1이면 댓글·조회수 정도는 무료로 직접 만든다. 대신 스팸 대책은 처음부터!

> 📚 **폴스나인 사이트 제작기**
>
> 1. [티스토리를 떠나 내 사이트를 만들기로 한 이유](/projects/fls9-site-build/01/)
> 2. [가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경](/projects/fls9-site-build/02/)
> 3. [Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지](/projects/fls9-site-build/03/)
> 4. [Pages에 내 도메인 붙이기 — 루트와 www, SSL까지](/projects/fls9-site-build/04/)
> 5. [무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing](/projects/fls9-site-build/05/)
> 6. [구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기](/projects/fls9-site-build/06/)
> 7. **서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1 (지금 글)**
> 8. [예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포](/projects/fls9-site-build/08/)
> 9. [모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대](/projects/fls9-site-build/09/)
> 10. [하루 만에 블로그에서 사이트로 — 회고와 다음 계획](/projects/fls9-site-build/10/)

이상으로 7편을 마칩니다~~ 댓글 기능 써 보시고 이상한 점 있으면 그 댓글로 알려 주세요ㅎㅎ

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-7%ED%8E%B8-%EC%84%9C%EB%B2%84-%EC%97%86%EC%9D%B4-%EB%8C%93%EA%B8%80%C2%B7%EC%A1%B0%ED%9A%8C%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%E2%80%94-Cloudflare-Pages-Functions-D1 -->
