#Write a program that will take a list of words as input and will print to the terminal the longest
#word and its length in one tuple.
#Please use the following list:

words = ['Python', 'is', 'a', 'widely', 'used',
         'high-level', 'programming', 'language',
         'for', 'general-purpose', 'programming,',
         'created', 'by', 'Guido', 'van', 'Rossum',
         'and', 'first', 'released', 'in', '1991.']
#Example of running the script:
#$ python3 longest_word.py
#('general-purpose', 15)#
longest = ('',0)
while words:
    word = words.pop()
    if len(word) > longest[1]:
        longest = word, len(word)
print(longest)
