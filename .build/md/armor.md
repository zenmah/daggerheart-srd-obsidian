---
tags:
  - Item
  - Armor
name: {{ name|upper }}
base_thresholds: '{{ base_thresholds }}'
base_score: '{{ base_score }}'
feat_name: {% if feat_name %}'{{ feat_name }}'{% endif %}
feat_text: {% if feat_name %}'{{ feat_text }}'{% endif %}
tier: {{ tier }}
---

# {{ name|upper }}

**Base Thresholds:** {{ base_thresholds }}; **Base Score:** {{ base_score }}

**Feature:** {% if feat_name %}***{{ feat_name }}:*** {{ feat_text }}{% else %}—{% endif %}

*Armor - Tier {{ tier }}*
