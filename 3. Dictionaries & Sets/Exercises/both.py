#Opět budeme pracovat s 2 stringy:
#str1 = 'New York'
#str2 = 'Yorkshire'
#Napište krátky skript (např. both.py), který vytiskne jedinečné znaky, které jsou v str1 nebo str2:
#Příklad běžícího skriptu:
#~/PythonBeginner/Lesson2 $ python both.py
#[' ', 'k', 'e', 'r', 'w', 's', 'i', 'o', 'h', 'Y', 'N']



str1 = 'New York'
str2 = 'Yorkshire'
both = set(str1) | set(str2)
print(list(both))
