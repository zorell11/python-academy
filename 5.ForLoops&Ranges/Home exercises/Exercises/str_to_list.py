#Write a Python program which prompts and accepts a string of comma-separated numbers from a user and generates a list of those individual numeric strings converted into numbers.
#The program should print the resulting list to the terminal.
#Also take care of possible spaces that could be located at the beginning or the end of the string. In case you do not know, how to get rid of blank spaces at the beginning or end of a string, take a look at the str.strip() method.
#Example of running the program:
#$ python3 str_to_list.py
#Hello, please write your numbers and press enter to confirm: 23,54,  645, 76
#List: [23, 54, 645, 76]


string = input('Hello, please write your numbers and press enter to confirm: ')
list = []
for i in string.split(','):
    list.append(int(i.strip(' ')))
print(list)
