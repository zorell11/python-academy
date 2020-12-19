# dict -> JSON -> file
import json

employee = {'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London', 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}

to_json = json.dumps(employee)
to_json_indent = json.dumps(employee, indent = 4, sort_keys = True)

print(to_json)
print(to_json_indent)

f = open('file.json', 'w')
f.write(to_json)
f.close()
