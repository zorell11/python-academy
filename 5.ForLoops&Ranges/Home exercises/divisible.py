START = int(input('START: '))
STOP = int(input('STOP: '))
DIVISOR = int(input('DIVISOR: '))

numbers = []

if DIVISOR:

    for i in range(START, STOP+1):
        if i%DIVISOR == 0:
            numbers.append(i)
    print('Numbers in range(' + str(START) + ',' + str(STOP+1) + ') divisible by ' + str(DIVISOR) + ':')
    print(numbers)

else:
    print('Cannot divide by zero')
