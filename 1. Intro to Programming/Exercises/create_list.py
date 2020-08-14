#Create script, which will:

# -assign an empty list to variable candidates,
# -print the content of variable candidates introducing it with a string 'Candidates at the beginning:',
# -assign a list to variable employees, containing strigns: 'Francis', 'Ann', 'Jacob', 'Claire',
# -print employees content introducing it with a string 'Employees at the beginning:',
# -add the names 'Bruno' and 'Agnes' to the empty 'candidates' list,
# -print the content of candidates introducing it with a string 'New names added to candidates:',
# -insert the name 'Bruno' stored in the candidate list into the` employees' list at index 1,
# -print the content of the employees variable introducing it with a string: 'New names added to employees':

# Example of running script:
#Candidates at the beginning: []
#Employees at the beginning: ['Francis', 'Ann', 'Jacob', 'Claire']
#New names added to candidates: ['Bruno', 'Agnes']
#New names added to employees: ['Francis', 'Bruno', 'Ann', 'Jacob', 'Claire']

# Create Candidate
candidates = []
# Print candidates at the beginning
print("Candidates at the beginning:", candidates)
# Create employees
employees = ['Francis', 'Ann', 'Jacob', 'Claire']
# Print employees at the beginning
print("Employees at the beginning:", employees)
# Add new candidates
new_names = ['Bruno', 'Agnes' ]
candidates += new_names
# Print new candidates
print('New names added to candidates: ', new_names)
# Insert name
employees.insert(1, candidates[0])
# Print the employees list after entering a new name
print("New names added to employees: ", employees)
