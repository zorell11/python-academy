

def is_leap(year):
    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        return True
    else:
        return False

def is_leap1(year):
    return (year%400 == 0) or (year%4 == 0 and year%100 != 0)

print(is_leap(2000))
print(is_leap(1600))
print(is_leap(1996))
print(is_leap(2004))
print()
print(is_leap(1700))
print(is_leap(1500))
print(is_leap(1900))
print()
print()
print(is_leap1(2000))
print(is_leap1(1600))
print(is_leap1(1996))
print(is_leap1(2004))
print()
print(is_leap1(1700))
print(is_leap1(1500))
print(is_leap1(1900))
