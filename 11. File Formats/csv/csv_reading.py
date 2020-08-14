import csv

with open('example1.csv', newline='') as file:
     reader = csv.reader(file)
     for row in reader:
         print(row)

with open('example.csv', newline='') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i != 0:
            print(row[3])

file = open('example.csv', newline='')
reader = csv.reader(file)
for i in reader:
    print(i)
file.close()


with open('example.csv', newline='') as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i)
