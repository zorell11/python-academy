import csv

f = open('names.csv')
f_reader = csv.reader(f)

for row in f_reader:
    print(row[0])

f.close()
