---
layout: post
title: "폴스나인 사이트 제작기 8편 | 예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포"
categories:
  - projects
  - fls9-site-build
tags: [fls9-site-build, cron, GithubActions, 예약발행, 자동화, 정적사이트]
description: >
  폴스나인 사이트 제작기 8편. 예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포
date: 2026-10-29 19:18:14 +0900
permalink: /projects/fls9-site-build/08/
---
티스토리엔 예약 발행 버튼이 있다. 정적 사이트엔 그런 게 없다. 페이지는 빌드할 때 만들어지니까, '15시에 공개'하려면 **15시에 한 번 더 빌드**를 해 줘야 한다.

## 아이디어

1. 글 원고에 발행 시각(date)을 적는다
2. 사이트 생성기는 date가 **지금보다 미래인 글은 빼고** 만든다
3. GitHub Actions가 매일 15:00(한국시간)에 깨어나서, 방금 발행 시각이 지난 글이 있으면 **빈 커밋**을 올린다
4. 빈 커밋을 본 Cloudflare Pages가 다시 빌드 → 그 글이 사이트에 나타난다

```yaml
on:
  schedule:
    - cron: "0 6 * * *"   # 15:00 KST (cron 은 UTC 기준!)
  workflow_dispatch: {}
permissions:
  contents: write
```

> ⚠️ **삽질 포인트**
>
> **cron은 UTC다.** 한국시간 15시는 UTC 6시. 처음에 15로 적을 뻔했다.
>
> **GitHub cron은 정각에 안 돈다.** 몇 분에서 수십 분 늦을 수 있다. 그래서 '지금으로부터 3시간 안에 발행 시각이 된 글'을 찾게 해서 늦게 깨어나도 놓치지 않게 했다. 오전 예약분용으로 09:05에도 한 번 더 돈다.
>
> 워크플로가 저장소에 커밋하려면 `permissions: contents: write`가 꼭 있어야 한다.

## 덤: 예약 글은 미리 고칠 수 있다

발행 전까지는 원고가 GitHub에만 있고 사이트엔 안 보인다. 그래서 15시 전에 GitHub 웹에서 원고를 열어 오타를 고쳐도 아무도 모른다ㅎㅎ 15시에 고친 버전으로 공개된다.

> 💡 **한 줄 정리**
>
> 정적 사이트 예약 발행 = 미래 날짜 글은 빌드에서 빼기 + 정해진 시각에 다시 빌드.

> 📚 **폴스나인 사이트 제작기**
>
> 1. [티스토리를 떠나 내 사이트를 만들기로 한 이유](/projects/fls9-site-build/01/)
> 2. [가비아 도메인을 Cloudflare로 옮기기 — 네임서버 변경](/projects/fls9-site-build/02/)
> 3. [Cloudflare Pages로 정적 사이트 배포하기 — GitHub 연결부터 첫 배포까지](/projects/fls9-site-build/03/)
> 4. [Pages에 내 도메인 붙이기 — 루트와 www, SSL까지](/projects/fls9-site-build/04/)
> 5. [무료로 contact@내도메인 메일 만들기 — Cloudflare Email Routing](/projects/fls9-site-build/05/)
> 6. [구글 서치콘솔·네이버 서치어드바이저에 새 도메인 등록하기](/projects/fls9-site-build/06/)
> 7. [서버 없이 댓글·조회수 만들기 — Cloudflare Pages Functions + D1](/projects/fls9-site-build/07/)
> 8. **예약 발행 만들기 — GitHub Actions cron으로 매일 15시 재배포 (지금 글)**
> 9. [모바일에서 한글이 예쁘게 보이게 — 줄바꿈·표·읽기 진행 막대](/projects/fls9-site-build/09/)
> 10. [하루 만에 블로그에서 사이트로 — 회고와 다음 계획](/projects/fls9-site-build/10/)

이상으로 8편을 마칩니다~~ 다음 편은 디자인 다듬기. 모바일 한글 줄바꿈 때문에 꽤 고생했다..

<!-- 원문: https://choho.tistory.com/entry/%ED%8F%B4%EC%8A%A4%EB%82%98%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%A0%9C%EC%9E%91%EA%B8%B0-8%ED%8E%B8-%EC%98%88%EC%95%BD-%EB%B0%9C%ED%96%89-%EB%A7%8C%EB%93%A4%EA%B8%B0-%E2%80%94-GitHub-Actions-cron%EC%9C%BC%EB%A1%9C-%EB%A7%A4%EC%9D%BC-15%EC%8B%9C-%EC%9E%AC%EB%B0%B0%ED%8F%AC -->
