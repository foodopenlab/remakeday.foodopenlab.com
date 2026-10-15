#!/usr/bin/env python3
"""kanban/*.yml (beyondbob.remakeday.com) -> _data/project_sprints.yml

사용법:
    python3 scripts/convert-kanban.py <src>/_data/kanban/*.yml [-o _data/project_sprints.yml]

- 다섯 파일의 카드를 전부 합친다(카드는 하나도 버리지 않는다).
- 담당자(member) 필드는 버리고, 카드 id 접두어와 태그로 `area`를 정한다.
- 날짜·id 순으로 정렬해 스프린트 4개에 나눈다.
- 제목·완료 기준·산출물 문구는 brainstorming.md §4의 치환 규칙대로 1인 개발 서술로 고친다.
"""
import argparse
import re
import sys
from datetime import date

import yaml

# ── 영역 결정 ────────────────────────────────────────────────────────────
# 실제 카드 접두어는 FE / APP / BE / AI / PM 이다(nav-spec의 FE/BE/EVAL/QA/SC와 다름).
PREFIX_AREA = {
    "FE": "fe",       # 웹 화면(아침·대화·권고)
    "APP": "fe",      # 노트·인스펙터 웹 화면 (원래 모바일 앱 → 웹으로 범위 조정)
    "BE": "be",       # 백엔드·API·도메인
    "AI": "ai",       # 에이전트·하네스·프롬프트
    "PM": "qa",       # 운영·인프라·릴리스·리뷰 (태그로 content/eval 분리)
    "EVAL": "eval",
    "QA": "qa",
    "SC": "content",
}
# 태그가 접두어보다 우선한다. 평가 실험·모델 선정은 eval, 서사·기획 문안은 content.
TAG_AREA = {
    "평가": "eval",
    "모델": "eval",
    "서사": "content",
    "기획": "content",
}

AREAS = [
    {"id": "fe", "label": "프론트"},
    {"id": "be", "label": "백엔드"},
    {"id": "ai", "label": "AI 에이전트"},
    {"id": "eval", "label": "평가"},
    {"id": "qa", "label": "QA·릴리스"},
    {"id": "content", "label": "시나리오·콘텐츠"},
]

STATES = [
    {"id": "todo", "label": "예정", "hint": "아직 착수 기록이 없는 작업"},
    {"id": "doing", "label": "진행 중", "hint": "작업 중이며 종료 조건 미충족"},
    {"id": "review", "label": "검토", "hint": "결과는 있으나 추가 확인 필요"},
    {"id": "done", "label": "완료", "hint": "구현·기록 확인"},
]

# ── 스프린트 경계 ────────────────────────────────────────────────────────
SPRINTS = [
    {
        "id": "sprint-1", "name": "Sprint 1", "period": "09.03 ~ 09.04", "phase": "설계",
        "start": date(2026, 9, 3), "end": date(2026, 9, 4),
        "goal": "기획서 v6 기준으로 기획 문서를 갱신하고 ERD·API 계약·에이전트 구성을 확정해 화면 5장 구현을 바로 시작할 수 있게 한다.",
        "exit": "ERD v1 FREEZE, API 계약 v1 발행, 도메인 계층 순수 함수 테스트가 CI에서 돈다.",
    },
    {
        "id": "sprint-2", "name": "Sprint 2", "period": "09.05 ~ 09.12", "phase": "구현",
        "start": date(2026, 9, 5), "end": date(2026, 9, 12),
        "goal": "절대 방어선 ①~⑤(대화·판정, 침묵 권고, 루프 축적, 민석 예외, 전이)를 코드로 구현하고 1루프 완주 알파를 거쳐 기능을 동결한다.",
        "exit": "18:00 기능 동결 뒤 회귀 시나리오 R1~R10 전건 통과, P0/P1 0건, 감사 어댑터 교체 시 엔진 코드 diff가 비어 있다.",
    },
    {
        "id": "sprint-3", "name": "Sprint 3", "period": "09.13 ~ 09.16", "phase": "검증·v1 공개",
        "start": date(2026, 9, 13), "end": date(2026, 9, 16),
        "goal": "세션/IP 제한·비용 상한·엔딩 텍스트를 공개 수준으로 닫고, RC 검증과 배포·롤백 리허설을 거쳐 v1을 공개한다.",
        "exit": "공개 오픈 + 30분 관측 정상 + 첫 실사용 로그 수집 확인.",
    },
    {
        "id": "sprint-4", "name": "Sprint 4", "period": "09.17 ~", "phase": "v1 이후",
        "start": date(2026, 9, 17), "end": None,
        "goal": "v1을 운영하면서 연구 재집계(09-18)와 개발일지를 이어 가고, v1에서 미룬 범위를 확장한다.",
        "exit": "종료일 없음. 작업이 생기는 대로 이 스프린트에 누적한다.",
    },
]

