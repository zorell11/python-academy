

def caesar(text, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''
    for i in text:
        if i.lower() not in alphabet:
            new_text += i
            continue

        place = alphabet.find(i.lower())
        new = (place+offset)%len(alphabet)

        if i.isupper():
            new_text += alphabet[new].upper()
        else:
            new_text += alphabet[new]

    print(new_text)



message = 'A BCD E'
#message = 'abc def ghi jkl mno pqr stu vwx Yz'
caesar(message,2)
caesar(message,-2)
