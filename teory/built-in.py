Built-in functions:
https://docs.python.org/3/library/functions.html

abs(number)
round(number[,ndigits rounding to])
divmod(number1, number2)  == (number1 // number2, number1 % number2)
all()	all items of supplied sequence are of boolean value True
any()	at least one of the items is True
sorted(iterable, *, key=None, reverse=False)
ordered_data = sorted(counts, key=counts.get, reverse=True) sort dictionraies key based on dictionary value
len()
max()
min()
ord() - Character's number representation

range()
reversed()


not built-in:
import math
sqrt()  -  usage math.sqrt()

import time
from time import sleep

import random
random.randrange(100)
random.random()
random.shuffle(list)
random.choice(sequence)
random.randrange(start,stop,step)
random.randint(start,stop)
random.sample(population, k)         list = [20,40,80,100,120] random.sample(list,3) [120, 20, 100]
