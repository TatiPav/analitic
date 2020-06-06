import csv

from matplotlib import pyplot as plt

filename = 'minsk_06_2019.csv'
with open(filename) as f:
    reader = csv.reader(f)
    name = next(reader)

    bigs = []
    for n in reader:
        big = (n[1])
        bigs.append(big)

    figure = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(bigs, c = 'red')

    plt.title('максимальная температура', fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()