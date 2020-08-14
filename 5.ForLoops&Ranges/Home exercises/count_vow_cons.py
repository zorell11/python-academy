vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'


text = 'a speech sound that is produced by comparatively open configuration of the vocal tract'
cons_count = 0
vowel_count = 0
count = {'cons':0, 'vowel':0}

for i in text:

    if i.lower() in vowels:
        #vowel_count += 1
        count['vowel'] += 1

    elif i.lower() in consonants:
        #cons_count += 1
        count['cons'] += 1

#print('No. consonants: ', cons_count, '| No. vowels:', vowel_count)
print('No. consonants: ', count['cons'], '| No. vowels:', count['vowel'])
