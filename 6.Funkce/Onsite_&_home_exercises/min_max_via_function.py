#!/usr/bin/env python3

seznam = [43, 45, 87, 21, 23, 54, 99]
print(seznam)

def minimum(zoznam):
    min = zoznam[0]
    for i in zoznam[1:]:
        if min > i:
            min =i
    return min


def maximum(zoznam):
    max = zoznam[0]
    for j in zoznam[1:]:
        if max < j:
            max = j
    return max

max_seznam = maximum(seznam)
min_seznam = minimum(seznam)

print("Minimum:",min_seznam)
print("Maximum:",max_seznam)

print("Minimum:",minimum(seznam))
print("Maximum:",maximum(seznam))
