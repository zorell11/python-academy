


import random

words = {'articles': ("the", "a", "an"),
         'determiners': ("another", "this", "every", "many"),
         'subjects': ("cat", "dog", "man", "woman"),
         'verbs': ("sang", "ran", "jumped"),
         'adverbs': ("loudly", "quietly", "well", "badly")}

combinations = [["articles", "subjects", "verbs", "adverbs"],
                ["determiners", "subjects", "verbs"],
                ["determiners", "subjects", "verbs", "adverbs"]]

def lorem_poetry(row):
    rows = []
    for j in range(row):
        sentence = []
        order = random.choice(combinations)
        for i in order:
            sentence.append(random.choice(words[i]))
        rows.append(' '.join(sentence))
        result = '\n'.join(rows)
    print(result)

lorem_poetry(5)
