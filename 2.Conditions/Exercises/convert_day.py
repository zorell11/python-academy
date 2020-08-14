#Your task is to create a script called convert_day.py that will:
# -ask for a number between 1 to 7
# -return the name of corresponding weekday (1 - 'Monday', 2-'Tuesday', 3 - 'Wednesday', 4 - 'Thursday', 5 - 'Friday', 6 - 'Saturday', 7 - 'Sunday')
# -if no input has been provided (user hitting enter without typing anything), the program should print: 'No input provided'
# -if the input is not a number the program should print: 'Enter only numbers, please'

#Example of running the script:
#~/PythonBeginner/Lesson1$ python convert_day.py
#Please enter the number of the day: 3
#Wednesday
#~/PythonBeginner/Lesson1$ python convert_day.py
#Please enter the number of the day: abc
#Enter only numbers, please
#~/PythonBeginner/Lesson1$ python convert_day.py
#Please enter the number of the day:
#No input provided

number = input("Please enter the number of the day: ")
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if number.isdecimal() and (0 < int(number) < 8):
    print(WEEKDAYS[int(number) - 1])
elif number.isalpha():
    print("Enter only numbers, please.")
elif number =='':
    print("No input provided")


if not number:
    print("No input provided")
elif number not in ['1', '2', '3', '4', '5', '6', '7']:
    print("Enter on numbers between 1 to 7")
else:
    day = int(number) - 1
    print(WEEKDAYS[day])
