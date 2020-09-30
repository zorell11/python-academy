import csv

f = open('salaries.csv')
reader = list(csv.reader(f))
f.close()
del reader[0]
dct = dict()

for row in reader:
    dct.update({row[0]: int(row[1])})

salaries = dct.values()

header = ['TYPE', 'SALARY']
max_sal = ['Maximum salary', max(salaries)]
min_sal = ['Minimum salary', min(salaries)]
avg_sal = ['Average salary', sum(salaries) / len(salaries)]
to_write = [header, max_sal, min_sal, avg_sal]

f = open('salary_statistics_engeto.csv', 'w')
writer = csv.writer(f)
writer.writerows(to_write)
f.close()
