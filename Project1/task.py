'''
author = Zoltan Veres
'''
# database of the registered username - password pairs
db = dict(bob = 123, ann = 'pass123', mike = 'password123', liz = 'pass123')

print(40 * '-')
print("Welcome to the app. Please log in:")
username = input("USERNAME: ")
password = input("PASSWORD: ")
print(40 * '-')

# test if the username match with password
if username not in db.keys() or password != str(db.get(username)):
    print("Wrong username or password")
    exit()

text_number = int(input('''We have 3 texts to be analyzed.
Enter a number btw. 1 and 3 to select: '''))
print(40 * '-')

# analyzed texts
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

#test if user entered choice between 1 and 3
if len(TEXTS) < text_number or text_number < 1:
    print("wrong choice")
    exit()

# remove special charcters from the chosen text and convert it to list - text_mod2
text = text_number - 1
text_mod1 = str(TEXTS[text]).replace('\n', ' ').replace('.', ' ').replace(',', ' ').replace('-', ' ')
text_mod2 = text_mod1.split()

print("There are " + str(len(text_mod2))+ " words in the selected text.")

# Calculation of the statistics for the selected text
premenna = 0
numeric = 0
string = 0
lowercase = 0
uppercase = 0
titlecase = 0
frequency = {} #store the frequencies of word lengths
numeric_sum = 0
while len(text_mod2) > premenna:
    if str(text_mod2[premenna]).isnumeric():
        numeric += 1
        numeric_sum += int(text_mod2[premenna])   #summ all the numbers in this

    elif str(text_mod2[premenna]).islower():
        lowercase += 1

    elif str(text_mod2[premenna]).isupper():
        uppercase += 1

    elif str(text_mod2[premenna][:1]).isupper():
        titlecase += 1

# fill dictionary with frequencies of word lengths in the text.
    lenght = len(text_mod2[premenna])
    if lenght in frequency:
        frequency[lenght] += 1
    else:
        frequency.update({lenght: 1})

    premenna += 1


print("There are", titlecase, "titlecase words")
print("There are", uppercase, "uppercase words")
print("There are", lowercase, "lowercase words")
print("There are", numeric,  "numeric strings")
print(40 * '-')


premenna1 = 1  #auxiliary variable to create the bar chart
premenna2 = 0  #auxiliary variable to store to values from dictionary
#creating the bar chart
while max(frequency)+1 > premenna1:
    if premenna1 in frequency:
        premenna2 = frequency.pop(premenna1)
        print(premenna1, premenna2 * '*', premenna2)
        frequency.update({premenna1 : premenna2})

    premenna1 += 1
print(40 * '-')
print("If we summed all the numbers in this text we would get:", numeric_sum)
print(40 * '-')
