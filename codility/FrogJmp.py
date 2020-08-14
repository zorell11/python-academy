def solution(X, Y, D):
    # write your code in Python 3.6
    #pass

    if X == Y:
        return 0

    elif X < Y:
        distance = Y - X
        #jumps=
        if distance%D == 0:
            return int(distance/D)
        else:
            jump = distance//D +1
            return int(jump)


print(solution(10, 85, 30))
print(solution(1, 5, 2))
