def solution(A):
    # write your code in Python 3.6
    sum_A = len(A)*(len(A)+1) // 2
    sum_A1 = sum(A)

    if len(A) != len(dict.fromkeys(A)):
        return 0

    if sum_A == sum_A1:
        return 1
    else:
        return 0

print(solution([4,1,3,2]))
print(solution([4,1,2]))
print(solution([1,4,1]))
