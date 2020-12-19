import csv

prvni = ['Surname', 'Name', 'Full Name', 'Age', 'City', 'Job', 'Gender']
obsah = [['Smith', 'John', 'Smith, John', '32', 'London', 'Programmer', ''],
['Doe', 'Joe', 'Doe, Joe', '34', 'Liverpool', '', 'Male'],
['Murphy', 'Ann', 'Murphy, Ann', '29', 'London', 'Admin', 'Female'],
['Cook', 'Floyd', 'Cook, Floyd', '28', '', 'Tester', 'Male'],
['Glenn', 'Taylor', 'Glenn, Taylor', '35', 'Birmingham', 'Manager', 'Female'],
['Mills', 'Amanda', 'Mills, Amanda', '41', 'Leicester', 'Quality Assurance', 'Female']]

f = open('write_list.csv','w')
f_write = csv.writer(f)

f_write.writerow(prvni)
f_write.writerows(obsah)

f.close()
