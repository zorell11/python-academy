# Opět budeme pracovat s 2 stringy:
#str1 = 'New York'
#str2 = 'Yorkshire'
#Napište krátky skript (např. unique.py), který vytiskne:
#list se znaky, které jsou jedinečné pro str1
#a list se znaky, které jsou jedinečné pro str2
#Příklad běžícího skriptu:
#~/PythonBeginner/Lesson2 $ python unique.py
#Unique to str1: [' ', 'w', 'N']
#Unique to str2: ['h', 's', 'i']

str1 = 'New York'
str2 = 'Yorkshire'

unique_to_str1 = set(str1) - set(str2)
unique_to_str2 = set(str2) - set(str1)
print('Unique to str1:', list(unique_to_str1))
print('Unique to str2:', list(unique_to_str2))
