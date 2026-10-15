---
layout: default
title: Sprint 3 일자별 진행 사항
permalink: /docs/schedule/sprint3.html
parent: 단계별 개발 일정
grand_parent: 5. 마일스톤&WBS
nav_order: 3
---

{% assign sprint = site.data.project_sprints.sprints | where: "id", "sprint-3" | first %}

# Sprint 3 일자별 진행 사항 ({{ sprint.period }})

**단계** {{ sprint.phase }} · **목표** {{ sprint.goal }}

**스프린트 종료 기준** {{ sprint.exit }}

{% if sprint.tasks.size == 0 %}
이 스프린트에 기록된 과제가 아직 없습니다.
{% endif %}
{% assign dates = sprint.tasks | map: "date" | uniq %}
{% for d in dates %}
{% assign day = site.data.schedule | where: "date", d | first %}
{% assign todays = sprint.tasks | where: "date", d %}
## {{ d }}{% if day %} ({{ day.dow }}) — {{ day.theme }}{% endif %}
{: #d-{{ d }} }

{% if day %}**관문** {{ day.gate }}{% endif %}

| id | 영역 | 우선순위 | 제목 | 상태 | 완료 기준 |
|---|---|:--:|---|:--:|---|
{% for t in todays -%}
{% assign a = site.data.project_sprints.areas | where: "id", t.area | first -%}
{% assign s = site.data.project_sprints.states | where: "id", t.status | first -%}
| {{ t.id }} | {{ a.label }} | {{ t.priority }} | {{ t.title }} | {{ s.label }} | {{ t.dod }} |
{% endfor %}
{% endfor %}

---

[← Sprint 2]({{ '/docs/schedule/sprint2.html' | relative_url }}) · [단계별 개발 일정]({{ '/docs/schedule/timeline.html' | relative_url }}) · [Sprint 4 →]({{ '/docs/schedule/sprint4.html' | relative_url }})
