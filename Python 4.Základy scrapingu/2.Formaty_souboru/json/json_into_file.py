import json
employee = {
    "Name": "Fred",
    "Job": "Programmer",
    "Full Name": "Galagher, Fred",
}

f = open('employees.json', 'w')
json.dump(employee, f, indent = 4)
f.close()
