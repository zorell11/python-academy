
def luhn(number):
    reverse = list(str(number)[::-1])

    for i in range(len(reverse)):
        reverse[i] = int(reverse[i])

    odd_digit = reverse[::2]
    s1 = sum(odd_digit)
    print(s1)

    even_digit = reverse[1::2]

    for i in range(len(even_digit)):
        even_digit[i] = 2 * even_digit[i]



    s2 = sum(even_digit)
    print(s2)
    if (s1 + s2) % 10 == 0:
        return True
    else:
        return False


print(luhn(49927398716))
