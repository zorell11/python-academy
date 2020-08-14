import json

file = open("employees.json")
print(json.load(file))
file.close()

with open("employees.json") as f:
    print(json.load(f))


emp ={'Name': 'Fred', 'Job': 'Programmer', 'Full Name': 'Galagher, Fred', 'Surname': 'Galagher', 'City': 'London', 'Gender': 'Male', 'Age': 38}

with open('employees1.json', 'w') as f:
    json.dump(emp, f, indent=10, sort_keys=True)
