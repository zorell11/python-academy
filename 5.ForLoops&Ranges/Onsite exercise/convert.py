
convert = input('Add word to convert: ')
converted_word = ''
for i in convert:
    if i.isupper():
        converted_word += i.lower()
    else:
        converted_word += i.upper()

print(converted_word)
