A = [9, 4, 2, 10, 7, 8, 8, 1, 9]
turbulences = []
tur_counter = 0
index = 0
previous = A.pop(0)
actual = A.pop(0)
while A:

    print(A, 'turbulence:',tur_counter, 'previous:', previous, 'actual:', actual, "index:", index)
    input()
    if (index%2 == 0 and previous > actual) or (index%2 == 1 and previous < actual):
        tur_counter +=1
        index +=1
        previous, actual = actual, A.pop(0)
        #input('Zadaj:')
        #print(A, tur_counter, previous, actual)
        input()
    else:
        turbulences.append(tur_counter)
        #A.pop(0)
        #input('Zadaj:')
        tur_counter = 0
        index = 0

print(A)
