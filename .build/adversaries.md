# {{ Name }}

- ***Tier {{ Tier }} {{ Type }}:*** *{{ Description }}*
- **Motives & Tactics:** {{ Motives_and_Tactics }}
- **Difficulty:** {{ Difficulty }} | **Thresholds:** {{ Thresholds }} | **HP:** {{ HP }} | **Stress:** {{ Stress }}
- **ATK:** {{ ATK }} | **{{ Attack }}:** {{ Range }} | {{ Damage }}
- **Experience:** {{ Experience }}

### FEATURES
{% for feature in features %}
**{{ feature.name }}:** {{ feature.desc }}
{% endfor %}