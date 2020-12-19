from functools import lru_cache

@lru_cache(maxsize=1000)
def fibo(nth):
    if nth == 0 or nth == 1:
        return nth
    else:
        return fibo(nth-1) + fibo(nth-2)


#a = fibo(0)
#b = fibo(1)

try:
    c = fibo('ola')
    print('{}'.format(c))

except (RecursionError,TypeError):
    print('Number must be an integer')