# ── 문구 치환 ────────────────────────────────────────────────────────────
# (카드 id, 필드) -> 새 문구. 기술 내용은 유지하고 팀 운영·담당자 표현만 1인 서술로 바꾼다.
OVERRIDES = {
    ("PM-01", "dod"): "개발 문서 사이트에서 기획·일정·타임라인이 열린다 (DNS 연결 완료)",
    ("FE-02", "dod"): "본문 행간 1.8 이상, 어절 단위 줄바꿈, 상태색 3종 확정",
    ("FE-19", "dod"): "웹 알파가 스테이징 URL에서 동작하고 1루프 완주",
    ("FE-29", "title"): "회귀 R1~R4 수행",
    ("AI-14", "title"): "SSE 이벤트 계약 확정",
    ("AI-14", "dod"): "advice/delta/tool/done/error 를 프론트와 백엔드가 같은 스펙으로 확정",
    ("AI-27", "dod"): "운영 프롬프트를 v1.0 으로 태깅, 이후 변경은 새 버전 태깅으로만",
    ("AI-36", "dod"): "프롬프트·모델 설정 변경 중단, 기록한 핫픽스 건만",
    ("APP-01", "title"): "화면 범위 조정 — 앱 → 노트·인스펙터",
    ("APP-01", "dod"): "기획서에 모바일 앱이 없음을 확인하고 노트·인스펙터를 웹 화면으로 확정",
    ("APP-01", "output"): "범위 확정",
    ("APP-02", "title"): "웹 개발 환경 셋업 · 디자인 토큰 공유",
    ("APP-02", "dod"): "같은 레포에서 dev 서버가 뜨고 아침·대화 화면과 같은 디자인 토큰을 사용",
    ("APP-04", "dod"): "필요한 필드가 계약에 다 있는지 확인하고 누락을 계약 변경 로그에 기록",
    ("APP-29", "title"): "회귀 R6·R10 수행",
    ("APP-33", "dod"): "공개 시연에서 그대로 띄울 수 있는 상태",
    ("BE-06", "dod"): "세션·루프·발화(SSE)·노트·인스펙터 스키마 공개, 프론트가 참조 시작",
    ("BE-14", "dod"): "프론트가 실 API로 아침→대화→응답을 완주, 계약 이슈 당일 해소",
    ("BE-31", "title"): "회귀 R5·R7 수행",
    ("BE-38", "dod"): "기록한 핫픽스만 처리",
    ("PM-01", "output"): "개발 허브 사이트",
    ("PM-04", "dod"): "상수 하드코딩 금지. 초기 5 / 5루프째 4 / 하한 3 을 잠정값으로 두고 확정 전까지 유효함을 기록",
    ("PM-04", "output"): "설정 파일 · 결정 기록",
    ("PM-05", "title"): "화면 범위 조정 (앱 → 노트·인스펙터)",
    ("PM-05", "dod"): "기획서에 모바일 앱이 없음을 확인하고 노트·인스펙터를 웹 화면으로 확정",
    ("PM-05", "output"): "범위 문서 갱신",
    ("PM-06", "dod"): "main 직접 push 차단, PR 템플릿에 방어선 항목 체크란 포함",
    ("PM-07", "title"): "ERD FREEZE 결정 · 기록",
    ("PM-07", "dod"): "18:00 ERD v1 확정, 이후 변경 절차(마이그레이션+클라이언트 대응) 기록",
    ("PM-10", "title"): "인프라 권한 · 접근 경로 정리",
    ("PM-10", "dod"): "서버·시크릿·배포 권한과 접근 경로를 문서로 정리 — 단일 장애점 제거",
    ("PM-10", "output"): "권한 정리",
    ("PM-22", "dod"): "기기별로 따라할 1루프 대본과 확인 항목 작성",
    ("PM-24", "title"): "알파 시연 — 1루프 완주",
    ("PM-24", "dod"): "여러 기기에서 아침→대화→죽음→아침을 완주",
    ("PM-25", "dod"): "미착수 방어선이 2개 이상이면 ⑨→⑧→⑦→⑥ 순으로 v1에서 제외하고 기록, 이후 재론 없음",
    ("PM-26", "dod"): "R2~R10 트리거 도달 여부 점검, 상위 5개에 기한 재지정",
    ("PM-30", "dod"): "18:00 이후 기능 PR 중단, 예외는 기록한 건만",
    ("PM-31", "dod"): "방어선 5개 + 기능/오류/데이터/보안/배포 항목을 체크리스트로 확정",
    ("PM-32", "title"): "전이 시연 — 엔진 diff 확인",
    ("PM-33", "dod"): "P0/P1 전건에 기한 지정, 하루 2회 갱신. 판정 로그 유실은 P0로 분류",
    ("PM-34", "dod"): "10개 시나리오가 표로 존재하고 각 시나리오에 통과 표시",
    ("PM-35", "dod"): "P0 잔여 0건 확인, 아니면 범위 재조정",
    ("PM-38", "title"): "엔딩 텍스트 검토",
    ("PM-38", "dod"): "4편을 통독하고 망설임 엔딩이 이야기로 성립하는지 확인",
    ("PM-40", "title"): "릴리스 체크리스트 최종 검증",
    ("PM-40", "dod"): "전 항목 통과 확인, 미통과 항목은 범위 축소로 처리",
    ("PM-41", "dod"): "무엇을·몇 분 안에 하는지 한 장으로 정리",
    ("PM-41", "output"): "운영 런북",
    ("PM-42", "dod"): "핫픽스 외 머지 중단, 예외는 기록한 건만",
    ("PM-48", "title"): "발화 예산 확정",
    ("PM-48", "dod"): "초기 회수·감소 곡선·하한을 확정하고 결정 로그에 근거와 함께 기록",
}

