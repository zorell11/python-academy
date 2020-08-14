def solution(N, A):
    # write your code in Python 3.6
    output = N  * [0]
    for i in range(len(A)):
        if A[i] == N+1:
            output =[max(output)] * len(output)
        elif  0 < A[i] < (N+1):
            output[A[i]-1] += 1


    return output







lst = [3,4,4,6,1,4,4]
print(solution(2100, lst))
print(solution(5, [1]))



def solution1(N, A):
    result = [0]*N    # The list to be returned
    max_counter = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter
    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > result[command-1]:
                # lazy write
                result[command-1] = max_counter
            result[command-1] += 1
            if current_max < result[command-1]:
                current_max = result[command-1]
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max
    for index in range(0,N):
        if result[index] < max_counter:
            # This element has never been used/updated after previous
            #     max_counter command
            result[index] = max_counter
    return result

print(solution1(5, lst))
print(solution1(5, [1]))
