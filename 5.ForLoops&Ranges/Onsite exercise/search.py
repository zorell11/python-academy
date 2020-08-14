text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''

def ask_user():
    search_word = input("SEARCH WORD: ")
    return search_word

def split(text):
    text = text.split()
    return text

def search(search_word, text):

    prem = -1
    for index, word in enumerate(text,1):
        word = word.strip(',./-')
        if word == search_word:
            print('POSITION: ', index)
            prem += 1

    if prem == -1:
        print('NO SUCH WORD')

def main():
    word = ask_user()
    searched_text = split(text)
    search(word, searched_text)


if __name__ == "__main__":
    main()
