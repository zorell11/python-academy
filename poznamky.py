https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

PEP8:
https://pep8.org/
https://www.python.org/dev/peps/pep-0008/

Strings

indexing:
>>> '01234'[2]
2

slicing:
sequence[start:end]
sequence[:end]
sequence[start:]
sequence[:]

striding:
sequence[start:stop:step]

String Methods
Operation	Syntax	Description	Example	Output
Letter change	   .lower()	    Return string with all letters lowercased	'HA HA'.lower()	'ha ha'
Letter change	   .upper()	    Return string with all letters uppercased	'he he'.upper()	'HE HE'
Letter check	   .islower()	Returns boolean value True, if all items in string are lowercased. Otherwise returns False	'David'.islower()	False
Letter check	   .isupper()	Returns boolean value True, if all items in string are uppercased. Otherwise returns False	'PETR'.isupper()	True
Letter change	   .title()	    Returns a new string, where every word begins with capital letter. If a number sequence precedes letters, the method will uppercase the first letter anyway. Also if there is apostrophe within the word, the letter succeding the apostrophe is also capitalized.	'123word'.title()	123Word
Letter change	   .replace(what,forwhat)	Replaces a substring for another substring inside the operated string.	'Race'.replace('R','F')	'Face'
Letter check	   .istitle()	Returns boolean value True, if the first character is a capital letter. Otherwise returns False	'Martin'.istitle()	True
Letter change	   .swapcase()	Swaps the upper and lowercase letters.	'Mr. Jones PhD'.swapcase()	'mR. jONES pHd.'
Split by symbol	   .split('a')	Splits the given string by the symbol given in the parentheses into a list. If the parentheses are empty, the method splits the list by space	splitted = 'This is my car'.split()	['This', 'is', 'my', 'car']
Split by delimeter .splitlines([keepends])	Splits the string on line end delimiters. Flag keepends - tells whether line delimiters ('\n' or '\r' etc.) should be kept	'This is the first line\nThis is the second line'.splitlines(keepends = True)	['This is the first line\n',This is the second line']
Split by separator .partition(separator)	Returns a tuple of part of the string preceding the separator, separator, part of the string succeeding the separator	up-to-date'.partition('-')	('up', '-', 'to-date')
Strip of symbols   .strip()	    Strips the given strings of the symbols we want to remove	'www.example.cz'.strip('www.cz')	'example'
Character type	   .isdecimal()	Returns True if all the characters inside the string are decimal characters ('0','1','2','3','4','5','6','7','8','9') and there is at least 1 character, otherwise False	'1234'.isdecimal()	True
Character type	   .isdigit()	Returns True if all the characters inside the string are decimal characters or subscripts or superscripts (e.g. "\u00B2") and there is at least one character, otherwise False.	'\u00B2'.isdigits()	True
Character type	   .isnumeric()	Returns True if all the characters inside the string are decimal characters, subscripts, superscripts (e.g. "\u00B2"), fractions (e.g. "\u00BC"), roman numerals (e.g. "\u2165"), currency numerators etc. (all characters that have the Unicode numeric value property), and there is at least one character, False otherwise.	'\u2165'.isnumeric()	True
Character type	   .isalpha()	Returns boolean value True, if all the characters are letters. Otherwise returns False	'asdvfb'.isaplha()	True
Character type	   .isalnum()	Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise (Basically all the Character Type methods above - .isdecimal(),.isdigit(),.isnumeric(), .isalpha().	'Z312'.isalnum()	True
Search	           .find('m')	Finds a character in a string and returns its index	'Thomas'.find('m')	3
Join by symbol	   .join(seq)	Joins the items of the sequence in the parentheses by the symbol written in the string	':'.join(['a', 'b'])	'a:b'


#################################################################################

tuple	Objects separated by commas and enclosed in parenthesis	(1, 2, 3, 4) or ('a', 'b', 'b')

indexing:
>>> ('a','bc','d')[2]
'd'

slicing:
sequence[start:end]
sequence[:end]
sequence[start:]
sequence[:]

striding:
sequence[start:stop:step]


#################################################################################

list	Object separated by commas and enclosed in square brackets	[5, 5, 5, 5, 5]
indexing:
>>> ['a','bc','d'][2]
'd'

slicing:
sequence[start:end]
sequence[:end]
sequence[start:]
sequence[:]

striding:
sequence[start:stop:step]

sorting - metoda
list.sort(key=None,reverse=False)
sorted(iterable, key=None, reverse=None)

List Operations:
Examples in the table below will simulate action on the list lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Item replacement	seq[index] = value	Item at specified index is replaced by a new value.	lst[2] = 75	[0, 1, 75, 3, 4, 5, 6, 7, 8, 9]
Slice replacement	seq[start:end] = iterable	The slice and the iterable have to be the same lenght. If the iterable is smaller number than the sequence slice, the rest in the sequence slice is discarded. If the iterable is longer, than slice, all items from the iterable are inserted into the sequence.	lst[3:6]=[65,98]	[0, 1, 2, 65, 98, 6, 7, 8, 9]
Item removal	    del seq[index]	Removes item at specified index	del lst[3]	[0, 1, 2, 4, 5, 6, 7, 8, 9]
Slice removal	    del seq[start:end] or seq[start:end] = []	Removes slice from item at index start till item at index end-1.	del lst[3:6]	[0, 1, 2, 6, 7, 8, 9]
Striding removal	del seq[start:end:step]	Removes every nth item in a slice spanning from index start till index end-1.	del lst[::2]	[1, 3, 5, 7, 9]

List Methods:
Examples in the table below will simulate action on the list lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

The method are only functional with list - lst.method(argument)
Operation	Syntax	Description	Example	Output
Insertion	      .append(x)	Appends 'x' value at the end of the list	lst.append('50')	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 50]
Insertion	      .insert(i, x)	Inserts 'x' value at the index 'i'	lst.insert(0, 420)	[420, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Insertion	      .extend(seq)	Extends the list by another list	lst.extend([420,2510])	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 420, 2510]
Item Removal      .remove(x)	Removes item 'x' from the list. If 'x' is not found, we get an error	lst.remove(9)	[0, 1, 2, 3, 4, 5, 6, 7, 8]
Item Removal	  .pop([i])	    Returns 'i' and deletes it from the list. If 'i' is not stated, the method takes the last value of the list by default	lst.pop()	9; [0, 1, 2, 3, 4, 5, 6, 7, 8]
Item Removal	  .clear()	    Deletes all the items from the list. The method takes no arguments	lst.clear()	[]
Count	          .count(x)	     Returns count of 'x' in the list	lst.count(5)	1
Search            .index(x)	    Finds 'x' in list and returns its index	lst.index(5)	5
Reversion	      .reverse()	Changes the order of the list. The method takes no arguments	lst.reverse()	[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Copy	          .copy()	     Returns a copy of the original list. The method takes no arguments	lst_copy = lst.copy()	lst_copy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Sort	          .sort(key=None,reverse=False)	Returns sorted sequence according to key and the parameter reverse	lst.sort(reverse=True)	[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#################################################################################

dictionary	Pairs of objects - key value pairs separated by colon. Key value pairs are separated by comma and everything is enclosed
in curly braces	{'a':1, 'b':2}
{'key':'value'}
creation:
d1 = dict()
d2 = {}
d4 = dict(First_name = 'Zoltan', Last_name = 'Veres', age = 37)
>>> d4['First_name']
'Zoltan'

>>> my_dict
{'volume': [3, 4, 7], 'surface': [3, 4], 'lengths': [3, 4, 7]}
>>>
>>>
>>> my_volume = my_dict['volume'][0]*my_dict['volume'][1]*my_dict['volume'][2]
>>>
>>> my_volume
84

dict.fromkeys(sequence[,value])
>>> d = dict.fromkeys(('Account1','Account2','Account3'),0)
>>> d
{Account1':0,'Account2':0,'Account3':0}

Insert:
>>> my_dict = {}
>>> my_dict['name'] = 'John'
>>> my_dict['surname'] ='Smith'
Update:
my_db.update(Name ='John E. Smith')
my_db.update({'Performance': {'Q1': 1, 'Q2':1, 'Q3':2, 'Q4':1}})

Get:
my_db.get(key[,default_value=None])

Remove item:
del my_dict[key]

Remove:
my_db.pop(key[,default_value])
db.pop('Performance', 'nigger')
{'Q1': 1, 'Q2': 1, 'Q3': 2, 'Q4': 1}

my_db.popitem() - removes the last key-value pair
>>> my_db.popitem()
('Address', {'Country': 'Venezuela', 'City': 'Boston', 'Street': 'Main', 'Street #': 241})

Clear:
my_db.clear()

Dictionary Views:
.keys() - returns objects of type dict_keys that refer to all top level keys in dictionary
.values() - returns objects of type dict_values that refer to all top level values in dictionary
.items() - returns objects of type dict_items that refer to all tuples of top level key-value pairs in dictionary
list(my_db.keys()) == list(my_db)

zip()

Dictionary methods
Update the dictionary	  .update()	Adds elemnts from other dictionary or iterable pairs (tuples).	store = {'butter': 2.35, 'bread': 0.95}; new = {'milk': 1.15}; store.update(new)	{'milk': 1.15, 'bread': 0.95, 'butter': 2.35}
Insert missing keys with values	.setdefault()	Insert key with a value, if key is not present	person = {'name':'Martin'}; person.setdefault('age': 25)	{'age': 25, 'name': 'Martin'}
Get value	              .get()	Returns value of the key.	dict = {'a': 1, 'b': 2}; dict.get('b')	2
Remove and return value	  .pop()	Removes and returns the value of the chosen key.	dict = {'a': 1, 'b': 2}; dict.pop('a')	1
Remove and return pair	  .popitem()	Removes and returns a pair from the dictionary.	dict = {'a': 1, 'b': 2}; dict.popitem()	('a', 1)
Remove items	  .clear()	Removes all items.	dict = {'a': 1, 'b': 2}; dict.clear()	{}
Copy dictionary	  .copy()	Returns shallow copy of a dictionary.	dict = {'a': 1, 'b': 2}; dict.copy()	{'a': 1, 'b': 2}
Create from keys  .fromkeys()	Returns a new dictionary with keys from given sequence.	dict = {}; list = ["A","B","C"]; dict.fromkeys(list)	{'C': None, 'B': None, 'A': None}
View keys	      .keys()	Returns view object of all keys.	dict = {'a': 1, 'b': 2}; dict.keys()	['a', 'b']
View values	      .values()	Returns view object of all values.	dict = {'a': 1, 'b': 2}; dict.values()	[1, 2]
View pairs	      .items()	Returns view of (key, value) pair.	dict = {'a': 1, 'b': 2}; dict.items()	[('a', 1), ('b', 2)]

for and dictionaries:
Keys:
for k  in employee:
    print(k)
for k  in employee.keys():
    print(k)

values:
for v in employee.values():
    print(v)

Both keys and values:
for k,v in employee.items():
    print(k,v)


#################################################################################
Set & frozenset:
Type	Syntax
Set	{'a','b','c'}
Frozenset	frozenset({'a', 'b', 'c'})
unordered collections of immutable and unique objects. Important defining feature is the uniqueness
of each item in a set. Each object (item) appears only once in a set no matter how many times it has
been added. There are 2 types of set data in Python - set & frozenset. The difference among the two
is that set is mutable collection whereas frozenset is immutable.
set	Objects separated by commas enclosed in curly braces	{'a', 'b', 'c'}
NoneType	Tells us that no value has been assigned yet to the variable	None

Create:
my_set = set()
my_set = frozenset()
my_set = {'John', 'Rob'}

Adding item:
set1.add(item)
>>> names = {'Marcus', 'Alex'}
>>> names.add('Oliver')
>>> names
{'Marcus', 'Oliver', 'Alex'}

Remove ietm:
set1.discard(item)
>>> names = {'Marcus', 'Oliver', 'Alex'}
>>> names.discard('Oliver')
>>> names
{'Marcus', 'Alex'}

Union:
set1 | set2 | set3 | ...

Difference:
set1 - set2 - set3 ...
set1.difference(others)

Symmetric Difference
set1 ^ set2
set1.symetric_difference(others)

Intersection:
set1 & set2 & set3 & ...
set1.intersection(others)

Subset: -set1 is in the set2
set1.issubset(set2)
<=
>=
>>> set('Hello') <= set('Yellow H')
True
>>> set('Hello') >= set('Yellow H')
False

Disjoint: -no elements in common,
len(set1 & set2) == 0
set1.isdisjoint(set2)
>>> set((1,2,3,4)) & set((6,7,8))
set()
>>> len({1,2,3,4} & {6,7,8})
0
>>> {1,2,3,4}.isdisjoint({6,7,8})
True

#################################################################################

constructor:	int()	float()	str()	list()	tuple()	range()	bytes()	bytearray	dict()	set()

Build in functions:
https://docs.python.org/3/library/functions.html
print(char, end='')
abs(number) - abs(-12)=12,  abs(12.0)=12.0
round(number[,ndigits rounding to]) - round(-12)=-12, round(12.12,1)=12.1, round(12.12)=12
divmod(number1, number2) - divmod(7,3)=S(2,1)
sorted(iterable, key=None, reverse=None)
len()
max()
min()
type()
ord() - Character's number representation  ord('z') ->122
bool()
all()	all items of supplied sequence are of boolean value True
my_list = [1,2,3,4]     all(my_list)    True
my_list = [0,1,2,3,4]   all(my_list)    False
my_list = [1,2,3,4, ''] all(my_list)	False

any()	at least one of the items is True
my_list = [1,2,3,4]     any(my_list)    True
my_list = [1,'',0, '']  any(my_list)    True
my_list = ['',0, '']    any(my_list)    False
my_list = []            any(my_list)    False

chr()
>>> chr(100)
'd'

ord()
>>> ord('d')
100

zip()
>>> dict(zip(('Name','Age'),('John',45)))
{'Age': 45, 'Name': 'John'}
>>> dict(zip(range(10),range(10)))
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

enumerate()
numbers = [321,45,32,12,54]
for index, number in enumerate(numbers):
	print(index, number)
0 321
1 45
2 32
3 12
4 54

list(enumerate('For loops support iteration protocol'))
[(0, 'F'), (1, 'o'), (2, 'r'), (3, ' '), (4, 'l'), (5, 'o'), (6, 'o'), (7, 'p'), (8, 's'), (9, ' '), (10, 's'), (11, 'u'), (12, 'p'), (13, 'p'), (14, 'o'), (15, 'r'), (16, 't'), (17, ' '), (18, 'i'), (19, 't'), (20, 'e'), (21, 'r'), (22, 'a'), (23, 't'), (24, 'i'), (25, 'o'), (26, 'n'), (27, ' '), (28, 'p'), (29, 'r'), (30, 'o'), (31, 't'), (32, 'o'), (33, 'c'), (34, 'o'), (35, 'l')]

data = (('Age',43),('Name','John'),('Surname','Smith'))
for category, value in data:
     print(category,':',value)
Age : 43
Name : John
Surname : Smith

data = (('Age',43,True),('Name','John',True),('Surname','Smith',False))
for i,j,k in data:
    print(i,j,k)
Age 43 True
Name John True
Surname Smith False

reversed()
>>> my_string = 'Python'
>>> for char in reversed(my_string):
>>>     print(char, end='')
nohtyP

random():
random.random() - no argument, generating between: 0.0 - 1.0
random.shuffle(list) - miesat karty -The input sequence has to be of mutable data type, therefore we used a list.
random.choice(sequence) - If seq is empty, raises IndexError
random.randrange(start,stop,step) - returns a number n from a sequence between start and stop, excluding stop
random.randint(start,stop) - returns a number n that is greater or equal to start and smaller or equal to stop
random.sample(population, k) - returns a new k length list of unique elements chosen from the population sequence or set.
>>> a
[5, 3, 1, 7, 6, 8, 4, 2]
>>> random.sample(a, 4)
[3, 5, 2, 8]

ternarny operator:
variable_name = expression1 if condition else expression2

dir(csv)  co ponuka modul

hours, mins = '17:15'.split(':')
hours, *mins = '17:15:11'.split(':')

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



def func(onem two, *args, four):
    print(one)
    print(two) 
    print(args)
    print(four)

func(1,2,3,4,5,6)  - error
func(1,2,3,4,5,four = 6)


#########
"....%s....%d..." % (inserted_values)
'My name is %s ans I am %d years old.' %('Bob', 37)
"...{}...{}..".format(*input_arguments)
'My name is {} and I am {} years old.'.format('Bob', 37)
'{1} and {0}'.format(arg1, arg2)

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

project- piskorky
enumerate


file = open('')
file.read() - kurzor moves to the end
file.close()

file = open('', 'w')
file.write()
file.close()

file.tell() - kde sa nahcadza kurzor
file.seek(x) - nastavenie kurzra
file.seek(0,2) - nastavenie kurzora na koniec

file.read(N) - N-character
file.readline() - reads everything up to the newline character '\n' or the end of the file
file.readlines() splits the string being read on newline character '\n') and puts the individual lines of text into a list

file.write()
file.writelines()

'r' - open for reading (default)
'w' - open for writing, truncating the file first, erese the content, no read
'w+' - reading and writing, content of file is erased when the file is opened
'r+' - writing and reading, content is not removed, cursor is set to the fisrt position and the content will be overwritten
'a' - open for writing, appending to the end of the file if it exists, cannot read
'a+' - open for writing, appending to the end of the file if it exists, can read

Context Manager:
with object_supporting_context_manager as alias:
     statements to be performed with the object in the context

with open('test.txt', 'a') as file:
     file.write('This is the last line')

binary:
-b flag
image = open('img_2011.jpg', 'rb')
image = open('img_2011.jpg', 'wb')

file.name
file.mode

file size:
getsizeof()
import sys
sys.getsizeof(file)
