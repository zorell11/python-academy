
for i in range(101):
    #if i%3 == 0 and i%5 == 0:
    #if i%15 == 0:
    if not i%15:
        print('FizzBuzz')
    elif i%5 == 0:
        print('Buzz')
    elif i%3 == 0:
        print('Fizz')
    else:
        print(i)
