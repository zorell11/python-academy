import random
def order_sequence():
    for i in range(1,len(l)):
        pos = i
        while pos > 0 and l[pos-1] > l[pos]:
            l[pos],l[pos-1] =  l[pos-1], l[pos]
            pos -= 1
    return l
def generate_random_list(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(1,100))
    return lst
l = generate_random_list(10)
print('Before sorting:',l)
print('After sorting:', order_sequence())
