def luhn(num):
    num_str = str(num).replace(' ', '')
    print(num, type(num))
    print(num_str, type(num_str))

    s1 = s2 = 0

    for i, num in enumerate(num_str[::-1]):
        if i % 2 == 0:
            s1 += int(num)
        else:
            num = int(num) * 2
            if num > 9:
                num = int(str(num)[0]) + int(str(num)[1])
            s2 += int(num)
    result = True if (s1 + s2) % 10 == 0 else False

    return result


num = '61789372994'

print(luhn(num))
print(luhn(49927398716))
