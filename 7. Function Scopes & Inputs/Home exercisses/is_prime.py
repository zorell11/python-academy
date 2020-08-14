
def get_prime(zoznam):
    for i in range(min(zoznam), max(zoznam)+1, min(zoznam)):
        if i in zoznam:
            zoznam.remove(i)
    return zoznam

def main(limit):
    #limit = int(input("List prime numbers till: "))
    lst = list(range(2,limit+1))

    prime = []

    while lst:
        prime.append(min(lst))
        lst = get_prime(lst)


    return limit in prime

print(main(50))
print(main(53))
print(main(54))
print(main(2))
print(main(3))
