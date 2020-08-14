json.dumps()    #from python to JSON
json.loads()    #from JSON to python

json.dump()     #wrtite to file
json.dump(employee, file, indent=4)
json.loads()    #read from file
json.load(file)


>>> employee = {'Active': False, 'Job': None, 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London', 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}
>>>
>>> json.dumps(employee)
'{"Active": false, "Job": null, "Age": 38, "Full Name": "Galagher, Fred", "City": "London", "Surname": "Galagher", "Gender": "Male", "Name": "Fred"}'


employee = {'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London', 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}
>>> print(json.dumps(employee, indent=4, sort_keys=True))
{
    "Age": 38,
    "City": "London",
    "Full Name": "Galagher, Fred",
    "Gender": "Male",
    "Job": "Programmer",
    "Name": "Fred",
    "Surname": "Galagher"
}
