myNewDict = {'m': 12345, 'n': 32145, 'o': 54321, 'p': 23232, 'q': 43210, 'r': 13579}
print(myNewDict)

maximalValueofKey = max(list(myNewDict.keys()))
print('Key with maximal value of key is: ', maximalValueofKey)

if max(list(myNewDict.values())) > myNewDict[maximalValueofKey]:
    del myNewDict[maximalValueofKey]

print(myNewDict)
