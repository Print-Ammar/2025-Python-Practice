import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url)
hn_dicts = r.json()
readable_file =  r'2025-Python-Practice\PythonCrashCourse\chapter_17\readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(hn_dicts,f,indent = 4)