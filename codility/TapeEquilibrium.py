def solution(N):
    minimum = float('inf')
    for i in range(1,len(N)):
        minimum = min(abs(sum(N[:i]) - sum(N[i:])), minimum)
    return minimum


def solution1(A):
    #total, minimum, left = sum(A), max(A), 0
    total, minimum, left = sum(A), float('inf'), 0
    for a in A[:-1]:
        left += a
        minimum = min(abs(total - left - left), minimum)
    return minimum

print(solution1([3, 1, 2, 4, 3]))




print(solution([3, 1, 2, 4, 3]))
