---
layout: default
title: 운영 런북
permalink: /docs/inspection/runbook.html
parent: 10. 최종 검수
nav_order: 2
description: 실제로 실행하는 절차. 환경·시크릿·DNS 표, 스테이징·프로덕션 배포 명령, 롤백 순서, 백업·복구, 장애 증상별 대응을 명령과 순서 그대로 적어 급할 때 생각하지 않고 따라간다.
---

# 운영 런북

> **이 문서는 「무엇을 할지」가 아니라 「어떻게 할지」입니다**
> 설계 판단은 <a href="{{ '/docs/high-level-design/infra.html' | relative_url }}">인프라 및 배포</a>에 있습니다. 여기는 손이 움직이는 절차만 둡니다. 값이 확정될 때마다 이 문서를 채웁니다.

> **기준 시점**
> 아래 배포·롤백 절차는 v1 공개 전에 스테이징·프로덕션 서버 구성을 전제로 쓴 것입니다. 실제 v1(2026-09-16)은 프론트 Vercel · 백엔드 홈서버(uvicorn 8500) + Cloudflare 터널 `api.remakeday.com` · DB docker compose(5435)로 공개했습니다. 홈서버 쪽 기동 절차는 <a href="{{ '/docs/devlog/2026-09-24-dev-log.html' | relative_url }}">2026-09-24 개발일지</a>에 있습니다.

## 환경

| 대상 | 주소 | 비고 |
|---|---|---|
| 스테이징 서버 | *(Day 2 확정)* | 배포 전 스모크 대상 |
| 프로덕션 서버 | *(Day 8 확정)* | |
| 스테이징 DB | *(Day 2 확정)* | 복구 리허설은 여기서만 |
| 프로덕션 DB | *(Day 8 확정)* | |
| GitHub | `github.com/remakeday` | 앱 저장소 `com.remakeday` |
| 도메인 DNS | `remakeday.com` | Cloudflare (09-16 이전) |

## 시크릿 목록

값은 **여기 적지 않습니다.** 이름과 저장 위치만 관리합니다.

| 키 이름 | 용도 | 저장 위치 |
|---|---|---|
| `DATABASE_URL` | DB 접속 | GitHub Secrets + 서버 `.env` |
| `JWT_SECRET_KEY` | 토큰 서명 (stg/prod 다름) | 동일 |
| `JWT_REFRESH_SECRET` | 갱신 토큰 서명 | 동일 |
| `LLM_API_KEY` | LLM 프로바이더 | 동일 |
| `LLM_DAILY_LIMIT_USD` | 일일 비용 상한 | 동일 |
| `STORAGE_PATH` / 버킷 자격증명 | 파일 업로드 | 동일 |
| `ALERT_WEBHOOK_URL` | 장애 알림 | GitHub Secrets |

**레포에는 `.env.example` 만 커밋합니다** — 키 이름만 있고 값은 비어 있습니다. 실제 한도 값은 배포 `.env`에서 정하고 문서에 적지 않습니다.

## DNS

| 이름 | 타입 | 가리키는 곳 | 용도 |
|---|---|---|---|
| 개발 문서 사이트 | CNAME | GitHub Pages | 이 사이트 |
| `api.…` | A / 터널 | 프로덕션 백엔드 | 백엔드 API |
| `api-stg.…` | A | 스테이징 서버 IP | 스테이징 API |
| `www` / apex | *(Day 2 확정)* | | 서비스 웹 |

## 절차 — 스테이징 배포

정상 흐름에서는 자동입니다. 수동으로 밀어야 할 때만 씁니다.

```bash
# 1) 현재 상태 확인
ssh <stg> "docker compose ps"

# 2) 최신 이미지로 교체
ssh <stg> "cd /srv/app && docker compose pull && docker compose up -d"

# 3) 마이그레이션
ssh <stg> "docker compose exec api alembic upgrade head"

# 4) 확인 — 여기서 끝내지 말고 반드시 스모크까지
curl -fsS https://api-stg.…/health && echo OK
./scripts/smoke.sh https://api-stg.…
```

