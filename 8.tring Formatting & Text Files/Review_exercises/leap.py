
def leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

print('year 2000 is leap:', leap(2000))
print('year 1700 is leap:', leap(1700))
print('year 1600 is leap:', leap(1600))
print('year 1900 is leap:', leap(1900))
print('year 1996 is leap:', leap(1996))


def leap2(year):
    if ((year % 400 ==0) or (year % 100 != 0 and year % 5 ==0)):
        return True
    else:
        return False
print()
print('year 2000 is leap:', leap(2000))
print('year 1700 is leap:', leap(1700))
print('year 1600 is leap:', leap(1600))
print('year 1900 is leap:', leap(1900))
print('year 1996 is leap:', leap(1996))

def leap4(year):
    return True if ((year % 400 ==0) or (year % 100 != 0 and year % 5 ==0)) else False
print()
print('year 2000 is leap:', leap(2000))
print('year 1700 is leap:', leap(1700))
print('year 1600 is leap:', leap(1600))
print('year 1900 is leap:', leap(1900))
print('year 1996 is leap:', leap(1996))


def leap4(year):
    return ((year % 400 ==0) or (year % 100 != 0 and year % 5 ==0))

print()
print('year 2000 is leap:', leap(2000))
print('year 1700 is leap:', leap(1700))
print('year 1600 is leap:', leap(1600))
print('year 1900 is leap:', leap(1900))
print('year 1996 is leap:', leap(1996))
