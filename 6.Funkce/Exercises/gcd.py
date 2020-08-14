# GCD is an acronym for Greatest Common Divisor. Your task is to create a function gcd(),
# that will calculate greatest common divisor of two integers.
# The GCD for numbers 12 and 8 is 4, because after the division by 4, there is 0 remainder.


def gcd(a, b):
    divisor = 1
    end = a if a > b else b
    for i in range(1, end + 1):
        if a % i == 0 and b % i == 0:
            divisor = i
    return divisor

print(gcd(414,78))
print(gcd(414,49))
