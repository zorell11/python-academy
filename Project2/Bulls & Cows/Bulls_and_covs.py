import random
import time


#############################################################################################
# read the number and test if it is number and have 4 digits
def guess(guesses):
    test = True
    while test:
        number = str(input(">> "))
        if not number.isnumeric() or len(number) != 4:
            print('Wrong input. Guess needs to be a number 0000-9999.')
        else:
            test = False
        guesses += 1
    return number, guesses

#############################################################################################
# counting the bulls and cows
def bulls_cows(a,b):
    bulls = 0
    cows = 0
    for i in range(4):
        if b[i] == a[i]:
            bulls +=1
        elif b[i] in a:
            cows += 1
    return bulls, cows

#############################################################################################
# time to guess the number - hours, minutes and seconds
def guess_time(start, end):
    time = int(round(end - start, 0))
    hours, remnant = divmod(time, 360)
    mins, sec = divmod(remnant, 60)
    return hours, mins, sec

#############################################################################################
# write stats to file - number of guesses and time
def store_stats(guess_number, time):
    file = open('stats.txt', 'a')
    file.write((str(guess_number) + ' ' + time + '\n'))
    file.close()

#############################################################################################
# message to user based on number of guesses
def message(guess):
    if guess <= 10:
        return 'amazing'
    elif 10 < guess <= 30:
        return 'average'
    elif 30 < guess <= 60:
        return 'not so good'
    elif guess > 60:
        return 'awful :D '


#############################################################################################
# MAIN PROGRAM
#############################################################################################

print('''
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number''')

# generate secret number
secret_num = random.sample(range(0, 9), 4)
print('secret number is: {}'.format(secret_num))

test = True
guesses = 0
start_time = time.time()
while test:
    guess_num, guesses = guess(guesses)
    guess_num1=[]
    for i in str(guess_num):
        guess_num1.append(int(i))

    if secret_num == guess_num1:
        test = False
        print("Correct, you've guessed the right number in {} guesses!".format(guesses))

    else:
        bulls, cows = bulls_cows(secret_num, guess_num1)
        print('bulls:', bulls, 'cows:', cows)

end_time = time.time()

hours, mins, sec = guess_time(start_time, end_time)
elapsed_time = '{:02}:{:02}:{:02}'.format(hours, mins, sec)
print('Your guessing time is {}'.format(elapsed_time))

word = message(guesses)
print("That's {}".format(word))

store_stats(guesses, elapsed_time)
