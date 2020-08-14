#!/usr/bin/env python3

for i in range(1,100):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)



for i in range(1,100):
    if not i%15:
        print("FizzBuzz")
    elif not i%3:
        print("Fizz")
    elif not i%5:
        print("Buzz")
    else:
        print(i)
