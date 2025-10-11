import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = r"2025-Python-Practice\PythonCrashCourse\chapter_16\eq_data_30_day_m1.geojson"

with open(filename, encoding="utf-8") as f:
    all_eq_data = json.load(f)

readable_file = r'2025-Python-Practice\PythonCrashCourse\chapter_16\readable_eq_data.json'
with open(readable_file,'w') as f:
    json.dump(all_eq_data, f, indent = 4)

all_eq_dicts = all_eq_data['features']
all_md_dicts = all_eq_data["metadata"]

name = all_md_dicts['title']

mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_text.append(eq_dict['properties']['title'])
data = [{
    'type' : 'scattergeo',
    'lat' : lats,
    'lon' : lons,
    'text' : hover_text,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'colorscale': "Viridis",
        'reversescale' : True,
        'colorbar' : {'title':'Magnitude'}
    }
}]
my_layout = Layout(title= name)
fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig,filename='global_earthquakes.html')