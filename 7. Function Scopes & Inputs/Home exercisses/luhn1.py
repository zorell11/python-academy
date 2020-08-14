
def luhn(number):
    s1, s2 = 0, 0
    number = str(number)[::-1]
    for k,num in enumerate(number,1):
        if k%2 == 1:
            s1+= int(num)
        else:
            num = int(num) * 2
            if num >9:
                num = int(str(num)[0]) + int(str(num)[1])
            s2 += num

    return True if (s1+s2)%10==0 else False




print(luhn(49927398716))
print(luhn(61789372994))
