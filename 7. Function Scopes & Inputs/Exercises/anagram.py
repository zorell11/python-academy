def all_anagrams(lst):
    if len(lst) == 0:
        return False
    elif len(lst) == 1:
        return True
    else:
        #first = sorted(lst[0])
        for i in lst[1:]:
            if sorted(i) == sorted(lst[0]): #first:
                return True
            else:
                return False

def all_anagrams1(lst):
    if lst:
        result = True
        seq = 


    else:
        return False




print(all_anagrams(['ship', 'hips']))
print(all_anagrams(['ship', 'hips', 'name']))
print(all_anagrams(['ship']))
print(all_anagrams([]))
