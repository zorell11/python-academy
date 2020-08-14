names = ['Michal', 'Pepa', 'Honza', 'Pavel', 'Lukas', 'Matej', 'Iva', 'Klara', 'Jana', 'Honza', 'Vasek','Milan', 'Michal']



for i in range(len(names)):
    for j in range(len(names)-1-i):
        if names[j] > names[j+1]:
            names[j],names[j+1] = names[j+1], names[j]

print(names)
