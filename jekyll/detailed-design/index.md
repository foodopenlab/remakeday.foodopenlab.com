---
layout: default
title: "8. 상세 설계서"
permalink: /docs/detailed-design.html
nav_order: 8
has_children: true
description: "판정 로그가 산출물인 데이터 모델, 화면 5장을 만드는 최소 API 계약, 전면 텍스트 디자인 시스템."
---

# 8. 상세 설계서

이 장은 상위 설계를 **테이블·엔드포인트·화면 규칙** 수준으로 내립니다.
데이터 모델은 게임 상태보다 판정 로그를 먼저 설계했습니다 — 11.1 시스템 검증 12종과 11.2 침묵 권고 채택률이 전부 이 테이블들에서 나옵니다.
API는 프론트가 화면 5장을 만들 수 있는 최소 계약이며, 09-16부터 구글 로그인과 과잉 사용 방지 허들이 붙었습니다.
디자인 시스템은 전면 텍스트라는 연출 원칙을 색·서체·레이아웃 결정으로 옮긴 것입니다.

| 절 | 내용 |
|---|---|
| [ERD — 데이터 모델]({{ '/docs/detailed-design/erd.html' | relative_url }}) | 테이블, 관계도, 인덱스, 마이그레이션 |
| [API 계약]({{ '/docs/detailed-design/api.html' | relative_url }}) | 인증·허들, 응답 형태, 엔드포인트, SSE 이벤트 |
| [디자인 시스템]({{ '/docs/detailed-design/design-system.html' | relative_url }}) | 레이아웃 선택, 토큰, 서체 3층, 기획서 조항 → UI 결정, 접근성 |
