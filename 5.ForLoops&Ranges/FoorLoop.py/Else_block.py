#!/usr/bin/env python

checked_string = 'Python Loop x Statements'
for letter in checked_string:
    if letter in 'xz':
        print('We have found it')
        break
    else:
        print('There are no letters "xz" inside the string')

print(40 *'*')

checked_string = 'Python Loop x Statements'
for letter in checked_string:
    if letter in 'xy':
        print('We have found it')
        break
else:
    print('There are no letters "xz" inside the string')
