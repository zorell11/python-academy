from time import sleep
#import time

number = int(input('How many seconds to you need?'))

while number:
    sleep(1)
    print(number)
    number -= 1
