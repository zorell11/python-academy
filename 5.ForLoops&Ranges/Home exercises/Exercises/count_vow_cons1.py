vowels = set('aeiouy')

letters = set()
# 1.
letter_a = 97
letter_z = 123

# 3.
for num in range(letter_a, letter_z):
    # 2.
    letters.add(chr(num))
print(letters)
print(vowels)
# 4.
consonants = letters - vowels

counts = {'cons':0,'vows':0}

sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'

for char in sentence:
    if char.isalpha():
        if char.lower() in vowels:
            counts['vows'] += 1
        else:
            counts['cons'] += 1

print('No. consonants: ' + str(counts['cons']) + ' | No. vowels: ' + str(counts['vows']))
