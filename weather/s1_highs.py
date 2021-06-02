import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/s_weather_07-18.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Чтение дат и максимальных температур
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# print(highs)

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='orange')

plt.title('Метеоданные за июль 2018 г', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Температура (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
