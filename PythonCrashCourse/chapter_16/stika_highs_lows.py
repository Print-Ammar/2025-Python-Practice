import csv
from datetime import datetime
import matplotlib.pyplot as plt
first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
filename = r"2025-Python-Practice/PythonCrashCourse/chapter_16/sitka_weather_2021_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    highs = []
    lows = []

    for index, column_header in enumerate(header_row):
        
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[4])
            low = int(row[5])
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
fig, ax = plt.subplots()
ax.plot(dates, highs, c='blue', alpha =0.5)
ax.plot(dates,lows,c='red', alpha = 0.5)
plt.fill_between(dates,highs,lows, facecolor ='blue', alpha = 0.1)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.title("Daily high and low temperatures - 2021", fontsize=24)

plt.show()