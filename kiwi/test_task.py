def solution(A):
    # write your code in Python 3.6
    A = list(dict.fromkeys(A))
    A.sort()

    B = A.copy()
    for i in A:
        if i<=0:
            B.remove(i)
        else:
            continue
    print(B)
    if not B:
        return 1

    elif len(B) == B[-1]:
        for i in range(len(B), 1000001):
            if i not in A:
                return i

    else:
        for i in range(1,1000001):
            if i not in A:
                return i

                
print(solution([1,2,3,4,-1,-2,]))
print(10 * '#')
print(solution([-1,-3]))
print(10 * '#')
print(solution([2]))
print(10 * '#')
a = list(range(1,40001))
#print(a)
print(solution(a))
b = list(range(1,100001))
#print(a)
print(solution(b))
c= list(range(101)) + list(range(102,201))
print(solution(c))
