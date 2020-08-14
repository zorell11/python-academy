#Your task is to create a script called check_start.py that will:
# -ask the user for the secret password
# -if the password given, starts with any of the lowercase 'a','e','f','q','z', print to the terminal 'Welcome!'
# -otherwise print 'The input does not match'

#Example of running the script:
#/Users/PythonBeginner/Lesson1$ python check_start.py
#Please enter the password: abcd
#Welcome!
#/Users/PythonBeginner/Lesson1$ python check_start.py
#Please enter the password: black hand
#The input does not match

PASS = ['a','e','f','q','z']
password = input("Please enter the password: ")

if password[0] in PASS:
    print("Welcome")
else:
    print('The input does not match')
