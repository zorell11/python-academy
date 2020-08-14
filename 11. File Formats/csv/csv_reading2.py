import csv

with open('example.csv', newline='') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i != 0:
            if row[4] == 'London':
                print(row)
