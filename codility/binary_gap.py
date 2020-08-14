def solution(N):
    # write your code in Python 3.6
    #pass

    binary = bin(N)[2:]
    print(binary)
    gaps = []

    first = binary.find('1')
    last =  binary.rfind('1')

    if first == last:
        return 0
    counter = 0
    for i in binary[first+1:last+1]:
        i = int(i)
        if i == 1:
            gaps.append(counter)
            counter = 0
        else:
            counter += 1
    return max(gaps)

print('0:', solution(0))
print('2:', solution(1))


print('2,147,483,647:', solution(2147483647))


print('1048577:', solution(1048577))

print('1025:', solution(1025))

print('32:', solution(32))
print('1041:', solution(1041))
print('9:', solution(9))
print('529:', solution(529))
