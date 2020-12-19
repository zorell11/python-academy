import json

f = open('employees.json')
data = json.load(f)
f.close()

print(data)
print(type(data))
