
database = {'id123': {},'id124': {},'id125': {},'id126': {}}

FirstDict = {'name': 'Thomas', 'age': 45, 'Country': 'Czechia', 'City': 'Brno'}
SecondDict = {'name': 'Daniel', 'age': 34, 'Country': 'Czechia', 'City': 'Prague'}
ThirdDict = {'name': 'Eva', 'age': 43, 'Country': 'Czechia', 'City': 'Olomouc'}

database.update(id123 = FirstDict)
database.update(id124 = SecondDict)
database.update(id125 = ThirdDict)

print(database)
