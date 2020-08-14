#!/usr/bin/env python3

seznam = [43, 45, 87, 21, 23]
print(seznam)
min = seznam[0]
for i in seznam:
    if min > i:
        min =i
print("Minimum:",min)


max = seznam[0]
for j in seznam:
    if max < j:
        max = j
print("Maximum:",max)
