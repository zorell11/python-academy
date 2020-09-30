import csv
import random

file = open('names.csv', 'r+')
reader = csv.reader(file)

print('The whole table:')
for row in reader:
    print(row)
file.seek(0)
column = random.randrange(len(list(reader)[0]))
file.seek(0)
print('{} column from the table:'.format(column))
for i in reader:
    print(i[1])

print('Shown city columns:')
file.seek(0)
print(type(reader))
for column in list(reader)[1:]:
    print(column[4])
