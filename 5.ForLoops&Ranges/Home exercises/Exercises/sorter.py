# Let's create a program that will sort any list of strings in alphabetical order. It is not permitted to use methods and functions as sort() or sorted().
#To test your program, use the following list of names:

# solution:
#['Honza', 'Honza', 'Iva', 'Jana', 'Klara', 'Lukas', 'Matej', 'Michal', 'Michal', 'Milan', 'Pavel', 'Pepa', 'Vasek']
names = [
    'Michal', 'Pepa', 'Honza',
    'Pavel', 'Lukas', 'Matej',
    'Iva', 'Klara', 'Jana',
    'Honza', 'Vasek', 'Milan', 'Michal'
]

#names = [
#    7, 10, 1,
#    9, 5, 6,
#    2, 4, 3,
#    1, 11, 8, 7
#]
print(names)
sorted_list = []
sorted_list.append(names.pop(0))
counter = 1
for i in names:
    for j, name in enumerate(sorted_list):
        if name > i:
            sorted_list.insert(j, i)
            break;
    else:
        sorted_list.append(i)


print(sorted_list)
