

d1 = dict()
d2 = {}
d3 = { 'first_name' : 'Zoltan', 'last_name' : 'Veres', 'Age' : 35}
d4 = dict( first_name = 'Zoltan', last_name = 'Veres', Age = 35)

my_dict['first_name']
my_dict['name'] = 'John'

conversion: tuple -> dict
>>> dict(((1,2),(3,4),(5,6)))
{1: 2, 3: 4, 5:6}
>>> dict(((1,2),))
{1: 2}

Method's:
.popitem()  return(key + value) and remove the last item of dictionary
.pop()      remove, my_db.pop(key[,default_value]) return value or default value
.get()      my_db.get(key[,default_value=None])    my_db.get('Salary',0)
if not food.get('milk'):
    food['milk'] = 14.90
food['milk'] = food.get('milk',14.90)

.clear()    my_db.clear()
.update()   my_db.update({'Performance': {'Q1': 1, 'Q2':1, 'Q3':2, 'Q4':1}}) new item
            my_db.update(Name ='John E. Smith') modify-item
.copy()     new_db = my_db.copy()
del my_dict[key]

.setdefault()   letters={}  letters.setdefault('a', 0)  letters={'a':0}
                letters={'a':4}  letters.setdefault('a', 0)  letters={'a':4}

.keys() - returns objects of type dict_keys that refer to all top level keys in dictionary
.values() - returns objects of type dict_values that refer to all top level values in dictionary
.items() - returns objects of type dict_items that refer to all tuples of top level key-value pairs in dictionary

dict.fromkeys(sequence[,value])  dict.fromkeys(('Account1','Account2','Account3'),0)
zip()
>>> dict(zip(('Name','Age'),('John',45)))
{'Age': 45, 'Name': 'John'}
>>> dict(zip(range(10),range(10)))
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

for k  in employee:
    print(k)
for k  in employee.keys():
    print(k)
for v in employee.values():
    print(v)
for k,v in employee.items():
    print(k,v)
############################################
Set	{'a','b','c'}
Frozenset	frozenset({'a', 'b', 'c'})

my_set = set()
my_set = {'John', 'Rob'}
>>> s = set([1,2,4,2,5,6,4,3,3,'a'])
>>> s
{1, 2, 3, 4, 5, 6, 'a'}

add()     set1.add(item)        names.add('Oliver')
discard() set1.discard(item)    names.discard('Oliver')

1. Membership testing - in
>>> 5 in {1,6,13,54,21,654,10,5}
True
2. Checking length - len()
>>> len({5,1,5,6,7})
4

union:
set1.union(others)              set('Hello').union(set('Yellow'),set ('Fellow'))
set1 | set2 | set3 | ...        set('Hello') | set('Yellow') | set ('Fellow')

difference:
set1.difference(others)         set('Hello').difference(set('Yellow'),set ('Fellow'))
set1 - set2 - set3 ...          set('Hello') - set('Yellow') - set('Fellow')

Symmetric Difference:
set1.symetric_difference(others)    set('Hello').symmetric_difference(set('Yellow'))
set1 ^ set2                         set('Hello') ^ set('Yellow')

Intersection:
issubset(): set1.issubset(set2)        set('Hello').issubset(set('Yellow H'))
less than < and equal to = operators:  set('Hello') <= set('Yellow H')

Disjoint:  no elements in common
set1.isdisjoint(set2)           {1,2,3,4}.isdisjoint({6,7,8})
len(set1 & set2) == 0           len({1,2,3,4} & {6,7,8})
