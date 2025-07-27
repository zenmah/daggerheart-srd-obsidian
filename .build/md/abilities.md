---
tags:
  - Ability
  - CharacterOption
name: '{{ name|upper }}'
level: {{ level }}
domain: '{{ domain }}'
type: '{{ type }}'
recall: '{{ recall }}'
description: '{{ text }}'
---
# {{ name|upper }}

> **Level {{ level }} {{ domain }} {{ type }}**  
> **Recall Cost:** {{ recall }}

{{ text }}
