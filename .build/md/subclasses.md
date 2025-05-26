# {{ Name|upper }}

{{ Description }}
{% if Spellcast_Trait %}
## SPELLCAST TRAIT

{{ Spellcast_Trait }}
{% endif %}
## FOUNDATION FEATURE{% if Found_2_Name %}S{% endif %}

***{{ Found_1_Name }}:*** {{ Found_1_Text }}{% if Found_2_Name %}

***{{ Found_2_Name }}:*** {{ Found_2_Text }}{% endif %}

## SPECIALIZATION FEATURE{% if Spec_2_Name %}S{% endif %}

***{{ Spec_1_Name }}:*** {{ Spec_1_Text }}{% if Spec_2_Name %}

***{{ Spec_2_Name }}:*** {{ Spec_2_Text }}{% endif %}

## MASTERY FEATURE{% if Mast_2_Name %}S{% endif %}

***{{ Mast_1_Name }}:*** {{ Mast_1_Text }}{% if Mast_2_Name %}

***{{ Mast_2_Name }}:*** {{ Mast_2_Text }}{% endif %}

{{ Extras }}
