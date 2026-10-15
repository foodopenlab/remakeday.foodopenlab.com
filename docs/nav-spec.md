# 메뉴·파일·permalink 명세 (프론트 ↔ 콘텐츠 계약)

> 이 문서는 Codex(프론트)와 콘텐츠 이전 작업이 공유하는 유일한 계약입니다. 여기 없는 permalink·title은 만들지 않습니다.
> just-the-docs의 `parent:`는 **부모 페이지의 `title` 문자열과 정확히 일치**해야 합니다. 아래 제목을 글자 그대로 씁니다.

## 0. 파일 소유권

| 경로 | 소유 | 비고 |
|---|---|---|
| `_config.yml`, `Gemfile`, `Gemfile.lock`, `.github/workflows/`, `CNAME`, `404.html` | Codex | |
| `_sass/`, `_includes/` (아래 예외 제외), `assets/js/`, `assets/css/` | Codex | metabole에서 이식 |
| `index.markdown` | Codex | §5 홈 블록. 문구는 콘텐츠 측이 나중에 채움 |
| `_layouts/` | Codex | just-the-docs 기본 사용. 커스텀 레이아웃은 만들지 않음 |
| `_includes/research/` | 콘텐츠 | research 사이트 이식. Codex는 스타일만 맞춤 |
| `jekyll/**` | 콘텐츠 | 모든 문서 페이지 |
| `_data/*.yml`, `_data/research_figures.json` | 콘텐츠 | 스키마는 §3 |
| `assets/img/`, `assets/images/` | 콘텐츠 | 스크린샷·그림 |
| `scripts/`, `tests/`, `docs/` | 콘텐츠 | 빌드 제외 |

## 1. 공통 front matter

```yaml
---
layout: default
title: 시스템 아키텍처          # parent 참조용. 장(章) 페이지는 "7. 상위 설계서"처럼 번호 포함
permalink: /docs/high-level-design/architecture.html
parent: 7. 상위 설계서
nav_order: 1
description: 한 문장 요약(검색·SEO)
---
```

- 장 페이지: `has_children: true`, `nav_order: <장 번호>`.
- 3단계 페이지: `parent` + `grand_parent`.
- 제목 h1은 본문에 `# 제목`으로 한 번만. just-the-docs가 `title`을 자동으로 h1로 넣지 않음.

## 2. 메뉴 트리

