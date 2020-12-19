# file -> JSON -> dict
import json

f = open('file.json', 'r')
count = f.read()
print(count)
print(type(count))

data = json.loads(count)

print(data)
print(type(data))


f1 = open('employees.json')
count1 = f1.read()
print(count1)
print(type(count1))
