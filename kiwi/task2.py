def solution(A):
    # write your code in Python 3.6
    #pass
    turbulences = []
    if len(A) == 1:
        return 1
    A.append(A[-1])
    while A:
        if len(A) == 1:
            turbulence.append(1)
            return max(turbulence)

        if A[0] == A[1]:
            A.pop(0)
#            print(A)

        if A[0] > A[1]:
            index = 0
        elif A[0] < A[1]:
            index = 1

        tur_counter = 1
        actual = A.pop(0)
        while A:
            previous, actual = actual, A.pop(0)
#            print(A, 'turbulence:',tur_counter, 'previous:', previous, 'actual:', actual, "index:", index)
            #input()
            if (index%2 == 0 and previous > actual) or (index%2 == 1 and previous < actual):
                tur_counter +=1
                index +=1


            else:
                turbulences.append(tur_counter)
#                print('turbulences:', turbulences)
                if A:
                    A.insert(0,previous)
                    A.insert(1,actual)
                break
    print(turbulences)
    turbulence = max(turbulences)
    return turbulence


height = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print("Turbulence for", height, "is:", solution(height))
print("Turbulence for 100 is:", solution([100]))
print("Turbulence for [4, 8,12, 16] is:", solution([4, 8,12, 16]))

N = []
for i in range(100000):
    if i%2 == 0:
        N.append(50)
    else:
        N.append(100)
print("Turbulence for N is:", solution(N))
