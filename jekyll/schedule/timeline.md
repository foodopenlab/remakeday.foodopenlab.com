---
layout: default
title: 단계별 개발 일정
permalink: /docs/schedule/timeline.html
parent: 5. 마일스톤&WBS
nav_order: 1
has_children: true
description: 2026-09-03부터 09-16 v1 공개까지의 14일 캘린더와 스프린트 경계, 그리고 v1 이후의 기록.
---

# 단계별 개발 일정

개발 시작 **2026-09-03**, v1 공개 **2026-09-16**. 하루마다 관문(gate)을 두고 기획서 12.3 절대 방어선 ①~⑤를 순서대로 넘었습니다. 관문을 못 넘기면 날짜를 미루는 대신 v1 범위를 먼저 닫고 이후에 확장합니다.

## 스프린트 경계

| 스프린트 | 기간 | 단계 | 일자별 기록 |
|---|---|---|---|
| Sprint 1 | 09.03 ~ 09.04 | 설계 | [Sprint 1 일자별 진행 사항]({{ '/docs/schedule/sprint1.html' | relative_url }}) |
| Sprint 2 | 09.05 ~ 09.12 | 구현 | [Sprint 2 일자별 진행 사항]({{ '/docs/schedule/sprint2.html' | relative_url }}) |
| Sprint 3 | 09.13 ~ 09.16 | 검증·v1 공개 | [Sprint 3 일자별 진행 사항]({{ '/docs/schedule/sprint3.html' | relative_url }}) |
| Sprint 4 | 09.17 ~ | v1 이후 | [Sprint 4 v1 이후 진행 사항]({{ '/docs/schedule/sprint4.html' | relative_url }}) |

## 14일 캘린더

| Day | 날짜 | 요일 | 단계 | 주제 | 관문 |
|:--:|---|:--:|---|---|---|
{% for d in site.data.schedule -%}
| {{ d.day }} | {{ d.date }} | {{ d.dow }} | {{ d.phase }} | {{ d.theme }} | {{ d.gate }} |
{% endfor %}

## v1 이후

v1 공개 뒤에도 개발은 계속됩니다. 2026-09-18에 사람 판 관찰을 재집계해 [연구 보고서]({{ '/docs/research.html' | relative_url }})에 반영했고, 09-24와 10-01의 [개발일지]({{ '/docs/devlog.html' | relative_url }})가 그 뒤를 잇습니다. 이후 작업은 [Sprint 4]({{ '/docs/schedule/sprint4.html' | relative_url }})에 누적합니다.
