---
layout: default
title: "모델 평가"
permalink: /docs/test/model-evaluation.html
parent: "9. 시나리오 테스트"
nav_order: 2
description: "Exp 1(AI 모델 선정)의 단계·게이트·채택 구성·측정 범위를 한 장으로 요약하고 연구 보고서의 근거 절로 연결한다."
---

# 모델 평가

이 페이지는 연구 보고서 [Exp 1 — AI 모델 선정]({{ '/docs/research/model-selection.html' | relative_url }})의 요약이다.
수치·판정·예외의 정본은 그 페이지이며, 여기서는 무엇을 어떤 순서로 쟀고 무엇을 채택했는지, 그리고 무엇은 재지 않았는지만 적는다.

## 1. 전제 — 자원 예산

- 단일 GPU **RTX 5060 Ti 16GB**(15.19 GiB 가용)에 Core(계획·관리·채점)와 NPC(인물 대화) 두 슬롯이 동시에 상주해야 한다.
- 2026-09-13 실측으로 잡은 Core 예산은 **약 9.5 GiB**(NPC `exaone3.5:7.8b` 유지 시). 예산 판정은 디스크 용량이 아니라 `/api/ps`의 실측 VRAM으로만 한다.
- 후보는 기준선 `gemma3:12b`(7.49 GiB)와 `gemma4:12b`(7.51), `gemma4:e4b`(3.06), `qwen3.5:9b`(5.25), 온라인 `gemini-3-flash-preview`이며 thinking OFF(`-N`)/ON(`-T`)을 나누어 **총 9셀**이다. 로컬 4종은 모두 Q4_K_M 양자화다.
  → [§1 자원 제약]({{ '/docs/research/model-selection.html' | relative_url }}#1-자원-제약--모든-후보의-상한) · [§2.2 조건]({{ '/docs/research/model-selection.html' | relative_url }}#22-조건--비대칭-요인-설계)

## 2. 단계 — Funnel 5단계

처음부터 모든 셀을 전부 돌리지 않고, 앞 단계를 통과한 셀만 다음 단계로 보낸다.

| Stage | 내용 | 차단 조건 |
|---|---|---|
| 0 `protocol` | 셀당 1콜. 한국어 JSON 생성, thinking 제어, GPU 상주량 확인 | JSON 파싱 실패 → 해당 셀 제외 |
| 1 `smoke` | 9셀 × 4역할 × n=1 | FBR > 0.5 또는 SVR < 0.9 → 제외 |
| 2 `formal` | 통과 셀 × n=3 — 공식 수치 | `metrics.yml` 적립은 이 단계부터 |
| 3 `concurrency` | 최종 후보 + NPC 동시 상주 | 교대 구간 축출 발생 시 제외 |
| 4 `loop` | 최종 후보로 실서버 경로 게임 1회차 완주 | 크래시·폴백 폭주 → "게이트 통과했으나 루프 불가" |

채택 결정은 Stage 4 뒤에만 한다. → [§4.1 Funnel]({{ '/docs/research/model-selection.html' | relative_url }}#41-funnel)

## 3. 최종 게이트 — Hard (미달 시 후보 제외)

| # | 게이트 | 값 |
|---|---|---|
| C1 | SVR(형식 통과율) | ≥ 0.98 |
| C2 | Fallback Rate | ≤ 0.05 |
| C3 | LAR (planner) | = 1.0 |
| C4 | 극성쌍 PC3·PC4, SPC1·SPC2 | 네 문항 모두 기대 방향 일치 |
| C5 | 모델 GPU 상주량 | ≤ 9.5 GiB |
| C6 | TFR (`-T` 셀) | ≤ 0.1 |
| C11 | `advisor_answer` p95 | ≤ 5초 |
| C12 | `planner` p95 | ≤ 15초 |
| C13 | 밤 채점 대리지표(`evaluator p50 × 10`) | ≤ 30초 |

C11~C13은 UX 통념으로 잡은 값이며 플레이테스트로 체감 검증한 값이 아니다. 비열등은 역할별 이진 판정이며 통계적 비열등성 검정이 아니다.
→ [§5.1 Hard 게이트]({{ '/docs/research/model-selection.html' | relative_url }}#51-hard--미달-시-후보-제외) · [§5.3 대체 판정]({{ '/docs/research/model-selection.html' | relative_url }}#53-대체-판정-non-inferiority)

## 4. 단계별 결과 (2026-09-13 ~ 09-14, 로컬)

- **Stage 0**: `qwen3.5:9b-T`가 JSON 생성 실패(TFR 1.0)로 제외.
- **Stage 1**: 8셀 → 4셀. `-T` 셀 3개는 C11(p95 ≤ 5초) 미달, `qwen3.5:9b-N`은 PCA 0.50·C11 미달. 온라인 Gemini는 raw 지연은 통과했으나 프로세스 전역 10 RPM 페이싱을 포함한 effective 기준에서 C11·C13 미달로 기록.
- **Stage 2**: 4셀 × 31문항 × 3반복 = **372개 역할-문항 실행에서 최종 폴백 0, 오류 0**. 재생성 9회는 성공으로 세지 않고 따로 적었다. 극성쌍 통제(RM1)를 통과한 로컬 셀은 `gemma4:12b-N`뿐이었다.
  → [A.7]({{ '/docs/research/model-selection.html' | relative_url }}#a7-2026-09-13--e7-stage-2--formal--4역할--n3)
- **Stage 3**: `gemma4:12b-N` pair peak 12.34 GiB, `gemma4:e4b-N` 7.89 GiB. 두 후보 모두 교대 6스냅샷에서 NPC와 동시 상주, 축출·오프로드 0.
  → [A.9]({{ '/docs/research/model-selection.html' | relative_url }}#a9-2026-09-14--e7-stage-3--concurrency--후보--npc-동시-상주)
- **Stage 4**: 두 후보 모두 실서버 경로 1회차 완주, 크래시 0, 폴백 0/17(12b 61.1s, e4b 35.6s). 점수는 판정 기준이 아니다.
  → [A.10]({{ '/docs/research/model-selection.html' | relative_url }}#a10-2026-09-14--e7-stage-4--loop--루프-스모크-1회차-완주)

## 5. 채택 구성

### 로컬 구성 (2026-09-14 결정)

- **Core `gemma4:12b`, thinking off** — 비열등 산식의 문자적 결론(VRAM 7.51 vs 7.49 GiB, evaluator p50 2,179 vs 976ms)이 아니라 Funnel 0~4 실측 전체를 근거로 한 결정. 극성쌍 통과, 실플레이 evaluator 통제 기대 일치 0.57(4셀 중 최상), C11~C13 통과, 무축출 공존, 루프 완주.
  → [채택 기록]({{ '/docs/research/model-selection.html' | relative_url }}#채택-2026-09-14-사용자-결정)
- **NPC `kanana1.5:8b`(Apache 2.0)** — 기존 `exaone3.5:7.8b`가 연구 전용 라이선스로 확인돼 상업 가능 후보 3종(`gemma4:e4b`·`kanana1.5:8b`·`midm2.0:mini`)을 같은 파이프라인으로 평가. kanana는 7세 정책 4/5, p95 1,917ms, Core와의 pair 12.42 GiB로 무축출. 롤백은 설정 한 줄.
  → [A.17]({{ '/docs/research/model-selection.html' | relative_url }}#a17-2026-09-14--npc-상업-라이선스-조사--상업-가능-후보-3종-평가)

### 공개 운영 구성 (2026-09-17 확정, 외부 API)

공개 운영 기간에는 홈서버 GPU 1장으로 동시 접속을 감당할 수 없어 같은 러너·같은 게이트로 외부 API를 비교했다.

| 역할 | 로컬 개발·롤백 | 공개 운영 | 결정 기록 |
|---|---|---|---|
| Core | `gemma4:12b` (think off) | `claude-sonnet-5` | A.19 |
| NPC | `kanana1.5:8b` | `claude-haiku-4-5` | A.19 |
| 대안 규칙 정렬(임베딩) | `bge-m3` 1024차원 | `gemini-embedding-001` 2560차원 | A.21 |

- **Core**: Sonnet 5는 n=1 PCA 0.90·eval 0.71, n=3 PCA 0.9667·eval 0.7143으로 의미 품질 게이트 통과. 지연 게이트는 n=1에서 C11 통과·C13 미달, n=3에서 C11 미달·C13 통과로 **반복 사이에 뒤집혔다**(변동성으로 해석). 5회차 self-play에서 planner 재생성 2·폴백 1(초기), 확인판 재생성 1·폴백 0. Opus 5는 PCA 1.00·eval 0.57(경계) 통과이나 C11·C13 둘 다 미달, 비용 2~3배라 채택하지 않음.
- **NPC**: 20케이스 × 2반복에서 구조 실패 0, 재생성 Haiku 2·Sonnet 1(재생성 0 게이트는 미충족), 중간값 Haiku 1.9~2.3s. 채점기를 `gemma4:12b`로 통일한 재측정에서 7세 정책 4/5.
- 이 채택은 지연·재생성 예외를 기록한 결정이며 **전 게이트 일괄 통과 선언이 아니다.**
  → [A.19]({{ '/docs/research/model-selection.html' | relative_url }}#a19) · [비교표]({{ '/docs/research/model-selection.html' | relative_url }}#무엇을-재는가--로컬-채택-구성-vs-외부-api-같은-러너같은-기준)

### 임베딩 (2026-09-18)

검수 22문장 골든에서 첫 추천 적중(top-1): Gemini 1536·2560 21/22(0.955), qwen@2560 20/22(0.909), bge-m3 20/22(0.909), qwen@1536 18/22(0.818), 어간 겹침 8/22(0.364). 순위 1회 계산 p50은 qwen 84~86ms, bge 109ms, Gemini 407~418ms. 로컬은 VRAM 동주 실측(gemma4·kanana·bge-m3 셋 다 온칩, 14,187 MiB)을 거쳐 `bge-m3`를 채택했다.
→ [A.21]({{ '/docs/research/model-selection.html' | relative_url }}#a21)

### 공개 운영 조합 세 축 실측 (2026-09-18)

Sonnet 5 채점 캘리브레이션 정답형 100·절반형 54.8·오답형 0(n=1), Haiku 4.5 정체 누설 하네스 on 0%·off 50%, self-play 5회차 오류·폴백 0. 기록된 호출 기준 판당 $0.46, NPC 발화까지 환산하면 약 $0.9~1.2(추정). 세 축 모두 n=1~2라 **게이트 통과 선언이 아니라 실측 기록**이다.
→ [A.23]({{ '/docs/research/model-selection.html' | relative_url }}#a23-2026-09-18--제출-조합sonnet-5--haiku-45-세-축-실측--채점-캘리브레이션정체-누설self-play원숭이손)

## 6. 측정한 것과 측정하지 않은 것

| 측정함 | 측정하지 않음 |
|---|---|
| 형식 통과율·폴백률·극성쌍·역할별 지연 p50/p95 (Stage 2, n=3) | `manager_paw` 창작 품질 (정량 비교 범위 밖) |
| NPC·Core 동시 상주와 축출 (교대 3라운드) | 허용 응답시간 안의 **동시 사용자 수** (부하 시험 없음) |
| 실서버 경로 1회차·5회차 완주, 크래시·폴백 | 재미 게이트 (완주율·이탈 지점만 DB로 셀 수 있음) |
| 외부 API의 같은 게이트 비교 (러너 수정·judge 교체 전후 구분) | 온라인 provider의 연속 호출 실제 벽시계 (effective는 유도 추정) |
| 검수 22문장 임베딩 top-1/top-3·지연·VRAM 동주 | 사람의 블라인드 페르소나 평가, 새 참가자의 5회차 실제 플레이 |
| 공개 운영 조합 채점 캘리브레이션·누설·self-play (n=1~2) | 통계적 비열등성 검정, 모델 간 순위의 유의성 |

채택은 모든 기준의 일괄 통과나 통계적 비열등성 증명을 뜻하지 않는다. 한계와 재현 조건은 [한계와 재현 방법]({{ '/docs/research/limitations.html' | relative_url }})을 따른다.
