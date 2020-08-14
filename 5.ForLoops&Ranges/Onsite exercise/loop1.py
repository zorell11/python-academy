names = ['Jakub', 'Jana', 'Petr', 'Klara']
letters = 0
for i in names:
    print(i)
    letters += len(i)
print('Total number of letters are: ', letters)
print(30 * '#')

for i in names:
    if i[0] == 'J':
        print(i)
