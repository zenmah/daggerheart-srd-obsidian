---
tags:
  - Adversary
  - Creature
  - Statblock

name: '{{ name|upper }}'
tier: {{tier}}
type: {{type}}
description: '{{description}}'
motives_and_tactics: '{{motives_and_tactics}}'
difficulty: '{{difficulty}}'
thresholds: '{{thresholds}}'
hp: '{{hp}}'
stress: '{{ stress }}'
atk: '{{atk}}'
attack: '{{attack}}'
range: '{{range}}'
damage: '{{damage}}'
experience:{% if experience %}
  - '{{ experience }}'{% endif %}
feats:{% for feat in feats %}
- name: '{{ feat.name.split(" - ")[0] }}'
  type: '{{ feat.name.split(" - ")[1] }}'
  text: '{{feat.text}}'{% endfor %}
layout: Daggerheart Adversary
source: srd-adversary
statblock: true
---

# {{ name|upper }}

***Tier {{ tier }} {{ type }}***
*{{ description }}*
**Motives & Tactics:** {{ motives_and_tactics }}

> **Difficulty:** {{ difficulty }} | **Thresholds:** {{ thresholds }} | **HP:** {{ hp }} | **Stress:** {{ stress }}
> **ATK:** {{ atk }} | **{{ attack }}:** {{ range }} | {{ damage }}  {% if experience %}
> **Experience:** {{ experience }}{% endif %}

## FEATURES
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}