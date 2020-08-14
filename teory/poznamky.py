hours, mins = '17:15'.split(':')
hours, *mins = '17:15:11'.split(':')

daytime = ['AM','PM'][int(hours)>=12]
[1,2][False] vystup je 1

argument - sum(1, 2) 1,2 -argument
parameter - def sum(a,b):  a,b - parameters

adjusted_h = hours if int(hours)==12 else str(int(hours) % 12)


def my_count(cislo:int , seq:list):  !!!int a list su pozanmky ze aky typ premennej sa ocakava
    prem = 0
    for i in seq:
        if i == cislo:
            prem += 1
    return prem


###3 pozriet dictionaris:
ako vytvorit, pridat, ako ziskat kodnoty, akoz iskat kluce, ako ziskat obidve
list - mutable
tuple - unmutable


######
def func(*iterable):                bez * vypise na kazdy riadok
    for i in iterable:                 * - vsetky zvysne argumenty
        print(i)

func([1,2,3,4,5])
func(1,2,3,4,5)


def func(one, two, *args):
    print(one)
    print(two)
    print(args)

func(1,2,3,4,5,6)



def func(one, two, *args, four):
    print(one)
    print(two)
    print(args)
    print(four)

func(1,2,3,4,5,6)  - error
func(1,2,3,4,5,four = 6)


#########

'My name is %s ans I am %d years old.' %('Bob', 37)
'My name is {} and I am {} years old.'.format('Bob', 37)

%s -retrazec
%d - cislo

* - rozbali sekvenciu
** - rozbali slovnik

'{:$^4}'.format(200)
$ -  fill, cim sa vyplnaju volne miesta
^ - zaorvnat na uprostred
< - dolava zarvnanie
> - doprava zarovnanie
4 - sirka

'{:,}'.format(1000000)
'1,000,000'

'{:.5}'.format(123456.789)
'1.2346e+05'

'{:{}}'.format(222, 5)
'  222'
