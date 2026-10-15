---
layout: default
title: 이 사이트 사용법
permalink: /docs/appendix/site-guide.html
parent: 14. 부록
nav_order: 3
description: just-the-docs 기반 이 문서 사이트를 혼자 유지보수하는 방법. 페이지·front matter·메뉴 순서, _data 파일 위치, 개발일지 추가, 로컬 빌드와 검증 명령.
---

# 이 사이트 사용법

이 사이트는 Jekyll + [just-the-docs](https://just-the-docs.com) 테마로 만든 정적 사이트입니다. 문서 페이지는 전부 `jekyll/` 아래 Markdown 파일이고, 메뉴는 각 파일의 front matter에서 자동으로 만들어집니다. 알아야 할 것은 세 가지입니다 — 페이지 추가하기, 개발일지 쓰기, 로컬에서 확인하기.

## 페이지와 front matter

모든 문서 페이지는 아래 형식으로 시작합니다.

```yaml
---
layout: default
title: 시스템 아키텍처          # 메뉴에 표시되는 이름. 장(章) 페이지는 "7. 상위 설계서"처럼 번호 포함
permalink: /docs/high-level-design/architecture.html
parent: 7. 상위 설계서           # 부모 페이지의 title과 글자 그대로 일치해야 한다
nav_order: 1                      # 같은 부모 아래에서의 순서
description: 한 문장 요약(검색·SEO)
---

# 시스템 아키텍처
```

| 필드 | 규칙 |
|---|---|
| `layout` | 항상 `default`. 커스텀 레이아웃은 만들지 않는다 |
| `title` | 메뉴·검색·`parent` 참조에 쓰인다. 바꾸면 자식 페이지의 `parent`도 같이 바꿔야 한다 |
| `permalink` | `docs/nav-spec.md`의 메뉴 표에 적힌 값만 쓴다. 여기 없는 경로는 만들지 않는다 |
| `parent` | **부모의 `title` 문자열과 정확히 일치**. 띄어쓰기·번호·마침표 하나라도 다르면 페이지가 메뉴에서 사라진다 |
| `grand_parent` | 3단계 페이지에만. 예: Sprint 페이지는 `parent: 단계별 개발 일정` + `grand_parent: 5. 마일스톤&WBS` |
| `nav_order` | 같은 층위 안의 순서. 장 페이지는 장 번호(1~15) |
| `has_children: true` | 자식 페이지를 거느리는 장 페이지에만 |
| `description` | 한 문장. 검색 미리보기와 메타 태그에 쓰인다 |

본문 첫 줄은 `# 제목` 한 번입니다. just-the-docs는 `title`을 자동으로 h1으로 넣지 않으므로 직접 씁니다. 사이트 안 링크는 항상 `{% raw %}{{ '/docs/...' | relative_url }}{% endraw %}` 형태로 씁니다.

메뉴 전체 구조(장 번호·파일·permalink·부모)는 저장소의 `docs/nav-spec.md`가 유일한 기준입니다. 새 페이지를 만들 때는 그 표에 먼저 한 줄을 넣고 파일을 만듭니다.

## `_data` 파일

| 파일 | 누가 읽나 | 내용 |
|---|---|---|
| `_data/project_sprints.yml` | 5장 [마일스톤&WBS]({{ '/docs/wbs.html' | relative_url }})의 로드맵·보드 include | 스프린트 4개(설계 09.03~04 / 구현 09.05~12 / 검증·v1 공개 09.13~16 / v1 이후), 각 스프린트의 `tasks` 카드. 카드는 `{id, date, status, priority, area, title, dod, output}`. `area`는 id 접두어(FE·BE·EVAL·QA·SC)로 정한다 |
| `_data/schedule.yml` | 5.1 [단계별 개발 일정]({{ '/docs/schedule/timeline.html' | relative_url }}) | 14일 표. `day: 1~14`, `date`, `dow`, `phase`, `theme`, `gate`, `note` |
| `_data/reading.yml` | 13장 연구 페이지의 읽기 층 include | 키는 각 연구 페이지의 permalink |
| `_data/research_figures.json` | 연구 페이지 그림 | `scripts/refresh_research_data.py`로 재생성 |

카드 상태를 바꾸려면 `project_sprints.yml`에서 해당 카드의 `status`(`todo` / `doing` / `review` / `done`) 한 줄을 고치고 커밋합니다. 진행률·보드·로드맵이 같은 데이터에서 계산됩니다. 지난 카드의 `date`는 바꾸지 않습니다 — 지연이 보여야 합니다.

YAML이 맞는지 확인하려면:

```bash
ruby -ryaml -e 'p YAML.load_file("_data/project_sprints.yml")["sprints"].size'
ruby -ryaml -e 'p YAML.load_file("_data/schedule.yml").size'
```

숫자가 나오면 정상입니다. 오류가 나면 대개 **들여쓰기**이거나, 값에 콜론(`:`)이 들어갔는데 따옴표를 안 씌운 경우입니다.

## 개발일지 추가하기

개발일지는 `jekyll/devlog/` 아래 파일 하나입니다. 파일명은 `YYYY-MM-DD-slug.md`.

```yaml
---
layout: default
title: "2026-10-08 홈서버 자동 기동 등록"
permalink: /docs/devlog/2026-10-08-autostart.html
parent: 12. 개발일지
nav_order: 12            # 기존 마지막 번호 + 1 (날짜 오름차순)
description: 재부팅 뒤 DB·백엔드가 자동으로 뜨도록 systemd 서비스를 등록한 기록.
---

# 2026-10-08 홈서버 자동 기동 등록

## 무엇을 했나
...
```

규칙 세 가지입니다.

1. `title`은 `YYYY-MM-DD 제목` 형태, 60자 안쪽으로. `parent`는 반드시 `12. 개발일지`.
2. `nav_order`는 날짜 오름차순으로 기존 마지막 번호 다음을 씁니다(2026-10-01 글이 11이므로 다음 글은 12).
3. [12. 개발일지]({{ '/docs/devlog.html' | relative_url }}) 목록 페이지(`jekyll/devlog/index.md`)의 표에 날짜 → 제목 → 링크 한 줄을 추가합니다.

무엇을 쓰나 — **결정과 이유, 측정치, 커밋 상태**를 씁니다. 커밋 목록만 나열하지 않습니다.

| 쓸 것 | 안 써도 되는 것 |
|---|---|
| 왜 A 대신 B 를 골랐는지 | 몇 시간 일했는지 |
| 바뀐 계약·규약·설정 | 커밋 목록 (git 에 이미 있음) |
| 하루 넘게 막혔던 문제와 해결 | 잘 된 일의 나열 |
| 다음에 밟을 함정, 이월 항목 | |

공개 사이트이므로 결말 스포일러, 운영 한도 값, 키 값은 적지 않습니다.

## 로컬에서 확인하기

고치기 전에 눈으로 확인하고 싶을 때 씁니다. `main`에 push 하면 GitHub Actions 가 빌드해서 Pages 에 올리므로 안 해도 배포는 됩니다.

```bash
bundle install                    # 최초 1회
bundle exec jekyll serve          # → http://localhost:4000 (기존 서버가 떠 있으면 다른 포트)
bundle exec jekyll build          # _site/ 생성
python3 scripts/check-site.py     # 링크·앵커·레이아웃 검사
node scripts/check-search.cjs     # 검색 색인 검사
python3 scripts/check_public.py   # 연구 금지어 검사
```

커밋 전에는 저장소 루트 `AGENTS.md`의 "절대 규칙"에 적힌 금지 표현 grep도 한 번 돌려 0건인지 확인합니다(개인 프로젝트 서술 원칙).

## 자주 겪는 문제

| 증상 | 원인 | 해결 |
|---|---|---|
| 새 페이지가 메뉴에 없음 | `parent`가 부모 `title`과 다름 | 부모 페이지의 `title`을 복사해 붙인다 |
| push 했는데 사이트가 그대로 | 빌드 실패 | 레포 Actions 탭에서 로그 확인. 사이트는 이전 버전이 유지된다 |
| 보드·일정이 비어 보임 | YAML 문법 오류 (들여쓰기·따옴표) | 위 YAML 확인 명령 |
| 두 페이지가 같은 주소 | `permalink` 중복 | `docs/nav-spec.md` 표와 대조 |
| 링크가 404 | 옛 경로 사용 | `{% raw %}{{ '/docs/...' | relative_url }}{% endraw %}` 로, 경로는 nav-spec의 permalink |
| 날짜가 하루 밀려 보임 | 타임존 | `_config.yml` 의 `timezone: Asia/Seoul` 확인 |

## 사이트 구조

```
_config.yml              사이트 설정 · 프로젝트 상수(started · v1_released · app_url)
_data/
  project_sprints.yml    5장 스프린트 보드·로드맵
  schedule.yml           5.1 14일 일정표
  reading.yml            13장 연구 읽기 층
  research_figures.json  13장 그림 데이터
_includes/research/      연구 페이지 include
jekyll/                  모든 문서 페이지 (장별 폴더)
  devlog/                12장 개발일지
  research/              13장 연구 보고서
  showcase/screens.html  15장 최종산출물
assets/img/screens/      구현 화면 24장
docs/nav-spec.md         메뉴·파일·permalink 계약 (빌드 제외)
scripts/                 검사·재생성 스크립트 (빌드 제외)
```

스타일(`_sass/`, `assets/css/`)과 레이아웃은 just-the-docs 기본을 쓰고, 색 팔레트만 `_sass/color_schemes/remakeday.scss`에 있습니다.
