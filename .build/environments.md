# {{ Name }}

- ***{{ Tier }}:*** *{{ Description }}*
- **Impulses:** {{ Impulses }}
- **Difficulty:** {{ Difficulty }}
- **Potential Adversaries:** {{ Potential_Adversaries }}

### FEATURES
{% for feature in features %}
**{{ feature.name }}:** {{ feature.desc }}
{% endfor %}