import csv
from datetime import datetime
import matplotlib.pyplot as plt

first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
print(first_date)

filename = r"C:\Users\ammar\programs\2025-Python-Practice\PythonCrashCourse\chapter_16\sitka_weather_07-2021_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates = []
    highs = []
    for row in reader:
        high = int(row[4])
        highs.append(high)
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
# Format plot.
plt.title("Daily high temperatures, July 2021", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()