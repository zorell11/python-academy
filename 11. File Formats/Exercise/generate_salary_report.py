import csv

def read_content(file):
    file = open(file, 'r')
    reader = csv.reader(file)
    salaries = []
    for i in list(reader)[1:]:
        salaries.append(int(i[1]))
    file.close()
    return salaries

def min_salary(salary):
    minimum = min(salary)
    salaries_stat.append(['Minimum salary', minimum])

def max_salary(salary):
    maximum = max(salary)
    salaries_stat.append(['Maximum salary', maximum])

def avg_salsary(salary):
    avg = sum(salary)/len(salary)
    salaries_stat.append(['Average salary', avg])

def save_to_file(stat):
    file = open('salaries_statistics.csv', 'w+')
    writer = csv.writer(file)
    writer.writerows(stat)
    file.close()


if __name__ == "__main__":

    salaries_stat = [['Type', 'Salary']]
    file_name = 'salaries.csv'
    salary = read_content(file_name)
    min_salary(salary)
    max_salary(salary)
    avg_salsary(salary)
    save_to_file(salaries_stat)
