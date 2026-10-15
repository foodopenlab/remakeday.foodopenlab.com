#!/usr/bin/env python3
"""jekyll/ 아래 페이지의 front matter를 읽어 메뉴 트리를 검사하고 출력한다.

검사 항목
- front matter가 YAML로 파싱되는가
- title · permalink · nav_order 가 있는가
- parent / grand_parent 가 실제 존재하는 title 인가
- permalink 중복이 없는가

사용: python3 scripts/check-navigation.py [--toc]   (--toc: 2장 목차용 markdown 출력)
"""
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAGES = sorted(list((ROOT / "jekyll").rglob("*.md")) + list((ROOT / "jekyll").rglob("*.html")))
if (ROOT / "index.markdown").exists():
    PAGES.insert(0, ROOT / "index.markdown")


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, "front matter 없음"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "front matter 종료 없음"
    try:
        return yaml.safe_load(parts[1]) or {}, None
    except yaml.YAMLError as e:
        return None, f"YAML 오류: {e}"


def main():
    want_toc = "--toc" in sys.argv
    pages, errors = [], []
    for p in PAGES:
        fm, err = front_matter(p)
        rel = p.relative_to(ROOT)
        if err:
            errors.append(f"{rel}: {err}")
            continue
        for key in ("title", "permalink"):
            if key not in fm:
                errors.append(f"{rel}: {key} 없음")
        if "nav_order" not in fm and not fm.get("nav_exclude"):
            errors.append(f"{rel}: nav_order 없음")
        pages.append((rel, fm))

    titles = {fm.get("title") for _, fm in pages}
    seen = {}
    for rel, fm in pages:
        for key in ("parent", "grand_parent"):
            if key in fm and fm[key] not in titles:
                errors.append(f"{rel}: {key} '{fm[key]}' 에 해당하는 title 없음")
        link = fm.get("permalink")
        if link in seen:
            errors.append(f"{rel}: permalink 중복 ({seen[link]})")
        seen[link] = rel

    roots = sorted(
        [(rel, fm) for rel, fm in pages if "parent" not in fm],
        key=lambda x: float(x[1].get("nav_order", 999)),
    )

    def children(title):
        return sorted(
            [(rel, fm) for rel, fm in pages if fm.get("parent") == title],
            key=lambda x: float(x[1].get("nav_order", 999)),
        )

    lines = []
    for rel, fm in roots:
        if want_toc:
            lines.append(f"- [{fm['title']}]({{{{ '{fm['permalink']}' | relative_url }}}})")
        else:
            lines.append(f"{fm['title']}  ({fm['permalink']})  <- {rel}")
        for crel, cfm in children(fm["title"]):
            if want_toc:
                lines.append(f"  - [{cfm['title']}]({{{{ '{cfm['permalink']}' | relative_url }}}})")
            else:
                lines.append(f"    {cfm['title']}  ({cfm['permalink']})  <- {crel}")
            for grel, gfm in children(cfm["title"]):
                if want_toc:
                    lines.append(f"    - [{gfm['title']}]({{{{ '{gfm['permalink']}' | relative_url }}}})")
                else:
                    lines.append(f"        {gfm['title']}  ({gfm['permalink']})  <- {grel}")

    print("\n".join(lines))
    print(f"\n페이지 {len(pages)}개", file=sys.stderr)
    if errors:
        print("\n".join("ERROR " + e for e in errors), file=sys.stderr)
        sys.exit(1)
    print("검사 통과", file=sys.stderr)


if __name__ == "__main__":
    main()
