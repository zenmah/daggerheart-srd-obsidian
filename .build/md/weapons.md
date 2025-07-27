---
tags:
  - Item
  - Weapon
name: '{{ name|upper }}'
trait: '{{ trait }}'
range: '{{ range }}'
damage: '{{ damage }}'
burden: '{{ burden }}'
feat_name: {% if feat_name %}'{{ feat_name }}'{% endif %}
feat_text: {% if feat_name %}'{{ feat_text }}'{% endif %}
primary_or_secondary: '{{ primary_or_secondary }} Weapon'
tier: {{ tier }}
---

# {{ name|upper }}

**Trait:** {{ trait }}; **Range:** {{ range }}; **Damage:** {{ damage }}; **Burden:** {{ burden }}

**Feature:** {% if feat_name %}***{{ feat_name }}:*** {{ feat_text }}{% else %}—{% endif %}

*{{ primary_or_secondary }} Weapon - Tier {{ tier }}*
