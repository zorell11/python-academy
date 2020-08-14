https://docs.python.org/3/library/stdtypes.html

zaujimave riesenia:
variable_name = expression1 if condition else expression2
price = ''.join([char for char in price if char!=','])
mode = 'a' if 'gold_price.csv' in os.listdir() else 'w'

#############################################
if __name__=="__main__":
    main()
#############################################

list comprehention(set,...):
>>> ls = [str(item) for item in new_employee]
>>> ls
['Mills', 'Amanda', 'Mills, Amanda', '41', 'Leicester', 'Quality Assurance', 'Female']
>>>


int	5
float	5
string	'abc' or '1234' etc.
tuple	(1, 2, 3, 4) or ('a', 'b', 'b')
list	[5, 5, 5, 5, 5]
range	range(0,10)
bytes	b'5'
bytearray	bytearray(21324)
dictionary	{'a':1, 'b':2}
set	{'a', 'b', 'c'}
NoneType	None

convertion:
constructor: 	int()	float()	str()	list()	tuple()	range()	bytes()	bytearray	dict()	set()
list,dictionary, set, tuple cannot be converted into integer or float

################################################################################


comparison:
identical	a is b
not identical	a is not b

################################################################################


################################################################################
Booleans:
>>> bool(1)
True
>>> bool(0)
False
>>> bool('')
False

These values are considered False in Python:
None
False
zero of any numeric type, for example, 0, 0.0, 0j.
any empty sequence, for example, '', (), [].
any empty mapping (dictionary), for example, {}.


>>> a = 2
>>> b = 3.14
>>> a and b
3.14

>>> a = 2
>>> b = 3.14
>>> a or b
2
################################################################################
Features of sequences
Indexing:
Strings
>>> '01234'[2]
2
Lists
>>> ['a','bc','d'][2]
'd'
Tupples
>>> ('a','bc','d')[2]
'd'


Slicing:
sequence[start:end]
sequence[:end]
sequence[start:]
sequence[:]

Striding:
sequence[start:stop:step]

Repetetion:
-Strings:
>>> 'ab' * 2
'abab'

-Lists
>>> ['ha'] * 3
['ha', 'ha', 'ha']
-Tuples
>>> ('ha',) * 3
('ha', 'ha', 'ha')

Membership testing:
>>> 'a' in 'abc'
True

#########################


if-else

ternary operator:
variable_name = expression1 if condition else expression2
hour = 15
day_time = 'Morning' if hour < 12 else 'Afternoon'



########################
enumerate()
numbers = [321,45,32,12,54]
for index, number in enumerate(numbers):
    if index % 2 == 0:
        print(number, ':', number**2)
