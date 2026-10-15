---
layout: default
title: "6. 요구사항정의서"
permalink: /docs/requirements.html
nav_order: 6
has_children: true
description: "무엇을 만들고 무엇을 만들지 않는가 — 절대 방어선 5개, 컷 순서, 화면 5장, 보안·운영 한도."
---

# 6. 요구사항정의서

이 장은 REMAKE DAY v1이 **무엇을 반드시 갖추고, 무엇을 만들지 않는지**를 정합니다.
우선순위는 따로 발명하지 않았습니다. 기획서 v6의 12.3이 정한 절대 방어선 ①~⑤가 그대로 MUST이고,
⑥~⑨는 아래에서부터 자르는 압축 대상입니다. 화면은 다섯 장뿐이며, 로그인·설치·긴 튜토리얼 없이
30초 안에 판단되는 진입이 비기능 요구사항입니다. v1 공개 직전에 붙은 구글 로그인과 사용 한도는
설계 변경이 아니라 비용 방어선이므로 별도 절로 둡니다.

| 절 | 내용 |
|---|---|
| [목적]({{ '/docs/requirements/purpose.html' | relative_url }}) | 우선순위 9단계와 절대 방어선 ①~⑤, 1회차 목표 |
| [개발 범위]({{ '/docs/requirements/dev-scope.html' | relative_url }}) | 자르는 순서, 3주 → 14일 압축, 범위 밖, 결정 기록 |
| [화면·기능 요구]({{ '/docs/requirements/screens.html' | relative_url }}) | 화면 5장, 첫 방문 30초 대응, 화면별 기능 규칙 |
| [보안 및 운영 한도]({{ '/docs/requirements/security.html' | relative_url }}) | 로그인, 판 수 제한, 지출 한도, 시크릿, 릴리스 보안 항목 |
