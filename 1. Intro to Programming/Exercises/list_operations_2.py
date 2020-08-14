#Again, use results from previous task. Add following:

# -print names on index from 2 to 5 introducing it with a string: 'In interval from 2 to 5 is:',
# -print every third element of the employees list introducing it with a string: 'Every third member is:',
# -print which index contains the string 'Jacob' in the `employees' list introducing it with a string: ' Jacob is on the index: ',
# -print the number of times the name 'Agnes' appears in the list `employees per string: 'Number of Agnes names in the sheet:'.

#Example of running script including previous tasks:
#Candidates at the beginning: []
#Employees at the beginning: ['Francis', 'Ann', 'Jacob', 'Claire']
#New names added to the candidates: ['Bruno', 'Agnes']
#New employees names added: ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']
#Bruno removed from the candidates: ['Agnes']
#Repetition of Agnes in candidates: ['Agnes', 'Agnes', 'Agnes']
#Joined candidates and employees: ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']
#On index 2 is: Ann
#On the 7 index is: Agnes
#From index 2 to 5 there are: ['Ann', 'Jacob', 'Claire', 'Agnes']
#Every third member is: ['Francis', 'Jacob', 'Agnes']
#Jacob is on the index: 3
#Number of name Agnes in sheet: 3


# Results from the previous task
candidates = ['Agnes', 'Agnes', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']


# Interval 2-5
print( 'In interval from 2 to 5 is:',employees[2:6])

# Each 3rd
print("Every third member is:", employees[::3])

# Save index
index = employees.index('Jacob')

# Jacob index
print("Jacob is on the index:", index)

# Number of name Agnes
print("Number of Agnes names in the sheet:", employees.count('Agnes'))
