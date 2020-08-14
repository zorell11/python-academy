def list_primes(num):
    prime = []
    for i in range(1, num + 1):
        lst = []
        for j in range(1, i+1):
            if i%j == 0:
                lst.append(j)
        if len(lst) == 2:
            prime.append(i)
    return prime

def is_prime(num):
    return num in list_primes(num)

#def is_prime(num):
#    lst = []
#    for i in range(1, num + 1):
#        if num%i == 0:
#            lst.append(i)
#    if len(lst) == 2:
#        return True
#    else:
#        return False


def main():
    print(list_primes(2))
    print(list_primes(54))
    print(is_prime(54))
    print(is_prime(53))

main()
