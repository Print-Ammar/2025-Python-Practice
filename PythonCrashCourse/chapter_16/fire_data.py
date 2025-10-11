import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

file = r"2025-Python-Practice\PythonCrashCourse\chapter_16\world_fires_1_day.csv"

with open(file) as f:
    reader = csv.reader(f)
    column_header = next(reader)

    for index, column_title in enumerate(column_header):
        print(index, column_title)
    
    lats, lons, brightness, dates= [], [], [], []

    for row in reader:
        lats.append(float(row[int(column_header.index("latitude"))]))
        lons.append(float(row[int(column_header.index("longitude"))]))
        brightness.append(float(row[int(column_header.index("brightness"))]))


data = {
    'type' : 'scattergeo',
    'lat' : lats,
    'lon' : lons,
    'marker' : {
        'color' : brightness,
        'size' : [0.1*bright for bright in brightness],
        'colorscale' : "Viridis",
        'reversescale' : True,
        'colorbar' : {'title' : "Brightness"}
    }
}

my_layout = Layout(title = "Fires Over One Day")
fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig,filename='global_fires.html')