#!/usr/bin/env python3


#start = int(input("start number: "))
#stop = int(input("end number: "))



def my_sum(start, stop):
    sucet = 0
    for i in range(start, stop+1):
        sucet += i
    return sucet

print(my_sum(int(input("start number: ")), int(input("end number: "))))
#print(my_sum(start,stop))
