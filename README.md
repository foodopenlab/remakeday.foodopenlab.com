# REMAKE DAY 개발 문서

같은 하루를 반복하는 루프물 대화 게임 REMAKE DAY와 그 엔진 BeyondBob의 개발 문서·연구 기록입니다. 김충식 개인 프로젝트입니다.

- 문서 사이트: <https://remakeday.foodopenlab.com>
- 실제 게임: `_config.yml`의 `project.app_url`
- 앱 저장소: <https://github.com/remakeday/com.remakeday>

## 구성

| 장 | 내용 | 위치 |
|---|---|---|
| 1 | 홈 | `index.markdown` |
| 2 | 목차 | `jekyll/toc.md` |
| 3~4 | 프로젝트 개요 · 개발자 소개 | `jekyll/intro/` |
| 5 | 마일스톤&WBS(일정·스프린트·위험) | `jekyll/schedule/`, `_data/schedule.yml`, `_data/project_sprints.yml` |
| 6~8 | 요구사항 · 상위 설계 · 상세 설계 | `jekyll/requirements/`, `jekyll/design/`, `jekyll/detailed-design/` |
| 9~11 | 시나리오 테스트 · 최종 검수 · 시연 시나리오 | `jekyll/test/`, `jekyll/inspection/`, `jekyll/deliverables/` |
| 12 | 개발일지 | `jekyll/devlog/` |
| 13 | 연구 보고서 | `jekyll/research/`, `_data/reading.yml`, `_includes/research/` |
| 14 | 부록 | `jekyll/appendix/` |
| 15 | 최종산출물(실플레이 화면) | `jekyll/showcase/screens.html`, `assets/img/screens/` |

메뉴·permalink·데이터 스키마 계약은 `docs/nav-spec.md`, 통합 배경은 `brainstorming.md`, 프론트 작업 지침은 `AGENTS.md`에 있습니다.

## 로컬 실행·검증

```bash
bundle install
bundle exec jekyll serve
```

```bash
bundle exec jekyll build
python3 scripts/check-site.py
node scripts/check-search.cjs
python3 scripts/refresh_research_data.py --check
python3 scripts/check_public.py
```

`scripts/check_public.py`는 `_private/public-rules.json`(git 제외)이 있어야 동작합니다. 연구 그림 데이터 `_data/research_figures.json`은 손으로 고치지 않고 `scripts/refresh_research_data.py`로 다시 만듭니다.

## 배포

`main` push → GitHub Actions(`.github/workflows/jekyll.yml`) → GitHub Pages. 저장소 Settings → Pages → Source를 "GitHub Actions"로 두고, DNS에 `remakeday.foodopenlab.com` CNAME을 등록합니다.
