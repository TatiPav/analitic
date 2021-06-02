import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/d_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Чтение дат и максимальных и минимальных температур
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Отсутствуют данные за {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# print(highs)

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='orange', alpha=0.5)
ax.plot(dates, lows, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = 'Метеоданные min и max за 2018 г'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Температура (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
