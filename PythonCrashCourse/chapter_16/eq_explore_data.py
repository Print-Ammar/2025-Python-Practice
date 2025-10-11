import json

filename = r"2025-Python-Practice\PythonCrashCourse\chapter_16\eq_data_1_day_m1.geojson"

with open(filename, encoding="utf-8") as f:
    all_eq_data = json.load(f)

readable_file = r'2025-Python-Practice\PythonCrashCourse\chapter_16\readable_eq_data.json'
with open(readable_file,'w') as f:
    json.dump(all_eq_data, f, indent = 4)
