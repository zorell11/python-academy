def create_alphabet():
    lst = []
    for i in range(97, 122 + 1):
        lst.append(chr(i))
    return lst

def caesar(text, offset):
    alphabet = create_alphabet()
    decrypt_text =''
    for i in text:
        if i.lower() not in alphabet:
            decrypt_text += i
            continue
        letter = (alphabet.index(i.lower()) + offset) % len(alphabet)
        if i.isupper():
            decrypt_text += (alphabet[letter]).upper()
        else:
            decrypt_text += alphabet[letter]
    return decrypt_text




def main():
    message = 'I love Python Academy'
    print(caesar(message,55))
    print(caesar(message,-2))

main()
