---
tags:
  - Community
  - CharacterOption
name: {{ name|upper }}
description: {{ description }}
---

# {{ name|upper }}

{{ description }}

*{{ note }}*

## COMMUNITY FEATURE
{% for feat in feats %}
***{{ feat.name }}:*** {{ feat.text }}
{% endfor %}
