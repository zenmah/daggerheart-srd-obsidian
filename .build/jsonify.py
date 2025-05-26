import csv
import json
import os
from collections import OrderedDict
from titlecase import titlecase


def normalize_header(header):
    return header.strip().lower().replace(" ", "_")


def csv_to_json(csv_path, json_path):
    """Converts a CSV file to a JSON file, normalizing headers, titlecasing 'name', and omitting empty fields."""
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(csv_path, newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        if not reader.fieldnames:
            return  # skip empty CSVs
        normalized_fieldnames = [normalize_header(h) for h in reader.fieldnames]
        data = []
        for row in reader:
            ordered_row = OrderedDict()
            for orig, norm in zip(reader.fieldnames, normalized_fieldnames):
                value = row[orig]
                if value is None:
                    continue
                value = value.strip()
                if value == "":
                    continue
                if norm == "name":
                    value = titlecase(value)
                ordered_row[norm] = value
            if ordered_row:  # only append non-empty rows
                data.append(ordered_row)
    with open(json_path, "w", encoding="utf-8-sig") as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)


def main():
    csv_dir = "csv"
    json_dir = "json"
    os.makedirs(json_dir, exist_ok=True)
    for filename in os.listdir(csv_dir):
        if filename.lower().endswith(".csv"):
            csv_path = os.path.join(csv_dir, filename)
            json_filename = os.path.splitext(filename)[0] + ".json"
            json_path = os.path.join(json_dir, json_filename)
            print(f"Converting {csv_path} → {json_path}")
            csv_to_json(csv_path, json_path)


if __name__ == "__main__":
    main()
