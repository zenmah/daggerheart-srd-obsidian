# Daggerheart SRD Build

## OCR

    cd build
    echo "OPENAI_API_KEY=XXXX" > .env
    pipenv install
    pipenv run python parse.py

## Adversaries Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables.

Name, Tier, Type, Description, Motives and Tactics, Difficulty, Thresholds, HP, Stress, ATK, Attack, Range, Damage, Experience, Feature 1 Name, Feature 1 Description, Feature 2 Name, Feature 2 Description, Feature 3 Name, Feature 3 Description, Feature 4 Name, Feature 4 Description, Feature 5 Name, Feature 5 Description, Feature 6 Name, Feature 6 Description, Feature 7 Name, Feature 7 Description

## Environments Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables.

Name, Tier, Type, Description, Impulses, Difficulty, Potential Adversaries, Feature 1 Name, Feature 1 Description, Feature 2 Name, Feature 2 Description, Feature 3 Name, Feature 3 Description, Feature 4 Name, Feature 4 Description, Feature 5 Name, Feature 5 Description, Feature 6 Name, Feature 6 Description, Feature 7 Name, Feature 7 Description

## Overwrite Tables

    pipenv run python detable.py && \
    rm -Rf ../adversaries && mv adversaries .. && \
    rm -Rf ../environments && mv environments ..
