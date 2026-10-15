---
layout: default
title: "7. 상위 설계서"
permalink: /docs/high-level-design.html
nav_order: 7
has_children: true
description: "헥사고날 + DDD 엔진, Planner·Agent·Advisor·Re-plan·Evaluator 에이전트 구성, 확정 LLM 구성, 인프라와 배포."
---

# 7. 상위 설계서

이 장은 REMAKE DAY가 **어떤 구조로 돌아가는지**를 계층 단위로 설명합니다.
어댑터 위 계층 전체가 BeyondBob Engine이고, 포트는 LLM·도구·도메인 세 곳뿐입니다.
판정은 "계산은 코드, 판단은 LLM"으로 나뉘어 도메인 계층을 LLM 없이 유닛테스트할 수 있습니다.
에이전트는 Planner → Agent → Re-plan → Evaluator의 대칭 구조에 침묵 권고(Advisor) 층이 붙고,
모델은 Core `claude-sonnet-5` + NPC `claude-haiku-4-5`로 확정돼 있습니다.
인프라는 웹 Vercel + API 컨테이너 1대이며, LLM 비용 상한이 곧 가용성 한계입니다.

| 절 | 내용 |
|---|---|
| [시스템 아키텍처]({{ '/docs/high-level-design/architecture.html' | relative_url }}) | 계층 구조, 포트 3개, 판정 구조, 하네스, 아키텍처 테스트 |
| [AI 에이전트 설계]({{ '/docs/high-level-design/agent.html' | relative_url }}) | 역할별 모델 배치, Re-plan, Memory, 도구 2개, 침묵 권고, 실패 처리 |
| [LLM 구성]({{ '/docs/high-level-design/llm-config.html' | relative_url }}) | 로컬 평가에서 외부 API 전환까지, 선정 근거와 롤백 |
| [인프라 및 배포]({{ '/docs/high-level-design/infra.html' | relative_url }}) | 구성, 환경, LLM 비용, 시크릿, 파이프라인, 관측, 롤백 |