## 절차 — 프로덕션 배포 (v1 공개)

> **순서를 바꾸지 않는다**
> 백업 → 마이그레이션 → API → 웹. 웹을 먼저 올리면 아직 없는 API 를 부릅니다.

```bash
# 0) 백업 먼저 — 예외 없음
ssh <prod> "/srv/scripts/backup.sh manual-$(date +%Y%m%d-%H%M)"

# 1) 태그 확인
git log --oneline -1 v1.0.0

# 2) 마이그레이션 (소요시간 기록)
ssh <prod> "cd /srv/app && docker compose exec api alembic upgrade head"

# 3) API 교체
ssh <prod> "cd /srv/app && docker compose pull api && docker compose up -d api"
curl -fsS https://api.…/health

# 4) 웹 배포 (Actions 승인)

# 5) 검증 — 릴리스 체크리스트 기능 항목 전부
./scripts/smoke.sh https://api.…
```

## 절차 — 롤백

**Day 13(9/15)에 리허설로 한 번 해봅니다.** 각 단계 소요시간을 아래 표에 기록합니다.

| 순서 | 대상 | 명령 | 목표 | 실측 |
|---|---|---|---|---|
| 1 | 판단 | 롤백 여부 결정 | 1분 | |
| 2 | 웹 | Vercel 이전 배포로 되돌림 | 1분 | |
| 3 | API | `docker compose up -d api` (이전 태그) | 3분 | |
| 4 | DB | `alembic downgrade -1` | 5분 | |
| 5 | 공지 | 상태 공지 | 1분 | |

> **DB 롤백이 가장 위험하다**
> 그래서 공개 직전 마이그레이션은 **추가만** 합니다. 컬럼 삭제·이름 변경은 공개 후 안정화되고 나서 합니다.

## 절차 — 백업 · 복구

```bash
# 백업 (자동: 매일 03:00)
ssh <prod> "/srv/scripts/backup.sh"

# 복구 리허설 — Day 11(9/13) BE-33
#   운영 DB 에 절대 복구하지 않는다. 반드시 별도 DB 에.
ssh <stg> "createdb restore_test && pg_restore -d restore_test /backups/latest.dump"
ssh <stg> "DATABASE_URL=…restore_test docker compose up -d api-restore-test"
curl -fsS https://api-stg.…:8301/health
```

## 장애 대응

| 증상 | 먼저 볼 것 | 그다음 |
|---|---|---|
| API 5xx 급증 | `docker compose logs api --tail 200` | DB 연결 → 마이그레이션 상태 |
| 응답 지연 | DB 커넥션 풀 사용률 | 느린 쿼리 (N+1 의심) |
| LLM 응답 실패 | 프로바이더 상태 · 쿼터 | 이 게임은 degrade 가 없다 — 즉시 롤백 판단 |
| 판정이 안 돌아옴 | LLM 프로바이더 상태 · 스키마 통과율 | 하네스 재시도 로그 |
| 전체 다운 | 프록시 → 컨테이너 → DB 순 | 롤백 판단 |

## 공개 직후 2시간 모니터링

| 보는 것 | 어디서 |
|---|---|
| 헬스체크 · 배포 상태 | `/health`, Vercel 배포 로그 |
| API 에러 로그 · DB | `docker compose logs api`, 커넥션 풀 |
| 스키마 실패율 · 토큰 비용 | 하네스 이벤트, LLM 콘솔 지출 |
| 웹 JS 오류 · 실패 요청 | 브라우저 콘솔, 네트워크 탭 |
| 노트·인스펙터 · 모바일 웹 유입 | 실사용 로그 |

이상이 보이면 **고치기 전에 롤백 여부를 먼저 판단합니다.** 고치려다 롤백 타이밍을 놓치는 게 가장 나쁜 결과입니다.
