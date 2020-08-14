# Create a program that will ask the user for any word and will then begin to search for the word in the text we have attached bellow. If the word is found, the program should print the number representing word's position (order) in the given string:
#Example:
#SEARCH WORD: miles
#POSITION: 4
#SEARCH WORD: milesss
#NO SUCH WORD



text = '''
Situated valley about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''

search = input('SEARCH WORD: ')
text1 = text.split()
found = True
for index, word in enumerate(text1):
    if word.strip('.,') == search:
        print('POSITION:', index + 1)
        found = False

if found:
    print("NO SUCH WORD")
