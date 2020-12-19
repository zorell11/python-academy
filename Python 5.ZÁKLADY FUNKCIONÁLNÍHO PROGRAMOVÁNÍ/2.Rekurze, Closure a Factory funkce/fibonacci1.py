from functools import lru_cache

def fibo(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        value = fibo(n-1) + fibo(n-2)
        cache[n] = value
    return value



for i in range(1,32):
    print(i, ":", fibo(i))

@lru_cache(maxsize=1000)#default 1028 values - maxsize
def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n >2:
        return fibo(n-1) + fibo(n-2)

for i in range(1,32):
    print(i, ":", fibo(i))
