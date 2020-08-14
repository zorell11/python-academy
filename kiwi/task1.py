def solution(A):
    ans = 0
    for i in range(1, len(A)):
        print(A[i])
        if A[i] < ans:
            ans = A[i]
    return ans


print(solution([-1, 1, -2, 2]))
print()
print(solution([]))
