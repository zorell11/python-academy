def solution(A):
    # write your code in Python 3.6
    sum_A = sum(A)
    sum_A1 = (len(A)+1)*(len(A)+2)//2
    return sum_A1 - sum_A

print(solution([2, 3, 1, 5]))
