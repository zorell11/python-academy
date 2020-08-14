# Now let's practice what we've learned about sets.
#We will work with these two strings:
#string01 = 'Bratislava'`<br>
#string02 = 'Budapest'`<br>
#Write a script that will find and print only elements using a suitable operator or method:
#Common - which have string01 and string02 common.
#Unique - which characters are present in string01 but not in string02.
#The output could look like this:
#~/PythonBeginner/Lesson3 $ python common_unique_chars.py
#Common characters: {'s', 'B', 't', 'a'}
#Unique characters: {'i', 'r', 'l', 'v'}

string01 = 'Bratislava'
string02 = 'Budapest'

common = set(string01) & set(string02)
print('Common characters:', common)

unique = set(string01) - set(string02)
print('Unique characters:', unique)

print('Common characters:', set(string01).intersection(string02))
print('Unique characters:', set(string01).difference(string02))
