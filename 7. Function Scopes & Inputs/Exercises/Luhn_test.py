
def luhn(number):
    reverse = []
    for i in str(number):
        reverse.insert(0 , int(i))
    s1 = sum(reverse[::2])
    s2 = []
    for i in reverse[1::2]:
        s = i * 2
        if s > 9:
            s2.append(int(str(s)[0]) + int(str(s)[1]))
        else:
            s2.append(s)
    if (sum(s2) + s1) % 10 == 0:
        return True
    else:
        return False


print(luhn(49927398716))
print(luhn(61789372994))
