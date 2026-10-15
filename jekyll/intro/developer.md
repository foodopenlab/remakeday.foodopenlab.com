---
layout: default
title: 4. 개발자 소개
permalink: /docs/developer.html
nav_order: 4
description: REMAKE DAY를 혼자 기획·구현·평가·운영한 개발자 김충식 소개.
---

# 4. 개발자 소개

**김충식** — REMAKE DAY의 기획·시나리오부터 프론트·백엔드·AI 에이전트·모델 평가·QA·릴리스·운영까지 전 영역을 혼자 맡은 1인 개발자입니다. 2026-09-03부터 14일 동안 집중 개발해 09-16에 v1을 공개했고, 지금도 개발을 이어 가고 있습니다.

## 영역별로 한 일

{% assign all = "" | split: "" %}{% for s in site.data.project_sprints.sprints %}{% assign all = all | concat: s.tasks %}{% endfor -%}
{% assign n_fe = all | where: "area", "fe" | size -%}
{% assign n_be = all | where: "area", "be" | size -%}
{% assign n_ai = all | where: "area", "ai" | size -%}
{% assign n_eval = all | where: "area", "eval" | size -%}
{% assign n_qa = all | where: "area", "qa" | size -%}
{% assign n_content = all | where: "area", "content" | size -%}

과제 건수는 [마일스톤&WBS]({{ '/docs/wbs.html' | relative_url }})의 스프린트 보드(총 {{ all.size }}건)에서 집계한 값입니다.

| 영역 | 한 일 | 과제 |
|---|---|:--:|
| 기획·시나리오·콘텐츠 | 기획서 v6를 기획 문서 10편에 반영 · 스코프와 절대 방어선 확정 · 시나리오 A(구역) 인물·비트·공개 관찰·진실 명제·쿠키 12종 · NPC 3인 말투 가이드 · 아침 문장과 손상 1~3층 문안 · 엔딩 4종 텍스트 · 장면·인물·쿠키 그림과 스타일 가이드 · 배경 BGM과 음성 대사 | 콘텐츠 과제 {{ n_content }}건 |
| 프론트 | Next.js 웹 화면 5장(아침·대화·노트·인스펙터·권고 오버레이) · 디자인 토큰과 읽기 우선 타이포 · SSE 수신과 API 클라이언트 · 손상 1~3층 렌더 · 모바일 웹 대응과 접근성 · Vercel 배포와 PR 프리뷰 · 프로덕션 빌드·기동 | 프론트 과제 {{ n_fe }}건 |
| 백엔드·API | 모듈러 모놀리스·헥사고날 구조와 Port/Adapter 경계 · 게임 엔진(낮 루프·밤 채점·신의 개입·세계 손상·쿠키) 결정론 코드 · 의심도·신뢰도·발화 예산 도메인 규칙 · Game API(OpenAPI 계약)와 PostgreSQL·alembic · 판정 로그·노트·손상 이벤트 저장 · 시나리오 교체 가능성(BaseScenario 계약) | 백엔드 과제 {{ n_be }}건 |
| AI 에이전트·하네스 | 에이전트 6층(Planner·Agent·Advisor·Re-plan·Evaluator·Memory) 설계와 구현 · 역할별 프롬프트와 구조화 출력 스키마 · JSON 스키마 하네스(재생성·폴백·사실 층 검사) · ask_npc 탐문 도구와 부작용 · 침묵 권고 Advisor · 메모리 정책(민석 예외) · 전이 어댑터(감사·커리어) · 비용 상한과 프롬프트 인젝션 방어 | AI 과제 {{ n_ai }}건 |
| 모델 평가 | LLM 프로바이더 선정과 역할별 후보·비용 추정 · 평가 설계(E7 Core 슬롯 선정 · E6 NPC 슬롯 descent · Funnel · 게이트) · 평가 러너와 metrics.yml(append-only) · 하네스 계측(HarnessReport) 집계 · 판정 일관성·탐문 ON/OFF 대조 실험 · provider 어댑터와 배포 지표(지연·VRAM) · Inspector/Harness 뷰 | 평가 과제 {{ n_eval }}건 |
| QA·릴리스·인프라 | 도메인 회귀 스위트와 채점 재현성 · 뷰포트 자동 검사(390px·1440px) · 플레이 검증과 결함 로그 · 회귀 시나리오 R1~R10 · 스테이징·프로덕션 프로비저닝과 시크릿 체계 · CI(import-linter 게이트) · 세션/IP 제한과 비용 상한 · 릴리스 체크리스트·RC 태깅·배포/롤백 리허설 · 기동 스크립트와 외부망 검증 · 오픈 온콜 | QA·릴리스 과제 {{ n_qa }}건 |
| 연구 기록·문서 | 개발 허브(Jekyll) 구축과 데브로그 11편 · 연구 보고서 9편(모델 선정 Exp 1 · 사람의 선택 관찰 Exp 2 · 사전등록 · 한계와 재현 방법) · 이미지 제작서와 플레이 가이드 · 기획서 반영표 | 문서·일지 |

## 개발 방식

계산은 코드, 판단은 LLM. 의심도·신뢰도·발화 예산·세계 손상 같은 수치는 전부 결정론 코드가 계산하고, LLM은 그 위에서 말하고 판정 근거를 서술하는 자리만 맡습니다. 그래서 모델이 실패해도 규칙은 걸리고, 게임은 무너지지 않습니다. 평가도 같은 원칙으로 합니다. 측정하지 않은 것은 주장하지 않는다 — 모델 선정과 사람 판 관찰은 전부 저장된 수치와 재현 절차로 남기고, 탐색적 관찰을 성능 주장으로 바꾸지 않습니다.

- [마일스톤&WBS]({{ '/docs/wbs.html' | relative_url }}) · [단계별 개발 일정]({{ '/docs/schedule/timeline.html' | relative_url }}) · [연구 보고서]({{ '/docs/research.html' | relative_url }}) · [개발일지]({{ '/docs/devlog.html' | relative_url }})
