#!/usr/bin/env python3



def my_find(seq,item):
    for counter, i in enumerate(seq):
        if i == item:
            return counter
    return -1

a='adwrgev'
b='w'
print(my_find(a,b))
print(my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}] , {'name': 'John'}))
