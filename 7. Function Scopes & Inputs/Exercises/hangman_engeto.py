import random

def get_letter(status,guesses_available):
    print(' '.join(status))
    letter = input('Guess a letter | guesses available: '
                    + str(guesses_available) + '\n')
    return letter

def replace_letters(letter, word, status):
    count_replaced = 0
    for i, char in enumerate(word):
        if char == letter:
            status[i] = letter
            count_replaced += 1

    if count_replaced:
        print("Number of positions matched: " + str(count_replaced))

    else:
        print('No, the letter ' + letter + ' is not in my word')
        

def main(words):

    word = random.choice(words)
    guesses_available = int(len(word)*1.6)
    status = ['_'] * len(word)
    print('I am thinking of a word. What word is it?')

    while True:

        letter = get_letter(status, guesses_available)
        count_replaced = replace_letters(letter, word, status)

        guesses_available -= 1

        if '_' not in status:
            print('\nCongatulations, you have won!\n')
            break
        if not guesses_available:
            print('\nYou have lost. The word was:\n' + word)
            break

words = ['Hangman', 'available', 'increase']
main(words)
