import csv
from datetime import datetime
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path(r"2025-Python-Practice\PythonCrashCourse\chapter_16\death_valley_2021_simple.csv")

with open(file_path) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [], [], []

    for index, column_header in enumerate(header_row):

        for row in reader:
            try:
                high = int(row[3])
                low = int(row[4])
                date = datetime.strptime(row[2], '%Y-%m-%d')
            except ValueError:
                print("Missing data")
            else:
                highs.append(high)
                lows.append(low)
                dates.append(date)

fig, ax = plt.subplots()
ax.plot(dates,highs, alpha = 0.5, c = 'red')
ax.plot(dates,lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
plt.title("Highs And Lows For Death Valley 2021")
plt.xlabel("Tempature")
plt.ylabel("Dates")
plt.show()