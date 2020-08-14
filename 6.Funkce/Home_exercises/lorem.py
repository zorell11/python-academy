import random


words = {'articles' : ("the", "a", "an"),
         'determiner' : ("another", "this", "every", "many"),
         'subjects' : ("cat", "dog", "man", "woman"),
         'verbs' : ("sang", "ran", "jumped"),
         'adverbs' : ("loudly", "quietly", "well", "badly")}

orders = [["articles", "subjects", "verbs", "adverbs"], ["determiner", "subjects", "verbs"], ["determiner", "subjects", "verbs", "adverbs"]]

rows = int(input("Zadaj pocet riadkov: "))

def create_table(rows_count):
    rows = []
    for i in range(rows_count):
        row = []
        for category in random.choice(orders):
            row.append(random.choice(words[category]))
        rows.append(' '.join(row))
    result = '\n'.join(rows)
    print(result)
    return rows

print(create_table(rows))
