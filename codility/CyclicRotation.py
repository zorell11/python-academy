def solution(A, K):
    # write your code in Python 3.6
    new = len(A) * ['None']
    for i in range(len(A)):
        offset = (i+K)%len(A)
        new[offset] = A[i]

    return new





print(solution([3, 8, 9, 7, 6], 1))
