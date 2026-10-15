---
layout: default
title: 12. 개발일지
permalink: /docs/devlog.html
has_children: true
nav_order: 12
description: REMAKE DAY 개발일지 목록. 2026-09-03 킥오프부터 v1 공개(09-16)와 그 이후까지 날짜별 기록.
---

# 12. 개발일지

날짜별 개발 기록, 최신이 아래. 각 글은 그날의 결정·측정치·커밋 상태를 그대로 적은 것이라 수치와 커밋 해시는 당시 기준입니다.

| 날짜 | 제목 | 링크 |
|---|---|---|
| 2026-09-03 | 킥오프 — 14일 안에 무엇을 어떻게 끝낼 것인가 | [읽기]({{ '/docs/devlog/2026-09-03-kickoff.html' | relative_url }}) |
| 2026-09-03 | 개발 문서 사이트를 왜 지킬로 만들었나 | [읽기]({{ '/docs/devlog/2026-09-03-jekyll-hub.html' | relative_url }}) |
| 2026-09-03 | 기획서 v6 를 반영했다 — 제품 정의부터 틀려 있었다 | [읽기]({{ '/docs/devlog/2026-09-03-spec-v6-reflected.html' | relative_url }}) |
| 2026-09-14 | 모델 선정 완료(Core gemma4·NPC kanana)와 실플레이 개선 3단계, 본진 승격 마무리 | [읽기]({{ '/docs/devlog/2026-09-14-dev-log.html' | relative_url }}) |
| 2026-09-15 | 첫 휴먼테스트, NPC 대화 교체(gemma4), 구글 로그인·랜딩 페이지 구축 | [읽기]({{ '/docs/devlog/2026-09-15-dev-log.html' | relative_url }}) |
| 2026-09-16 | 테스터6 휴먼테스트, 개발 로그인, Anthropic·Gemini 평가, 프로덕션 도메인 연결 | [읽기]({{ '/docs/devlog/2026-09-16-dev-log.html' | relative_url }}) |
| 2026-09-17 | 공개 운영 모델 확정(Sonnet 5·Haiku 4.5), 테스터7~11 휴먼테스트, 원숭이손 재설계 | [읽기]({{ '/docs/devlog/2026-09-17-dev-log.html' | relative_url }}) |
| 2026-09-18 | 임베딩 3모델 평가, 신의 질문 개선, 낮 화면 재구성, 최종 배포 | [읽기]({{ '/docs/devlog/2026-09-18-dev-log.html' | relative_url }}) |
| 2026-09-19 | 밤 답안 뭉침 해소, 클리어 화면 평가 수집, 그림 WebP 전환 | [읽기]({{ '/docs/devlog/2026-09-19-dev-log.html' | relative_url }}) |
| 2026-09-24 | Anthropic 키 교체 뒤 서버 복구, 새 키로 첫 판 시작 확인 | [읽기]({{ '/docs/devlog/2026-09-24-dev-log.html' | relative_url }}) |
| 2026-10-01 | ERD 문서 추가 (docs/erd.md, 코드 수정 없음) | [읽기]({{ '/docs/devlog/2026-10-01-dev-log.html' | relative_url }}) |

> **읽는 법**
> 09-03부터 09-16까지 14일은 집중 개발 기간이고, 그 끝인 2026-09-16에 `remakeday.com`에 v1을 공개했습니다. 09-17 이후 항목은 v1 공개 뒤의 작업입니다 — 공개 운영 모델 전환(09-18), 휴먼테스트 반영, 운영 점검, 문서 보강. 프로젝트는 지금도 개발 중입니다.
>
> 09-04~09-13 사이의 작업은 별도 일지 없이 [5. 마일스톤&WBS]({{ '/docs/wbs.html' | relative_url }})의 스프린트 보드와 [단계별 개발 일정]({{ '/docs/schedule/timeline.html' | relative_url }})에 카드 단위로 남아 있습니다.
