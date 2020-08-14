# V následujícíh cvičeních budeme pracovat s těmito dvěma stringy:
#str1 = 'New York'
#str2 = 'Yorkshire'
#Napište krátký skript (můžeme ho pojmenovat common.py), který vytiskne všechny znaky, které mají tyto 2 stringy společné.
#Příklad běžícího programu:
#~/PythonBeginner/Lesson2 $ python common.py
#['Y', 'e', 'k', 'r', 'o']

str1 = 'New York'
str2 = 'Yorkshire'

common = set(str1) & set(str2)
print(list(common))
