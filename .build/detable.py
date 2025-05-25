import csv
import os
import re
from jinja2 import Template

def normalize_key(key):
    if not key:
        return None
    return key.replace(' ', '_').replace('&', 'and').replace('-', '_')

def safe_filename(name):
    name = re.sub(r'[^\w\-_ ]', '', name.strip()).title()
    return name.title()

def process_csv_to_md(csv_file, template_file, output_dir, feature_count=7):
    os.makedirs(output_dir, exist_ok=True)
    with open(template_file) as f:
        template = Template(f.read())
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for orig_row in reader:
            row = {normalize_key(k): v for k, v in orig_row.items() if k}
            # Feature extraction (optional—only if relevant to template/csv)
            features = []
            for i in range(1, feature_count + 1):
                fname = row.get(f'Feature_{i}_Name', '')
                fdesc = row.get(f'Feature_{i}_Description', '')
                if fname and fdesc:
                    features.append({'name': fname.strip(), 'desc': fdesc.strip()})
            row['features'] = features
            filename = safe_filename(row['Name'])
            content = template.render(**row)
            with open(f"{output_dir}/{filename}.md", 'w', encoding='utf-8') as outfile:
                outfile.write(content)

# List your jobs: (csv, template, output_dir)
jobs = [
    ("adversaries.csv", "adversaries.md", "adversaries"),
    ("environments.csv", "environments.md", "environments"),
]

for csv_file, template_file, output_dir in jobs:
    process_csv_to_md(csv_file, template_file, output_dir)
