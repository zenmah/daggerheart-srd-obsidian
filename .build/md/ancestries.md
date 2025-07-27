---
tags:
  - Ancestry
  - CharacterOption
name: '{{ name|upper }}'
description: '{{ description }}'
feats:{% for feat in feats %}
- name: '{{ feat.name }}'
  text: '{{feat.text}}'{% endfor %}
---

# {{ name|upper }}

{{ description }}

## ANCESTRY FEATURES
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
