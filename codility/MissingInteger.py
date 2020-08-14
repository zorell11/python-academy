def solution(A):
    # write your code in Python 3.6
    A = sorted(list(dict.fromkeys(A)))
    B = A.copy()
    for i in A:
        if i < 1:
            B.remove(i)

    if not B:
        return 1

    elif len(B) == B[-1]:
        for i in range(len(B), 1000001):
            if i not in B:
                return i


    else:
        for i in range(1, 1000001):
            if i not in B:
                return i



solution([1, 3, 6, 4, 1, 2])
solution([1, 2, 3])
solution([-1, -3])
solution([-1, 6, -3, 8, -9])
solution([-1, -3, -10, -3, -4])
