import csv

f = open('names.csv')

f_reader = csv.DictReader(f)

for i in f_reader:
    print(i)
    if i['Name'] == 'Zoltan':
        print(i['Surname'])
        print(i)

f.close()
