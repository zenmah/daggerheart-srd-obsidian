---
tags:
  - Environment
  - Statblock

name: '{{ name|upper }}'
tier: {{tier}}
type: {{type}}
description: '{{description}}'
difficulty: '{{difficulty}}'
impulses: '{{ impulses }}'
potential_adversaries: '{{ potential_adversaries }}'
feats:{% for feat in feats %}
- name: '{{ feat.name.split(" - ")[0] }}'
  type: '{{ feat.name.split(" - ")[1] }}'
  text: '{{feat.text}}'{% endfor %}
layout: Daggerheart Environment
source: srd-adversary
statblock: true
---

# {{ name|upper }}

***Tier {{ tier }} {{ type }}***  
*{{ description }}*  
**Impulses:** {{ impulses }}

> **Difficulty:** {{ difficulty }}  
> **Potential Adversaries:** {{ potential_adversaries }}

## FEATURES
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}