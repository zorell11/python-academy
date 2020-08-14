
def my_modus(seq:list):
    dictionary = dict.fromkeys(data,0)
    for i in seq:
        dictionary[i] += 1
    return max(dictionary.values())

##### another solution
def my_modus2(seq):
    dictionary = dict.fromkeys(data,0)
    for key, item in dictionary.items():
        if item == 2:
            print(key)


print(my_modus([35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]))
