#read csv. file:
csv.reader()
csv.DictReader()

csv.writer()
-writerow()
-writerows()

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

# write to csv file

with open('example1.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(new_employee)

with open('example.csv','a',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(employees)
