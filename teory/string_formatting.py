
 - formatting expression - %()
 "....%s....%d..." % (inserted_values)
s - tells Python, that the inserted item should be formatted as a string
d - tells Python, that the inserted item should be formatted as a decimal number

>>> print('My name is %s and I am %d years old.' %(name, age))
My name is Bob and I am 37 years old.

Insertion by key:
person_data = {'name':'Bob', 'age' : 37}
>>> formatted = 'My name is %(name)s and I am %(age)d years old.' % person_data
>>> formatted
'My name is Bob and I am 37 years old.'

################################################################################

- format method - .format():
"...{}...{}..".format(*input_arguments)
'{1} and {0}'.format(arg1, arg2)

>>> 'Today is our {}st anniversary.'.format(1)
Today is our 1st anniversary.

>>> name = 'Bob'
>>> age = 37
>>> 'My name is {1} and I am {0} years old.'.format(name, age)
'My name is 37 and I am Bob years old.''

Insertion by key:
>>> formatted = 'My name is {name} and I am {age} years old.'.format(name='Bob', age=37)
>>> formatted
'My name is Bob and I am 37 years old.'

>>> name = 'Bob'
>>> age = 37
>>> formatted = 'My name is {name} and I am {age} years old.'.format(name=name, age=age)
>>> formatted
'My name is Bob and I am 37 years old.'

Unpacking to format method:
two stars for dictionaries
>>> person_data = {'name':'Bob', 'age' : 37}
>>> formatted = 'My name is {name} and I am {age} years old.'.format(**person_data)
>>> formatted
'My name is Bob and I am 37 years old.'

one star for sequences
>>> data = ('Bob',37)
>>> formatted = 'My name is {} and I am {} years old.'.format(*data)
>>> formatted
'My name is Bob and I am 37 years old.'


'This is the formated text:
{[keyname_or_index]:[[fill] align] [sign] [width] [,] [.precision] [typecode]}'.format(keyname)

-keyname_or_index - determine, which argument should replace this placeholder
- fill - Can be any character other than "{" or "}". Here we provide the character, that should be filled in instead of white space if field width is greater than item length. This option can be specified only if align is specified.
- align - Possible values - <, >, ^ - left alignment / right alignment / centered alignment
- sign -Possible value +,- or " " (space) - force sign (+ or minus) and if needed insert space
- width - Can be an integer value. Specifies the length of the field. If the length specified is less than input string length, then the width parameter is ignored.
- ,(comma) - Possible value ,. Requests comma to mark thousands (inserted after every 3 zeroes) in numbers
- precision - Possible value .integer. Specifies maximum input string length or if argument is float, then max number of decimal places.

width:
>>> '|{0:3}|{0:4}|'.format(45)
'| 45|  45|'

align and fill
>>> '|{0:$<3}|{0:$<4}|'.format(45)
'|45$|45$$|'

precision
>>> '|{0:.5}|'.format(123.4567)
'|123.46|'
>>> '|{0:$<7.5}|'.format(1.234)
'|1.234$$|'
>>> '|{0:.3}|{0:.4}|{0:.5}|'.format(123.4567)
'|1.23e+02|123.5|123.46|'

coma:
>>> '|{0:*>19,.14}|'.format(123456789.123456)
'|**123,456,789.12346|'

sing:
>>> '|{0:-}|'.format(280)
'|280|'
>>> '|{0:+}|'.format(280)
'|+280|'
>>> '|{0: }|'.format(280)
'| 280|'
