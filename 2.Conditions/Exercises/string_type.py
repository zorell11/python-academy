#Your task is to create a script called string_type.py that will:
# -Ask user for any string
# -Determine, whether the string entered
# -contains only numbers - digits - in that case the program should print to the terminal: 'Numeric'
# -contains only letters - in that case the program should print to the terminal: 'Letters Only'
# -otherwise print to terminal: 'Mixed'

#Example of running the script:
#/Users/PythonBeginner/Lesson1$ python string_type.py
#Give me some input: Abc
#Letters Only
#/Users/PythonBeginner/Lesson1$ python string_type.py
#Give me some input: 4every1
#Mixed
#/Users/PythonBeginner/Lesson1$ python string_type.py
#Give me some input: 99
#Numeric

string = input("Give me some input: ")

if string.isnumeric():
    print("Numeric")
elif string.isalpha():
    print("Letters Only")
else:
    print("Mixed")
