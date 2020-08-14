import random

WORDS = ['Hannibal', 'Superman', 'Batman', 'Joker', 'Robin']
TRY = 9

def get_word():
    return random.choice(WORDS)

def print_guess(guess):
    for i in guess:
        print(i, end=' ')

def check_letter(letter, lst, guessed_word):
    count = 0
    for index,i in enumerate(guessed_word,0):
        if letter == i:
            lst[index] = letter
            count += 1
    print("Yes, there are", count, "letters '" + letter +"'") if count>0 else print("No, the letter", letter, "is not in my word")
    return lst



def hangman(guessed_word, guess):
    print('I am thinking of a word. What word is it?:')
    print_guess(guess)
    for i in range(TRY,0,-1):
        letter = input('\nGuess a letter (' + str(i) +' guesses available):')
        guess = check_letter(letter, guess, guessed_word)
        print_guess(guess)
        if ''.join(guess) == guessed_word:
            print('\nCongratulations, YOU have won')
            exit()
    print('\nYou have lost. THe word was: ', guessed_word)


def main():
    guessed_word = get_word()
    print(guessed_word)
    guess = ['_'] * len(guessed_word)
    hangman(guessed_word, guess)

main()
