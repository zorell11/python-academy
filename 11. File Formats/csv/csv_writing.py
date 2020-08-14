import csv

new_employee=['Mills','Amanda','Mills, Amanda', 41,'Leicester','Quality Assurance','Female']

with open('example1.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(new_employee)


employees = [['Harris','Roy','Harris, Roy',22,'London','Junior Programmer','Male'],
         ['Chesterfield','Mark','Chesterfield, Mark',46,'Liverpool','SCRUM Master','Male'],
         ['Hammet','Sandra','Hammet, Sandra',48,'Liverpool','Designer','Female']]

with open('example1.csv','a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(employees)

employees = [{'Job': 'Programmer', 'Age': 35, 'Full Name': 'Murphy, John', 'City': 'London', 'Surname': 'Murphy', 'Gender': 'Male', 'Name': 'John'},
{'Job': 'Supervisor', 'Age': 26, 'Full Name': 'Higgins, Mary', 'City': 'Leicester', 'Surname': 'Higgins', 'Gender': 'Female', 'Name': 'Mary'}]
