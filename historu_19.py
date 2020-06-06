import csv
filename = 'minsk_06_2019.csv'
with open(filename) as f:
    reader = csv.reader(f)
    name = next(reader)

    for index, column_name in enumerate(name):
        print(index,column_name)