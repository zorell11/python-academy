def solution(A):
    #pass
    if list(dict.fromkeys(A)) == 1:
        return 0

    if A[0] == 0:
        first, other = 0, 1
    else:
        first, other = 1, 0

    passing_cars = 0
    for i in range(len(A)):
        if A[i] == first:
            passing_cars += A[i:].count(other)

    return passing_cars





print(solution([0, 1, 0, 1,1]))
print(solution([1, 0, 1, 0,0]))

print(solution([1, 0]))