FORBIDDEN = re.compile(
    r"류준|장민석|신채연|이은상|팀장|팀원|우리 팀|원티드|Championship|해커톤|공개 투표|심사|출품|탈락|제출|D-[0-9]"
    r"|전원|5인|2인|합의|승인|주재|입회|담당자|PM 승인"
)


def area_of(card):
    for tag in card.get("tags") or []:
        if tag in TAG_AREA:
            return TAG_AREA[tag]
    prefix = card["id"].split("-", 1)[0]
    if prefix not in PREFIX_AREA:
        raise SystemExit(f"unknown id prefix {prefix!r} ({card['id']}) — PREFIX_AREA에 추가 필요")
    return PREFIX_AREA[prefix]


def convert_card(card):
    out = {
        "id": card["id"],
        "date": str(card["date"]),
        "status": card["status"],
        "priority": card["priority"],
        "area": area_of(card),
    }
    for field in ("title", "dod", "output"):
        out[field] = OVERRIDES.get((card["id"], field), card[field])
    for field in ("title", "dod", "output"):
        m = FORBIDDEN.search(out[field])
        if m:
            raise SystemExit(f"{card['id']}.{field}: 치환 누락 {m.group(0)!r}: {out[field]}")
    return out


def bucket(cards):
    sprints = []
    for s in SPRINTS:
        tasks = [
            c for c in cards
            if date.fromisoformat(c["date"]) >= s["start"] and (s["end"] is None or date.fromisoformat(c["date"]) <= s["end"])
        ]
        # 기간이 끝난 스프린트(v1 공개 이전)는 종료된 것으로 본다. 카드별 상태는 그대로 보존한다.
        status = "done" if s["end"] is not None else "doing"
        sprints.append({
            "id": s["id"],
            "name": s["name"],
            "period": s["period"],
            "phase": s["phase"],
            "goal": s["goal"],
            "exit": s["exit"],
            "status": status,
            "record_url": f"/docs/schedule/{s['id'].replace('-', '')}.html",
            "tasks": tasks,
        })
    return sprints


class Dumper(yaml.SafeDumper):
    pass


def _str(dumper, value):
    style = "'" if re.fullmatch(r"\d{4}-\d{2}-\d{2}|\d{2}\.\d{2} ~( \d{2}\.\d{2})?", value) else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


Dumper.add_representer(str, _str)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", help="source _data/kanban/*.yml")
    ap.add_argument("-o", "--output", default="_data/project_sprints.yml")
    args = ap.parse_args()

    cards = []
    for path in args.files:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        cards.extend(convert_card(c) for c in data["tasks"])

    ids = [c["id"] for c in cards]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate card ids")

    def sort_key(c):
        prefix, num = c["id"].split("-", 1)
        return (c["date"], prefix, int(num))

    cards.sort(key=sort_key)
    sprints = bucket(cards)

    doc = {
        "as_of": "2026-10-15",
        "status_note": "v1은 2026-09-16 공개. 이후 작업은 Sprint 4에 누적.",
        "states": STATES,
        "areas": AREAS,
        "sprints": sprints,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        f.write("# scripts/convert-kanban.py 가 생성. 손으로 고치지 말고 스크립트를 수정한다.\n")
        yaml.dump(doc, f, Dumper=Dumper, allow_unicode=True, sort_keys=False, width=200, default_flow_style=False)

    from collections import Counter
    print(f"cards: {len(cards)} -> {args.output}", file=sys.stderr)
    for s in sprints:
        print(f"  {s['id']}: {len(s['tasks'])} ({s['status']}) "
              + ", ".join(f"{k}={v}" for k, v in sorted(Counter(t['status'] for t in s['tasks']).items())), file=sys.stderr)
    print("  by area: " + ", ".join(f"{k}={v}" for k, v in sorted(Counter(c['area'] for c in cards).items())), file=sys.stderr)


if __name__ == "__main__":
    main()
