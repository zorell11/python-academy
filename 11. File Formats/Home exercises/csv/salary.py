import csv

with open('salaries.csv', newline='') as f:
    reader = csv.reader(f)
    salary = []
    for counter, row in enumerate(reader):
        #if counter != 0:
            try:
                salary.append(int(row[1]))
            except:
                pass
#    print(salary)
#    print(max(salary), min(salary), sum(salary)/len(salary))

header = ['Type', 'Salary']
min = ['Minimum salary', min(salary)]
max = ['Maximum salary', max(salary)]
avg = ['Average salary', sum(salary)/len(salary)]
info = [header, max, min, avg]

with open('salary_info.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(info)
