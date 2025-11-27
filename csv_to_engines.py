#!/usr/bin/env python3
import csv, os, re

OUT = "./searx_settings/engines"
os.makedirs(OUT, exist_ok=True)

with open("engines.csv", newline="", encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = re.sub(r'[^a-zA-Z0-9_-]', '_', row['key'])
        yml = f"""
name: "{row['name']}"
category: "{row['category']}"
country: "IN"
search_url: "{row['search_url_template']}"
js_render: {row['requires_js'].lower()}
"""
        with open(f"{OUT}/{key}.yml", "w", encoding="utf8") as out:
            out.write(yml)
