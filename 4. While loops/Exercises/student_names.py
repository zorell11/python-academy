# We have a class of students. All the student names are stored in the list students.
# Our task is to extract an overview of what unique names and surnames do we have in the class.

students = ['Adam, Baker','Chelsea, Archer',
            'Marcus, Archer','Oliver, Cook',
            'Alex, Dyer', 'Sandra, Turner',
            'Ann, Fisher', 'Glenn, Hawkins',
            'Samuel, Baker','Clara, Slater',
            'Tyler, Hunt', 'Alex, Smith',
            'Clara, Woodman','Abraham, Mason',
            'Marcus, Sawyer','Alex, Glover',
            'Glenn, Cook','Clara, Fisher',
            'Alfred, Dyer', 'Curt, Head',
            'Oliver, Slater','Alex, Mason',
            'Tyler, Fisher','Ann, Parker',
            'Samuel, Hawkins', 'Ann, Woodman',
            'Sandra, Slater', 'Curt, Dyer']

print('Extracting ...')
print('Unique names:')

names = []
surnames = []
for i in students:
    a, b = i.split(', ')
    names.append(a)
    surnames.append(b)

print(set(names))
print(set(surnames))
