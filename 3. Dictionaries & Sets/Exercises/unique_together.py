## Opět budeme pracovat s 2 stringy:
#str1 = 'New York'
#str2 = 'Yorkshire'
#Napište krátky skript (např. unique_together.py), který vytiskne znaky, které jsou v str1 nebo str2,
#ale ne v obou:
#Příklad běžícího skriptu:
#~/PythonBeginner/Lesson2 $ python unique_together.py
#[' ', 'w', 's', 'i', 'h', 'N']

str1 = 'New York'
str2 = 'Yorkshire'

unique = set(str1) ^ set(str2)
print(list(unique))
