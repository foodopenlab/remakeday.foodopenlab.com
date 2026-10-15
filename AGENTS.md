# remakeday.foodopenlab.com — 에이전트 작업 지침

REMAKE DAY 개인 프로젝트의 개발 문서·연구 보고서 사이트(Jekyll, just-the-docs). 김충식 1인 개발.

## 먼저 읽을 것

0. `HANDOFF.md` — 현재 상태와 할 일 순서
1. `CLAUDE.md` — 구현 원칙(과도한 테스트·선제적 추상화 금지)
2. `docs/nav-spec.md` — 메뉴·파일·permalink·`_data` 스키마 계약. **여기 없는 경로·제목은 만들지 않는다.**
3. `brainstorming.md` — 왜 이렇게 합치는지(§2·§6), 팀→개인·해커톤→개인 프로젝트 치환 규칙(§4)

## 절대 규칙

- 사이트 어디에도 다음 표현이 나오면 안 된다: 류준·장민석·신채연·이은상·팀장·팀원·우리 팀·원티드·Championship·해커톤·공개 투표·심사·출품·탈락·D-day 카운트다운. 검증: `grep -rE '류준|장민석|신채연|이은상|팀장|팀원|우리 팀|원티드|Championship|해커톤|공개 투표|심사|출품|탈락' --exclude-dir=_site --exclude-dir=.git --exclude-dir=docs --exclude-dir=.jekyll-cache .` → 0건.
- `REMAKE_DAY_*`, `TalkFile_*`, `_private/`는 커밋·빌드 금지.
- 새 프레임워크·새 의존성 금지. just-the-docs + SCSS + 바닐라 JS.
- 파일 소유권(`docs/nav-spec.md` §0)을 넘지 않는다.

## 프론트(Codex) 작업 범위

원본 골격: `/home/kimchungsik/projects/metabole.beyondfacade.cloud` (just-the-docs 0.10, Jekyll 4.4). 거기서 복사·수정한다.

1. `Gemfile`(metabole 그대로), `_config.yml`(아래 §설정), `.github/workflows/jekyll.yml`(`/home/kimchungsik/projects/beyondbob.remakeday.com/.github/workflows/jekyll.yml` 복사), `CNAME`=`remakeday.foodopenlab.com`, `404.html`.
2. `_sass/custom/_docs.scss`·`_presentation.scss`·`_erd.scss` 이식. `_sass/color_schemes/metabole.scss` → `remakeday.scss`로 복사해 팔레트만 교체(기존 beyondbob `assets/css/style.scss`의 상태색·강조색 참고). `_config.yml`의 `color_scheme: remakeday`.
3. `_includes/head_custom.html`·`nav_footer_custom.html`·`title.html`·`lunr/custom-index.js`·`components/nav` 이식. `assets/js/docs.js`·`erd.js` 이식.
4. `_includes/sprint-boards.html`·`sprint-roadmap.html` 이식 후 `docs/nav-spec.md` §3 스키마에 맞게 수정: 담당자 없음, `area` 라벨 배지 표시, Sprint 4 "v1 이후"는 종료일 없음.
5. `index.markdown`: `docs/nav-spec.md` §5 블록 구조. 클래스 접두어 `mb-` → `rd-`. 문구는 placeholder여도 되지만 링크·앵커는 명세대로.
6. `jekyll/showcase/screens.html`의 레이아웃·갤러리 스타일(metabole `jekyll/showcase/screens.html` 참고). 본문 내용은 콘텐츠 측이 넣는다. 이미지는 `assets/img/screens/NN-*.jpg` 24장.
7. `_includes/research/*.html`(콘텐츠 측이 이식)이 just-the-docs 본문 폭에서 깨지지 않게 `_sass/custom/_research.scss` 추가. 기존 research 스타일은 `/home/kimchungsik/projects/research.remakeday.com/assets/css/style.scss` 참고. 레이아웃 교체는 하지 않는다.
8. `scripts/check-site.py`·`scripts/check-search.cjs`(metabole) 이식 후 통과. 375/768/1152/1440 폭에서 홈·일반 문서·ERD·연구 페이지 확인.

### `_config.yml` 설정

```yaml
title: REMAKE DAY
description: 같은 하루를 반복하는 루프물 대화 게임 REMAKE DAY의 개발 문서와 연구 기록. 김충식 개인 프로젝트.
url: "https://remakeday.foodopenlab.com"
baseurl: ""
lang: ko
timezone: Asia/Seoul
theme: just-the-docs
plugins: [jekyll-feed]
search_enabled: true
search: {heading_level: 3, preview_words: 30}
enable_copy_code_button: true
heading_anchors: true
color_scheme: remakeday
mermaid: {version: "10.9.3"}
project:
  app_url: "https://remakeday.com"        # 실제 게임. 확인 후 수정
  repo_app: "https://github.com/remakeday/com.remakeday"
  repo_site: "https://github.com/foodopenlab/remakeday.foodopenlab.com"
  started: "2026-09-03"
  v1_released: "2026-09-16"
footer_content: "REMAKE DAY — 김충식 개인 프로젝트 개발 문서. 탐색적 관찰은 성능 주장이 아닙니다."
exclude: [README.md, HANDOFF.md, brainstorming.md, AGENTS.md, CLAUDE.md, docs/, scripts/, tests/, _private/, Gemfile, Gemfile.lock, "REMAKE_DAY_*", "TalkFile_*"]
```

## 로컬 실행·검증

```bash
bundle install
bundle exec jekyll serve          # 기존 서버가 떠 있으면 다른 포트
bundle exec jekyll build
python3 scripts/check-site.py
node scripts/check-search.cjs
python3 scripts/check_public.py   # 연구 금지어(콘텐츠 측 이식 후)
```
