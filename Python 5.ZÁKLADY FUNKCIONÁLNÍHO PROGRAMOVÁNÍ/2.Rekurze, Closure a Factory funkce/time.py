import time


def while_time(n):
    faktotrial1 = 1
    while n>0:
        faktotrial1 *= n
        n -=1
    return faktotrial1

def for_time(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res



def rekurze_time(n):
    if n == 1:
        return 1
    return n * rekurze_time(n-1)

iteration = 998
start1 = time.time()
#print(while_time(iteration))
sol1 = while_time(iteration)
end1 = time.time()
time1 = end1 - start1

start2 = time.time()
#print(for_time(iteration))
sol2 = for_time(iteration)
end2 = time.time()
time2 = end2 - start2


start3 = time.time()
#print(rekurze_time(iteration))
sol3 = rekurze_time(iteration)
end3 = time.time()
time3 = end3 - start3

if sol1 == sol2 == sol3:
    print('Vysledky sa zhoduju.')
    print('While loop time: {}'.format(time1))
    print('For loop time: {}'. format(time2))
    print('Recursion time: {}'. format(time3))
else:
    print('Vysledky se nezhoduju')
