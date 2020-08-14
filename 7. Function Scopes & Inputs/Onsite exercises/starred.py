def my_sum(*args):
    result = 0
    for i in args:
        result += i
    return result

print(my_sum(1,2,3,4,5,6))


def kwargs(**args):
    print(args)

kwargs(name='Zoltan', city='Bratislava')
#kwargs('Zoltan', 'Bratislava')

def func(prefix, suffix, *args, **kwarg):
    for i in args:
        if 'capital' in kwarg and kwarg['capital']==True:
            i = i.upper()
        print(prefix + i + suffix)

func('in','ly','competent', 'formal', 'credib', capital=True)

print()

def func1(prefix, suffix, *args, capital):
    for i in args:
        if capital:
            i = i.upper()
        print(prefix + i + suffix)

func1('in','ly','competent', 'formal', 'credib', capital=True)
