
txt= 'It was a bright, sunny day in May, and the church bell was just ringing'
#txt = txt.lower()

letters = {}

for letter in txt:
    letters.setdefault(letter, 0)
    letters[letter] += 1

print(letters)