| nav | 파일 | title | permalink | parent | 원천 |
|---|---|---|---|---|---|
| 1 | `index.markdown` | 1. 홈 | `/` | | Codex |
| 2 | `jekyll/toc.md` | 2. 목차 | `/docs/toc.html` | | 새로 작성(마지막) |
| 3 | `jekyll/intro/overview.md` | 3. 프로젝트 개요 | `/docs/overview.html` | | `_plan/overview.md` 요약 |
| 3.1 | `jekyll/intro/purpose.md` | 프로젝트 목적 | `/docs/overview/purpose.html` | 3. 프로젝트 개요 | `_plan/overview.md` 한 줄 정의·맥락 |
| 3.2 | `jekyll/intro/scope.md` | 주요 내용 | `/docs/overview/scope.html` | 3. 프로젝트 개요 | `_plan/overview.md` 이름 두 개·엔진 경계, `_plan/scope.md` 절대 방어선 요약 |
| 3.3 | `jekyll/intro/effects.md` | 기대 효과 | `/docs/overview/effects.html` | 3. 프로젝트 개요 | overview 전이 시연·연구 활용 |
| 4 | `jekyll/intro/developer.md` | 4. 개발자 소개 | `/docs/developer.html` | | `_data/team.yml` 김충식 항목 + 1인 전 영역 |
| 5 | `jekyll/schedule/wbs.md` | 5. 마일스톤&WBS | `/docs/wbs.html` | | `{% include sprint-roadmap.html %}` + `{% include sprint-boards.html %}` |
| 5.1 | `jekyll/schedule/timeline.md` | 단계별 개발 일정 | `/docs/schedule/timeline.html` | 5. 마일스톤&WBS (`has_children: true`) | `_data/schedule.yml` 14일 표 |
| 5.1.1~4 | `jekyll/schedule/sprint1.md` … `sprint4.md` | Sprint 1 일자별 진행 사항 … Sprint 4 v1 이후 진행 사항 | `/docs/schedule/sprintN.html` | 단계별 개발 일정 / grand_parent 5. 마일스톤&WBS | kanban 카드 일자별 |
| 5.2 | `jekyll/schedule/risk.md` | 위험 관리 방안 | `/docs/schedule/risk.html` | 5. 마일스톤&WBS | `_plan/risk.md` |
| 6 | `jekyll/requirements/index.md` | 6. 요구사항정의서 | `/docs/requirements.html` | | 안내 |
| 6.1 | `jekyll/requirements/purpose.md` | 목적 | `/docs/requirements/purpose.html` | 6. 요구사항정의서 | `_plan/scope.md` 상단 |
| 6.2 | `jekyll/requirements/dev-scope.md` | 개발 범위 | `/docs/requirements/dev-scope.html` | 6. 요구사항정의서 | `_plan/scope.md` 방어선·범위 밖·결정 기록 |
| 6.3 | `jekyll/requirements/screens.md` | 화면·기능 요구 | `/docs/requirements/screens.html` | 6. 요구사항정의서 | `_plan/scope.md` 화면 5장, `_plan/design.md` 화면 원칙 |
| 6.4 | `jekyll/requirements/security.md` | 보안 및 운영 한도 | `/docs/requirements/security.html` | 6. 요구사항정의서 | `_plan/infra.md` 방어선(로그인·판 수·지출 한도), `_plan/release.md` 보안 항목 |
| 7 | `jekyll/design/index.md` | 7. 상위 설계서 | `/docs/high-level-design.html` | | 안내 |
| 7.1 | `jekyll/design/architecture.md` | 시스템 아키텍처 | `/docs/high-level-design/architecture.html` | 7. 상위 설계서 | `_plan/architecture.md` |
| 7.2 | `jekyll/design/agent.md` | AI 에이전트 설계 | `/docs/high-level-design/agent.html` | 7. 상위 설계서 | `_plan/ai.md` |
| 7.3 | `jekyll/design/llm-config.md` | LLM 구성 | `/docs/high-level-design/llm-config.html` | 7. 상위 설계서 | `misc/llm-orchestration.md` |
| 7.4 | `jekyll/design/infra.md` | 인프라 및 배포 | `/docs/high-level-design/infra.html` | 7. 상위 설계서 | `_plan/infra.md` |
| 8 | `jekyll/detailed-design/index.md` | 8. 상세 설계서 | `/docs/detailed-design.html` | | 안내 |
| 8.1 | `jekyll/detailed-design/erd.md` | ERD — 데이터 모델 | `/docs/detailed-design/erd.html` | 8. 상세 설계서 | `_plan/data.md` (mermaid erDiagram으로) |
| 8.2 | `jekyll/detailed-design/api.md` | API 계약 | `/docs/detailed-design/api.html` | 8. 상세 설계서 | `_plan/api.md` |
| 8.3 | `jekyll/detailed-design/design-system.md` | 디자인 시스템 | `/docs/detailed-design/design-system.html` | 8. 상세 설계서 | `_plan/design.md`, `misc/ui.html` |
| 9 | `jekyll/test/index.md` | 9. 시나리오 테스트 | `/docs/test.html` | | 안내 |
| 9.1 | `jekyll/test/release.md` | QA 및 릴리스 | `/docs/test/release.html` | 9. 시나리오 테스트 | `_plan/release.md` |
| 9.2 | `jekyll/test/model-evaluation.md` | 모델 평가 | `/docs/test/model-evaluation.html` | 9. 시나리오 테스트 | 13장 Exp 1 요약 + 링크(새로 작성) |
| 10 | `jekyll/inspection/index.md` | 10. 최종 검수 | `/docs/inspection.html` | | 안내 |
| 10.1 | `jekyll/inspection/checklist.md` | 검수 체크리스트 | `/docs/inspection/checklist.html` | 10. 최종 검수 | `pm/checklist.md` |
| 10.2 | `jekyll/inspection/runbook.md` | 운영 런북 | `/docs/inspection/runbook.html` | 10. 최종 검수 | `pm/infra.md` |
| 11 | `jekyll/deliverables/demo-scenario.md` | 11. 시연 시나리오 | `/docs/demo-scenario.html` | | `deliverables/screens.md` 흐름을 글로 |
| 12 | `jekyll/devlog/index.md` | 12. 개발일지 | `/docs/devlog.html` | | 안내 + 날짜 목록 |
| 12.x | `jekyll/devlog/YYYY-MM-DD-slug.md` | `YYYY-MM-DD 제목` | `/docs/devlog/YYYY-MM-DD-slug.html` | 12. 개발일지 | `_posts/*` 11편. `nav_order`는 날짜 오름차순 1~11 |
| 13 | `jekyll/research/index.md` | 13. 연구 보고서 | `/docs/research.html` | | research `index.md` |
| 13.1 | `jekyll/research/statement.md` | 왜 게임인가 | `/docs/research/statement.html` | 13. 연구 보고서 | `statement.md` |
| 13.2 | `jekyll/research/testbed.md` | 실험환경 설계 | `/docs/research/testbed.html` | 13. 연구 보고서 | `testbed.md` |
| 13.3 | `jekyll/research/model-selection.md` | Exp 1 — AI 모델 선정 | `/docs/research/model-selection.html` | 13. 연구 보고서 | `experiments/model-selection.md` 전문 |
| 13.4 | `jekyll/research/human-observations.md` | Exp 2 — 사람의 선택 관찰 | `/docs/research/human-observations.html` | 13. 연구 보고서 | `experiments/human-observations.md` |
| 13.5 | `jekyll/research/prereg.md` | 다음 실험의 사전등록 | `/docs/research/prereg.html` | 13. 연구 보고서 | `prereg.md` (본문 수정 최소) |
| 13.6 | `jekyll/research/plain-summary.md` | 비유로 읽는 연구 | `/docs/research/plain-summary.html` | 13. 연구 보고서 | `plain-summary.md` |
| 13.7 | `jekyll/research/limitations.md` | 한계와 재현 방법 | `/docs/research/limitations.html` | 13. 연구 보고서 | `limitations.md` |
| 13.8 | `jekyll/research/lab-notes.md` | 날짜별 연구 기록 | `/docs/research/lab-notes.html` | 13. 연구 보고서 | `lab-notes.md` |
| 14 | `jekyll/appendix/index.md` | 14. 부록 | `/docs/appendix.html` | | 안내 |
| 14.1 | `jekyll/appendix/glossary.md` | 용어 정의 | `/docs/appendix/glossary.html` | 14. 부록 | research `_includes/research/glossary.html` + 기획 용어 |
| 14.2 | `jekyll/appendix/spec-projection.md` | 기획서 반영표 | `/docs/appendix/spec-projection.html` | 14. 부록 | `misc/projection.html` |
| 14.3 | `jekyll/appendix/site-guide.md` | 이 사이트 사용법 | `/docs/appendix/site-guide.html` | 14. 부록 | `pm/jekyll-guide.md` 1인용 재작성 |
| 15 | `jekyll/showcase/screens.html` | 15. 최종산출물 | `/showcase/screens/` | | `deliverables/screens.md` + `assets/img/screens/*.jpg` 24장 |

