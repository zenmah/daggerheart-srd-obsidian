# Daggerheart SRD Build

## OCR the Pages Using ChatGPT

    cd build
    echo "OPENAI_API_KEY=XXXX" > .env
    pipenv install
    pipenv run python parse.py

## Adversaries CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables.

Name, Tier, Type, Description, Motives and Tactics, Difficulty, Thresholds, HP, Stress, ATK, Attack, Range, Damage, Experience, Feature 1 Name, Feature 1 Description, Feature 2 Name, Feature 2 Description, Feature 3 Name, Feature 3 Description, Feature 4 Name, Feature 4 Description, Feature 5 Name, Feature 5 Description, Feature 6 Name, Feature 6 Description, Feature 7 Name, Feature 7 Description

## Environments CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables.

Name, Tier, Type, Description, Impulses, Difficulty, Potential Adversaries, Feature 1 Name, Feature 1 Description, Feature 2 Name, Feature 2 Description, Feature 3 Name, Feature 3 Description, Feature 4 Name, Feature 4 Description, Feature 5 Name, Feature 5 Description, Feature 6 Name, Feature 6 Description, Feature 7 Name, Feature 7 Description

## Cards CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables.

Name, Level, Domain, Spell or Ability, Recall Cost, Text

## Classes CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables. Ignore subclass information. Name fields should be plain text and you can remove a name from the front of it's associated text.

Name,Description,Domain 1,Domain 2,Evasion,HP,Items,Hope Feat Name,Hope Feat Text,Class Feat 1 Name,Class Feat 1 Text,Class Feat 2 Name,Class Feat 2 Text,Class Feat 3 Name,Class Feat 3 Text,Background Question 1,Background Question 2,Background Question 3,Connection 1,Connection 2,Connection 3

## Subclasses CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables. Ignore subclass information. Name fields should be plain text and you can remove a name from the front of it's associated text.

Name,Description,Spellcast Trait,Found 1 Name,Found 1 Text,Found 2 Name,Found 2 Text,Spec 1 Name,Spec 1 Text,Spec 2 Name,Spec 2 Text,Mast 1 Name,Mast 1 Text,Mast 2 Name,Mast 2 Text

## Communities CSV Prompt (GPT 4.1)

You are a markdown to csv converter. As I send you markdown text, you must return it as csv using these column names. Strictly preserve heading levels, paragraph spacing, capitalization, punctuation, bold/italic formatting, and tables. Ignore subclass information. Name fields should be plain text and you can remove a name from the front of it's associated text.

Name,Description,Note,Feat Name,Feat Text

## Overwrite Tables

    pipenv run python downify.py && \
    rm -Rf ../abilities && mv abilities .. && \
    rm -Rf ../adversaries && mv adversaries .. && \
    rm -Rf ../armor && mv armor .. && \
    rm -Rf ../classes && mv classes .. && \
    rm -Rf ../communities && mv communities .. && \
    rm -Rf ../consumables && mv consumables .. && \
    rm -Rf ../environments && mv environments .. && \
    rm -Rf ../items && mv items .. && \
    rm -Rf ../subclasses && mv subclasses .. && \
    rm -Rf ../weapons && mv weapons ..

## And So Much Cleanup...

## Regexes to Remember

### Find/Replace Table Links

        \|\n\| \*\*([^\*]*)?\*\*
        |\n| [$1](../weapons/$1.md)

### Replace Spaces in Markdown Links

        \]\((.*) (.*)\)
        ]($1%20$2)
