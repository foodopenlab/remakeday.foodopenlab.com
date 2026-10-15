---
layout: default
title: 10. 최종 검수
permalink: /docs/inspection.html
has_children: true
nav_order: 10
description: v1 공개 전후에 실제로 따라 읽은 검수 체크리스트와 운영 런북. 무엇을 확인했고 장애 때 어떤 순서로 움직이는지.
---

# 10. 최종 검수

이 장은 집중 개발 14일(2026-09-03 ~ 09-16)과 v1 공개 당일에 **실제로 따라 읽은 절차**를 그대로 둔 것입니다. 설계 판단은 다른 장에 있고, 여기에는 손이 움직이는 순서만 있습니다.

| 문서 | 무엇이 있나 |
|---|---|
| [검수 체크리스트]({{ '/docs/inspection/checklist.html' | relative_url }}) | 매일 아침·저녁에 반복한 점검 항목, 매일 보는 위험 신호 표, 단계별(ERD 동결 → 알파 시연 → 기능 동결 → 공개 대비 → 리허설 → v1 공개) 추가 항목 |
| [운영 런북]({{ '/docs/inspection/runbook.html' | relative_url }}) | 환경·시크릿·DNS 표, 스테이징·프로덕션 배포 명령, 롤백 순서와 목표 시간, 백업·복구, 장애 증상별 대응 순서, 공개 직후 2시간 모니터링 |

> **읽을 때 기준 시점**
> 체크리스트와 런북은 v1 공개 전에 쓴 문서라 일부 절차(스테이징 서버 ssh 등)는 계획 시점의 구성입니다. 실제 v1 구성은 프론트 Vercel · 백엔드 홈서버 + Cloudflare 터널 · DB docker compose이며, 그 경위는 [2026-09-16 개발일지]({{ '/docs/devlog/2026-09-16-dev-log.html' | relative_url }})와 [인프라 및 배포]({{ '/docs/high-level-design/infra.html' | relative_url }})에 있습니다.
