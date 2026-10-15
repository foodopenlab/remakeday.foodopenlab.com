---
layout: default
title: 5. 마일스톤&WBS
permalink: /docs/wbs.html
nav_order: 5
has_children: true
description: 14일 집중 개발로 v1을 공개하고 이후 계속 개발 중인 REMAKE DAY의 스프린트 로드맵과 과제 보드.
---

# 5. 마일스톤&WBS

REMAKE DAY는 2026-09-03부터 14일 동안 집중 개발해 2026-09-16에 v1을 공개했습니다. 14일은 설계(Sprint 1) → 구현(Sprint 2) → 검증·v1 공개(Sprint 3) 세 스프린트로 나뉘고, 공개 이후의 작업은 종료일 없는 Sprint 4에 누적합니다. 아래 로드맵과 보드는 `_data/project_sprints.yml`의 과제 210건을 영역(프론트·백엔드·AI 에이전트·평가·QA·릴리스·시나리오·콘텐츠)별로 보여 줍니다.

## 스프린트 로드맵

{% include sprint-roadmap.html %}

## 스프린트 보드

{% include sprint-boards.html %}

## 더 보기

- [단계별 개발 일정]({{ '/docs/schedule/timeline.html' | relative_url }}) — 14일 캘린더와 스프린트별 일자 기록
- [위험 관리 방안]({{ '/docs/schedule/risk.html' | relative_url }})
