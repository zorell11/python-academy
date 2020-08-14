# Goal of this task is to put different dictionaries into our main dictionary.
#Here is our main dictionary:
#database = {'id123': {},'id124': {},'id125': {}}
#And here are the others:
#first_dict = {'name': 'Thomas', 'age': 45, 'Country': 'Czechia', 'City': 'Brno'}
#second_dict = {'name': 'Daniel', 'age': 34, 'Country': 'Czechia', 'City': 'Prague'}
#third_dict = {'name': 'Eva', 'age': 43, 'Country': 'Czechia', 'City': 'Olomouc'}
#Your solution should print the resulting dictionary (we have made the dictionary a bit nicer for you here):
#{
#    'id123': {
#        'name': 'Thomas', 'age': 45, 'Country': 'Czechia', 'City': 'Brno'
#    },
#   'id124': {
#        'name': 'Daniel', 'age': 34, 'Country': 'Czechia', 'City': 'Prague'
#    },
#    'id125': {
#        'name': 'Eva', 'age': 43, 'Country': 'Czechia', 'City': 'Olomouc'
#     }
#}

database = {'id123': {},'id124': {},'id125': {}}
first_dict = {'name': 'Thomas', 'age': 45, 'Country': 'Czechia', 'City': 'Brno'}
second_dict = {'name': 'Daniel', 'age': 34, 'Country': 'Czechia', 'City': 'Prague'}
third_dict = {'name': 'Eva', 'age': 43, 'Country': 'Czechia', 'City': 'Olomouc'}

database['id123'] = first_dict
database['id124'] = second_dict
database['id125'] = third_dict

print(database)
