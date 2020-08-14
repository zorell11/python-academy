import csv

file = open('example.csv', newline='')
reader = csv.reader(file)
for i in reader:
    print(i)

data = []
file.seek(0)
data = list(reader)
print(data)

file.seek(0)
data1 = dict(reader)
print(data1)

file.close()
