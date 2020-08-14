List methods:

-mutable:
Insertion       .append(x)	    Appends 'x' value at the end of the list	lst.append('50')
Insertion       .insert(i, x)	Inserts 'x' value at the index 'i'	        lst.insert(0, 420)
Insertion       .extend(seq)	Extends the list by another list            lst.extend([420,2510])
Item Removal    .remove(x)	    Removes item 'x' from the list. If 'x' is not found, we get an error	lst.remove(9)
Item Removal	.pop([i])	    Returns 'i' and deletes it from the list. If 'i' is not stated, the method takes the last value of the list by default	lst.pop()
Item Removal	.clear()	    Deletes all the items from the list. The method takes no arguments	lst.clear()
Count	        .count(x)	    Returns count of 'x' in the list	        lst.count('5')
sort            .sort(key=None,reverse=False)	Returns sorted sequence according to key and the parameter reverse	lst.sort(reverse=True)
Search          .index(x)	    Finds 'x' in list and returns its index	    lst.index('5')
Reversion       .reverse()      Changes the order of the list. The method takes no arguments	    lst.reverse()
copy            .copy()         Returns a copy of the original list. The method takes no arguments	lst_copy = lst.copy()

List operations:
Item replacement        seq[index] = value
Slice replacement       seq[start:end] = iterable
Item removal            del seq[index]
Slice removal	        del seq[start:end]or seq[start:end] = []
Striding removal	    del seq[start:end:step]



###############################
String methods:
Syntax	Example	Output	Description
.lower()	    'HA HA'.lower()	     'ha ha'   Return string with all letters lowercased
.upper()	    'he he'.upper()	     'HE HE'   Return string with all letters uppercased

.islower()	    'David'.islower()  	  FALSE	   Returns boolean value True, if all items in string are lowercased. Otherwise returns False
.isupper()	    'PETR'.isupper()	  TRUE	   Returns boolean value True, if all items in string are uppercased. Otherwise returns False
.istitle()      'Martin'.istitle()    TRUE	   Returns boolean value True, if the first character is a capital letter. Otherwise returns False
.isdecimal()	'1234'.isdecimal()	  TRUE	   Returns True if all the characters inside the string are decimal characters ('0','1','2','3','4','5','6','7','8','9') and there is at least 1 character, otherwise False
.isdigit()	    '\u00B2'.isdigits()	  TRUE	   Returns True if all the characters inside the string are decimal characters or subscripts or superscripts (e.g. "\u00B2") and there is at least one character, otherwise False.
.isnumeric()	'\u2165'.isnumeric()  TRUE	   Returns True if all the characters inside the string are decimal characters, subscripts, superscripts (e.g. "\u00B2"), fractions (e.g. "\u00BC"), roman numerals (e.g. "\u2165"), currency numerators etc. (all characters that have the Unicode numeric value property), and there is at least one character, False otherwise.
.isalpha()	    'asdvfb'.isaplha()	  TRUE	   Returns boolean value True, if all the characters are letters. Otherwise returns False
.isalnum()	    'Z312'.isalnum()	  TRUE	   Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise (Basically all the Character Type methods above - .isdecimal(),.isdigit(),.isnumeric(), .isalpha().
.startswith()   'Jan'.startswith('J') TRUE

.find('m')	     'Thomas'.find('m')	    3       Finds a character in a string and returns its index
.rfind('t')                                 Return the highest index in the string where substring sub is found,
.title()	'123word'.title()	123Word	   Returns a new string, where every word begins with capital letter. If a number sequence precedes letters, the method will uppercase the first letter anyway. Also if there is apostrophe within the word, the letter succeding the apostrophe is also capitalized.

.replace(what,forwhat)	'Race'.replace('R','F')	'Face'	Replaces a substring for another substring inside the operated string.
.swapcase()	            'Mr. Jones PhD'.swapcase()	'mR. jONES pHd.'	Swaps the upper and lowercase letters.
.split('a')	            splitted = 'This is my car'.split()	['This', 'is', 'my', 'car']	Splits the given string by the symbol given in the parentheses into a list. If the parentheses are empty, the method splits the list by space
.splitlines([keepends])	'This is the first line\nThis is the second line'.splitlines(keepends = True)	['This is the first line\n',This is the second line']	Splits the string on line end delimiters. Flag keepends - tells whether line delimiters ('\n' or '\r' etc.) should be kept
.partition(separator)	up-to-date'.partition('-')	('up', '-', 'to-date')	Returns a tuple of part of the string preceding the separator, separator, part of the string succeeding the separator
.strip()	     'www.example.cz'.strip('www.cz')	'example'	Strips the given string(s) of the symbols we want to remove. The symbols will be removed only if they are at the beginning and the end.
.join(seq)	     ':'.join(['a', 'b'])	'a:b'	Joins the items of the sequence in the parentheses by the symbol written in the string
