

VOWELS = 'aeiouy'
SENTENCE = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
SENTENCE.strip('.')
vovel = 0
consonant = 0
for i in SENTENCE.split():
    a = i.strip('.')
    for j in a:
        if j.lower() in VOWELS:
            vovel += 1
        else:
            consonant += 1

print('No. consonants:', consonant, '| No. vowels:', vovel)