## 3. `_data` 스키마

### `_data/project_sprints.yml` (5장 보드·로드맵, Codex include가 읽음)

```yaml
as_of: '2026-10-01'
status_note: 'v1은 2026-09-16 공개. 이후 작업은 Sprint 4에 누적.'
states:
  - {id: todo,   label: 예정,   hint: 아직 착수 기록이 없는 작업}
  - {id: doing,  label: 진행 중, hint: 작업 중이며 종료 조건 미충족}
  - {id: review, label: 검토,   hint: 결과는 있으나 추가 확인 필요}
  - {id: done,   label: 완료,   hint: 구현·기록 확인}
areas:                      # 실제 생성값. include는 여기서 라벨을 읽는다(하드코딩 금지)
  - {id: fe,      label: 프론트}
  - {id: be,      label: 백엔드}
  - {id: ai,      label: AI 에이전트}
  - {id: eval,    label: 평가}
  - {id: qa,      label: QA·릴리스}
  - {id: content, label: 시나리오·콘텐츠}
sprints:
  - id: sprint-1
    name: Sprint 1
    period: '09.03 ~ 09.04'
    phase: 설계
    goal: ...
    exit: ...
    status: done
    record_url: /docs/schedule/sprint1.html
    tasks:
      - {id: FE-01, date: '2026-09-03', status: done, priority: P0, area: fe, title: ..., dod: ..., output: ...}
```

