def solution(X, A):
    new_A = list(dict.fromkeys(A))
    sum_A = len(new_A) * (len(new_A)+1)/2

    if sum_A == sum(new_A) and X in new_A:
        return A.index(new_A[-1])

    else:
        return -1


lst = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution(5, lst))
