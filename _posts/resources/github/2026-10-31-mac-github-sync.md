---
layout: post
title: "GitHub | 맥미니 ↔ GitHub 동기화에서 배운 것 — 체크리스트와 사고 기록"
categories:
  - resources
  - github-ref
tags: [github-ref, git, GitHub, 동기화, 트러블슈팅]
description: >
  여러 작업이 한 저장소를 함께 고칠 때 맥미니와 GitHub이 어긋나지 않게 하는 규칙과, 실제로 겪은 문제·해결법.
date: 2026-10-31 23:10:00 +0900
permalink: /resources/github/mac-github-sync/
---
폴스나인은 예약 작업 여러 개와 대화 여러 개가 같은 저장소를 고친다. 그러다 보니 맥미니와 GitHub이 몇 번 어긋났다. 다시 꺼내 볼 수 있게 규칙과 해결법을 정리한다.

## 원칙 세 줄

1. **GitHub main이 정본이다.** 맥미니도, 클라우드 작업 공간도 GitHub을 따라간다.
2. **시작 전에 받고, 끝나면 올린다.** `git fetch` → 맞추기 → 작업 → 커밋 → push.
3. **자기 파일만 add 한다.** `git add -A`는 남의 작업 중인 파일까지 쓸어 담는다.

## 상태별 처리법

```bash
git fetch origin main
git status -sb      # ## main...origin/main [ahead N, behind M]
```

| 상태 | 처리 |
| --- | --- |
| 같음 | 끝 |
| 내 쪽만 앞섬 (ahead) | `git push origin HEAD:main` |
| GitHub만 앞섬 (behind) | `git merge --ff-only origin/main` |
| 둘 다 앞섬 (갈라짐) | 백업 브랜치 → `git rebase origin/main` → push |

갈라졌을 때는 먼저 백업 브랜치를 만든다.

```bash
git branch -f backup/mac-$(date +%Y%m%d%H%M) HEAD
git rebase origin/main
```

## 실제로 겪은 문제와 해결

> ⚠️ **잠금 파일 때문에 git이 멈춤**
>
> 맥미니의 공유 폴더는 기본적으로 파일 삭제가 막혀 있었다. git은 작업할 때 `.lock` 파일을 만들었다 지우는데, 못 지우니 다음 명령부터 'File exists'로 실패했다. → 그 폴더에 삭제 권한을 먼저 받고 git을 돌린다. 10분 넘게 남아 있는 `index.lock`은 찌꺼기이므로 지운다.

> ⚠️ **압축으로 옮기다 .git 객체 덮어쓰기 실패**
>
> 저장소를 tar로 묶어 옮길 때, `.git/objects` 파일은 읽기 전용이라 `--overwrite`가 실패했다. → 객체는 `--skip-old-files`로 새 것만 풀고, 나머지는 `--exclude objects`로 덮어쓴다. 지금은 압축으로 옮기지 않고 git으로 직접 맞춘다.

> ⚠️ **커밋 안 한 옛 초안이 길을 막음**
>
> 맥미니에 커밋 안 된 수정 39개가 남아 있었는데, 확인해 보니 **전부 GitHub에 더 새 버전이 있는 파일**이었다. 지우지 않고 `git stash`로 치워 두고 fast-forward 했다.
>
> 이어서 추적되지 않은 파일 13개가 merge를 막았다. GitHub의 같은 경로 파일과 내용이 같아서 치우고 진행했다. 내용이 다르면 따로 백업 폴더로 옮긴 뒤 진행한다.

> ⚠️ **맥미니에만 있는 커밋이 낡은 파일을 쓸어 담음**
>
> 맥미니에서 `git add -A`로 커밋하는 바람에, 다른 작업이 이미 GitHub에서 고친 파일의 옛 버전까지 함께 커밋됐다. → 맥미니 쪽에서 정말 필요한 폴더만 골라 GitHub에 반영하고, 맥미니는 백업 브랜치를 남긴 뒤 `reset --hard origin/main`.

> ⚠️ **토큰 권한은 저장소 단위**
>
> 맥미니의 토큰은 한 저장소 전용이라 다른 저장소에 push하니 403이 났다. 토큰 범위를 넓히거나, 그 저장소에 맞는 다른 연결 방법을 쓴다.

## 자동 동기화 작업이 하는 일

매시 55분에 도는 작업이 위 처리법을 그대로 한다.

1. 다른 작업이 진행 중이면(최근 잠금·압축 파일) 건너뛴다.
2. 커밋 안 된 수정이 있으면 60분이 지난 것만 추적 파일만(`git add -u`) 자동 커밋한다.
3. 상태에 따라 push / fast-forward / 백업 후 rebase.
4. 7일 넘은 백업 브랜치는 정리한다.
5. 문제가 있을 때만 알린다.

## 덤: 커밋 표시

- 커밋 메시지 맨 앞에 작업 방 머리표([사이트], [분석] 등)를 붙이면 `git log`만 봐도 누가 무엇을 했는지 보인다.
- 비어 있는 커밋으로 재배포하기: `git commit --allow-empty -m "재배포" && git push`
