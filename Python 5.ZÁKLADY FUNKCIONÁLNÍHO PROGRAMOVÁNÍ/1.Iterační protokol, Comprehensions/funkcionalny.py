l1 = [1, 2, 3, 4, 5]
r = len(l1)
for i in range(r):
    l1[i] += 1
print(l1)

l1 = [1, 2, 3, 4, 5]
l1 = map(lambda x: x+1, l1)
print(list(l1))



def double(x):
    return x*2

m = map(double, range(5))

l1 = list(m)

print(l1)
