words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']

out = ('', 0)
while words:
    word = words.pop(0)
    if len(word) > out[1]:
        out = (word, len(word)) 


print(out)
