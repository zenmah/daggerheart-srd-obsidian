---
tags:
  - Ancestry
  - CharacterOption
name: {{ name|upper }}
description: {{ description }}
---

# {{ name|upper }}

{{ description }}

## ANCESTRY FEATURES
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
