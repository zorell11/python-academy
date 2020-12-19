import csv

dict1 = {'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London', 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}
header = ['Surname', 'Name', 'Full Name', 'Age', 'City', 'Job', 'Gender']

f = open('write_dict.csv', 'w')

f_writer = csv.DictWriter(f, header)

f_writer.writeheader()
f_writer.writerow(dict1)

f.close()
