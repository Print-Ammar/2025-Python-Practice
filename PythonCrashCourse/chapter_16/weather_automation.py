import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path(r"2025-Python-Practice\PythonCrashCourse\chapter_16\death_valley_2021_simple.csv")

with open(file_path) as f:
    reader = csv.reader(f)
    first_row = next(reader)

    heighs, lows, dates = [], [], []
    name = ''

    for row in reader:
        try:
            high = int(row[first_row.index('TMAX')])
            low = int(row[first_row.index("TMIN")])
            date = datetime.strptime(row[first_row.index("DATE")], '%Y-%m-%d')
            name = row[first_row.index("NAME")]
        except ValueError:
            print("Missing Value")
        else:
            heighs.append(high)
            lows.append(low)
            dates.append(date)
    
fig, ax = plt.subplots()
ax.plot(dates,heighs, color = 'red', alpha = 0.5)
ax.plot(dates,lows, color = 'blue', alpha = 0.5)
plt.fill_between(dates, heighs, lows, facecolor = 'blue', alpha = 0.1)
plt.xlabel("dates")
plt.ylabel("tempatures")
plt.title(f"Tempature highs and lows in {name}")
plt.show()