스프린트 경계: Sprint 1 = 09-03~04(설계) · Sprint 2 = 09-05~09-12(구현) · Sprint 3 = 09-13~09-16(검증·v1 공개) · Sprint 4 = 09-17~(v1 이후). 담당자 필드 없음. `area`는 카드 id 접두어(FE·APP→fe, BE→be, AI→ai, PM→qa)와 태그(평가·모델→eval, 서사·기획→content)로 결정. 총 210건. 생성기는 `scripts/convert-kanban.py`, 손으로 고치지 않는다. 기간이 끝난 Sprint 1~3은 `status: done`, Sprint 4는 `doing`이며 카드 0건으로 시작한다.

### `_data/schedule.yml` (5.1 일정표)

기존 구조 유지하되 `dday` 제거, `day: 1~14`, `date`, `dow`, `phase`, `theme`, `gate`, `note`. `note`의 팀원 언급 제거.

### `_data/reading.yml`, `_data/research_figures.json`

research 사이트 것을 그대로 가져오되 `reading.yml`의 키를 새 permalink(`/docs/research.html`, `/docs/research/statement.html` …)로 바꾼다. `research_figures.json`의 `sources[].path`는 `jekyll/research/...`로 바꾸고 `scripts/refresh_research_data.py`로 재생성한다.

## 4. 연구 페이지의 읽기 층 호출

각 `jekyll/research/*.md` 본문 맨 위(h1 아래)에 다음을 둔다. Codex는 이 include들이 just-the-docs 본문 폭 안에서 깨지지 않게만 스타일을 맞춘다.

```liquid
{% assign reading = site.data.reading[page.url] %}
{% if reading %}{% include research/overview.html reading=reading %}{% endif %}
```

`model-selection.md`는 추가로 `{% include research/model-decisions.html %}`, `prereg.md`는 `{% include research/prereg-notes.html %}`, `index.md`는 `{% include research/home.html %}`.

## 5. 홈(`index.markdown`) 블록 — Codex

metabole `index.markdown`의 클래스 구조(`mb-*`)를 `rd-*`로 바꿔 그대로 쓴다. 블록 순서와 링크 대상:

1. masthead: `FOODOPENLAB / REMAKE DAY`
2. hero: 제목 "같은 하루를 반복하는데, 나만 그걸 기억한다." / 버튼 ① `/showcase/screens/` ② 실제 게임(URL은 `_config.yml` `project.app_url`)
3. 범위 숫자 3칸: 14일 만에 v1 공개 · 5회차 루프 · 사람 판 14판 + 주의 문구 "탐색적 관찰은 성능 주장이 아닙니다"
4. 3단계 흐름: 아침(단서) → 낮(대화·탐문) → 밤(서술·채점·신의 개입)
5. 최종 산출물 인덱스: `/showcase/screens/#entry #morning #day #night #doom #god #final`
6. 설계와 기록 3카드: EVIDENCE → `/docs/research.html` · ENGINEERING → `/docs/detailed-design.html` · JOURNAL → `/docs/devlog.html`
7. 개발자: "한 사람이 만든 REMAKE DAY." → `/docs/developer.html`
8. endnote: 개발 시작 2026-09-03 · v1 공개 2026-09-16 · 연구 재집계 2026-09-18 · 현재 개발 중 → `/docs/schedule/timeline.html`
