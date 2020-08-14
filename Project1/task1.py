'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

ACCOUNTS = { 'bob':'123', 'ann': 'pass123', 'mike': 'oassword123', 'liz': 'pass123'}

print('-' * 50)
print("Welcome to the app. Please log in:")
username = input('USERNAME: ')
password = input('PASSWORD: ')
print('-' * 50)

if ACCOUNTS[username] != password:
    print('LOGIN failed, username or password are wrong.')

else:
    print('We have 3 texts to be analyzed.')
    selection = int(input('Enter a number btw. 1 and 3 to select: '))
    print('-' * 50)

    text = TEXTS[selection - 1].split()
    text1 = []
    titlecase = 0
    uppercase = 0
    lowercase = 0
    numeric = 0
    frekvencies = {}
    text_len = 0
    for i in text:
        word = (i.strip(',.'))
        text1.append(word)

        text_len += len(word)

        if word.istitle():
            titlecase += 1

        if word.isupper():
            uppercase += 1

        if word.islower():
            lowercase += 1

        if word.isnumeric():
            numeric += 1

        if len(word) in frekvencies:
            frekvencies[len(word)] += 1
        else:
            frekvencies.update({len(word) : 1})

    words = len(text1)
    print('There are', words, 'words in the selected text.')
    print('There are', titlecase, 'titlecase words')
    print('There are', uppercase, 'uppercase words')
    print('There are', lowercase, 'lowercase words')
    print('There are', numeric, 'numeric strings')
    print('-' * 50)

    num_frekvencies = sorted(list(frekvencies))

    while num_frekvencies:
        index = num_frekvencies.pop(0)
        print(index, '*' * frekvencies[index], frekvencies[index])

    print('-' * 50)
    print('If we summed all the numbers in this text we would get:', text_len)
    print('-' * 50)
