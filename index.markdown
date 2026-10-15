---
layout: default
title: 1. 홈
permalink: /
home: true
nav_order: 1
description: 같은 하루를 반복하는 루프물 대화 게임 REMAKE DAY. 구현 화면, 개발 문서와 연구 기록을 함께 읽습니다.
---

<div class="rd-home">
  <div class="rd-masthead"><span>FOODOPENLAB <span aria-hidden="true">/</span> REMAKE DAY</span><span>개발 문서와 연구 기록</span></div>
  <section class="rd-hero" aria-labelledby="home-title">
    <div class="rd-hero-copy">
      <p class="rd-kicker"><span aria-hidden="true"></span> REMAKE DAY · 루프물 대화 게임</p>
      <h1 id="home-title" class="no_anchor">같은 하루를 반복하는데,<br><em>나만 그걸 기억한다.</em></h1>
      <p class="rd-lead">다섯 번의 하루, 달라지는 대화와 선택.<br>단서를 모으고 인물에게 질문하며<br>세계가 멸망하는 이유를 찾아갑니다.</p>
      <div class="rd-actions"><a class="rd-button" href="{{ '/showcase/screens/' | relative_url }}">최종 산출물 보기 <span aria-hidden="true">↗</span></a><a class="rd-text-link" href="{{ site.project.app_url }}" rel="noopener">실제 게임 <span aria-hidden="true">↗</span></a></div>
      <p class="rd-hero-note">김충식 개인 프로젝트 · v1 공개 후 계속 개발 중</p>
    </div>
    <figure class="rd-scene"><img class="rd-game-screen" src="{{ '/assets/img/screens/08-day-scene.jpg' | relative_url }}" alt="REMAKE DAY 낮 장면의 대화와 탐문 화면" fetchpriority="high"><figcaption>실제 실행 화면 · 낮, 인물과 대화하고 단서를 찾는 시간</figcaption></figure>
  </section>

  <div class="rd-scope" aria-label="프로젝트 범위">
    <div><strong>14<span>일</span></strong><p>14일 만에 v1 공개</p></div>
    <div><strong>5<span>회차</span></strong><p>5회차 루프</p></div>
    <div><strong>14<span>판</span></strong><p>사람 판 14판 · 탐색적 관찰</p></div>
  </div>
  <p class="rd-scope-caution">탐색적 관찰은 성능 주장이 아닙니다.</p>

  <section class="rd-story" aria-labelledby="journey">
    <div class="rd-section-intro"><p class="rd-eyebrow">01 / 반복되는 하루</p><h2 id="journey">같은 하루에서<br>다른 선택을 만듭니다.</h2><p>아침의 단서에서 낮의 대화로,<br>밤의 서술에서 다음 하루의 변화로.</p></div>
    <ol class="rd-steps">
      <li><span>01</span><div><h3 id="home-morning">아침 · 단서</h3><p>눈을 뜨고 오늘의 단서와 이전 밤에 정한 규칙을 확인합니다.</p></div><span aria-hidden="true">↓</span></li>
      <li><span>02</span><div><h3 id="home-day">낮 · 대화·탐문</h3><p>장면을 옮겨 인물에게 질문하고, 서로 다른 기억과 단서를 모읍니다.</p></div><span aria-hidden="true">↓</span></li>
      <li><span>03</span><div><h3 id="home-night">밤 · 서술·채점·신의 개입</h3><p>알아낸 것을 쓰고 결과를 확인합니다. 다음 하루에 적용할 규칙을 선택합니다.</p></div><span aria-hidden="true">↗</span></li>
    </ol>
  </section>

  <section class="rd-feature" aria-labelledby="documents">
    <div class="rd-feature-copy"><p class="rd-eyebrow">02 / 실제로 만든 것</p><h2 id="documents">화면으로 만나는<br>REMAKE DAY.</h2><p>진입부터 다섯 번째 밤까지.<br>실제 한 판을 끝까지 플레이하며 찍은 화면 24장입니다.</p><a class="rd-button rd-button-light" href="{{ '/showcase/screens/' | relative_url }}">최종 산출물 살펴보기 <span aria-hidden="true">↗</span></a></div>
    <div class="rd-feature-index" aria-label="최종 산출물 구성"><p>PRODUCT WALKTHROUGH</p>
      <a href="{{ '/showcase/screens/' | relative_url }}#entry"><span>01</span>진입 <span aria-hidden="true">↗</span></a>
      <a href="{{ '/showcase/screens/' | relative_url }}#morning"><span>02</span>아침 <span aria-hidden="true">↗</span></a>
      <a href="{{ '/showcase/screens/' | relative_url }}#day"><span>03</span>낮 · 대화 <span aria-hidden="true">↗</span></a>
      <a href="{{ '/showcase/screens/' | relative_url }}#night"><span>04</span>밤 · 서술과 채점 <span aria-hidden="true">↗</span></a>
      <a href="{{ '/showcase/screens/' | relative_url }}#doom"><span>05</span>멸망 <span aria-hidden="true">↗</span></a>
      <a href="{{ '/showcase/screens/' | relative_url }}#god"><span>06</span>신의 개입 <span aria-hidden="true">↗</span></a>
      <a href="{{ '/showcase/screens/' | relative_url }}#final"><span>07</span>다섯 번째 밤 <span aria-hidden="true">↗</span></a>
    </div>
  </section>

  <section class="rd-reading" aria-labelledby="architecture">
    <div class="rd-reading-heading"><div><p class="rd-eyebrow">03 / 설계와 기록</p><h2 id="architecture">결과 뒤의 과정도<br>열어볼 수 있습니다.</h2></div><a class="rd-text-link" href="{{ '/docs/toc.html' | relative_url }}">전체 문서 목차 <span aria-hidden="true">→</span></a></div>
    <div class="rd-reading-grid">
      <a href="{{ '/docs/research.html' | relative_url }}"><span class="rd-eyebrow">EVIDENCE</span><img class="rd-research-image" src="{{ '/assets/images/research-instrument.webp' | relative_url }}" width="1600" height="1000" alt="게임·AI 제안·사람의 선택·기록으로 구성한 연구 실험환경" loading="lazy"><h3 class="no_anchor">어디까지 확인했는가</h3><p>AI 모델 선정과 사람의 선택 관찰,<br>연구 결과를 해석할 때의 한계.</p><span class="rd-reading-arrow" aria-hidden="true">↗</span></a>
      <a href="{{ '/docs/detailed-design.html' | relative_url }}"><span class="rd-eyebrow">ENGINEERING</span><h3 class="no_anchor">어떻게 만들었는가</h3><p>데이터 모델과 API 계약,<br>대화 게임을 작동시키는 설계.</p><span class="rd-reading-arrow" aria-hidden="true">↗</span></a>
      <a href="{{ '/docs/devlog.html' | relative_url }}"><span class="rd-eyebrow">JOURNAL</span><h3 class="no_anchor">무엇을 바꿔 왔는가</h3><p>기능을 만들고 검증하며<br>날짜별로 남긴 개발 기록.</p><span class="rd-reading-arrow" aria-hidden="true">↗</span></a>
    </div>
  </section>

  <section class="rd-team" aria-labelledby="developer-heading"><div class="rd-team-mark" aria-hidden="true">R.</div><div><p class="rd-eyebrow">DEVELOPER / 김충식</p><h2 id="developer-heading">한 사람이 만든 REMAKE DAY.</h2><p>기획·시나리오·프론트·백엔드·AI 에이전트·평가·운영</p></div><a class="rd-text-link" href="{{ '/docs/developer.html' | relative_url }}">개발자 소개 <span aria-hidden="true">↗</span></a></section>
  <div class="rd-endnote"><span>개발 시작 <strong>2026-09-03</strong></span><span>v1 공개 <strong>2026-09-16</strong></span><span>연구 재집계 <strong>2026-09-18</strong></span><a href="{{ '/docs/schedule/timeline.html' | relative_url }}">현재 개발 중 · 개발 일정 <span aria-hidden="true">↗</span></a></div>
</div>
