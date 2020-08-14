# We continue to work with the list, with the code from the previous task. Write a script, that will:

# -remove the 'Bruno' element from the candidates list,
# -print the content of candidates introducing it with a string: 'Bruno removed from candidates:',
# -repeat the name 'Agnes' 3 times inside the candidates list,
# -print the content of the candidates list introducing it with a string: 'Repetition of Agnes in the candidate list:',
# -join the list employees with the listcandidates into a new list which retains the name `employees',
# -print the content of the new `employees' list introducing it with a string: 'Joined candidates and employees:',
# -print the name on index 2 introducing it with a string: 'On index 2 is:',
# -print the name on the last index introducing it with a string: 'On the <last_index> index is:'
# -<last_index> * should be replaced with the latest index number from our newly joined employees list.
# -An example of a running script that includes a previous task:

#Candidates at the beginning: []
#Employees at the beginning: ['Francis', 'Ann', 'Jacob', 'Claire']
#New names added to the candidates: ['Bruno', 'Agnes']
#New employees names added: ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']
#Bruno removed from the candidates: ['Agnes']
#Repetition of Agnes in the candidate list: ['Agnes', 'Agnes', 'Agnes']
#Joined candidates and employees: ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire', 'Agnes', 'Agnes', 'Agnes']
#On index 2 is: Ann
#On index 7 is: Agnes


# Results from previous task
candidates = ['Bruno', 'Agnes']
employees = ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']

# Delete names from candidates
candidates.remove('Bruno')
# Print remaining candidates
print("Bruno removed from the candidates:", candidates)

# Repeat element
candidates = 3 * candidates

# Print repeating element in list candidates
print("Repetition of Agnes in the candidate list:", candidates)

# Join lists
employees += candidates

# Print joined lists
print("Joined candidates and employees:", employees)

# Index 2a
print("On index 2 is:", employees[2])

# Find out last index and assign it to variable
last_index = len(employees)-1

# Last index
print("On index", last_index, "is:", employees[last_index])
