import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'basa.csv'
with open(filename) as f:
    reader = csv.reader(f)
    name = next(reader)

    dates, bigs = [], []
    for n in reader:
        andate = datetime.strptime(n[1], '%Y-%m-%d')
        dates.append(andate)

        big = (n[2])
        bigs.append(big)

    figure = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, bigs, c='green')

    plt.title('Максимальная температура', fontsize=24)
    plt.xlabel('', fontsize=16)

    figure.autofmt_xdate()
    plt.ylabel('Temperature', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()