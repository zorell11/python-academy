#Your task is to create 2 functions:
#Function my_min that imitates the built-in function min(). It should take any sequence data type as input and return the item with the lowest value.
#Example of using my_min:
#>>> my_min([43,45,87,21,23])
#21
#Function my_max that should imitate the built-in function max(). It should take any sequence data type as input and return item with the highest value.
#Example of using max:
#>>> my_max([43,45,87,21,23])
#87

def my_min(lst):
    min = lst[0]
    for i in lst[1:]:
        if i < min:
            min =i
    print(min)
    return min


def my_max(lst):
    max = lst[0]
    for i in lst[1:]:
        if i > max:
            max = i
    print(max)
    return max

my_min([43,45,87,21,23])
my_max([43,45,87,21,23])
