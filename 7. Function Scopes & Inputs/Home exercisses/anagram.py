
def all_anagrams(list):
    if not list:
        return False
    elif len(list) == 1:
        return True
    else:
        for word in list[1:]:
            for letter in list[0]:
                if letter not in word:
                    return False
        return True

def all_anagrams1(list):

    if list:
        result = True
        word = sorted(list.pop())
        for i in list:
            if word != sorted(i):
                result = False
    else:
        result = False

    return result




print(all_anagrams(['ship', 'hips']))
print(all_anagrams(['ship', 'hips', 'name']))
print(all_anagrams(['ship']))
print(all_anagrams([]))

print()

print(all_anagrams1(['ship', 'hips']))
print(all_anagrams1(['ship', 'hips', 'name']))
print(all_anagrams1(['ship']))
print(all_anagrams1([]))
