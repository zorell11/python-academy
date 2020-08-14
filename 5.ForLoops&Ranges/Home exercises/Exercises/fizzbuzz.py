# Write a program that prints the integers from 1 to 100 (inclusive).
#But:
# -for multiples of three, print Fizz (instead of the number)
# -for multiples of five, print Buzz (instead of the number)
# -for multiples of both three and five, print FizzBuzz (instead of the number)


for number in range(101):
    if number % 15 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)
