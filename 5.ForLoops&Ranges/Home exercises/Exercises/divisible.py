# Write a program that will work with three inputs:
# -integer start
# -integer stop
# -integer divisor
# All of them should be provided by the user.
# The program should:
#generate a collection of integers in range between start (including) and stop (included in the
# collection) print a list of only those numbers in range start - stop, that are divisible by divisor
# If divisor is 0, the program should print to the terminal a string 'Cannot divide by zero' instead
# of the list of divisible numbers

# Example of running the program:
#$ python3 divisible.py
#START: 3
#STOP: 9
#DIVISOR: 3
#Numbers in range(3,10) divisible by 3:
#[3,6,9]
#$ python3 divisible.py
#START: 3
#STOP: 9
#DIVISOR: 0
#Cannot divide by zero

start = int(input('START: '))
stop = int(input('STOP: '))
divisor = int(input('DIVISOR: '))
output = []

if divisor == 0:
    print('Cannot divide by zero')
else:
    for i in range(start, stop + 1):
        if (i % divisor) == 0:
            output.append(i)
    print('Numbers in range(' + str(start) + ',' + str(stop) + ') divisible by ' + str(divisor) + ':')
    print(output)
