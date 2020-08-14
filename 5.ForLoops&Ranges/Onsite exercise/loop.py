names = ['Jakub', 'Jana', 'Petr', 'Klara']

for i in names:
    print(i)

length = 0
print("Names beginning with the letter: ", end=" ")
for i in names:        
    if i.startswith('J'):
        length += len(i)
        print(i, end=' ')
print("Total number of letters that these names contain", length)
