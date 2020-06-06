import csv
filename = 'minsk_06_2019.csv'
with open(filename) as f:
    reader = csv.reader(f)
    name = next(reader)

    bigs = []
    for n in reader:
        big = (n[1])
        bigs.append(big)

    print(bigs)