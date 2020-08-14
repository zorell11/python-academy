candidates = []
print("Candidates at the beginning:", candidates)
employes = ['Frank', 'Amy', 'John', 'Kate']
print("Employees at the beginning:", employes)

candidates += ['Bob', 'Ann']
print("Added new names to candidates:", candidates)

employes.insert(1, candidates[0])
print("Added new names to employees:", employes)

candidates.remove('Bob')
print("Removed Bob from candidates:", candidates)

candidates = 3 * candidates
print("Repeated name Ann in candidates:", candidates)

employes += candidates
print("Merged candidates with employees:", employes)

print("At index 2 we have:", employes[2])
print("At index 7 we have:", employes[len(employes) - 1])

print("At indices 2 to 5 we have:", employes[2:6])
print("Every third member: " + str(employes[::3]))


print("John is at index:", employes.index('John'))

print("The number of occurences of Ann:", employes.count('Ann'))
