#Create a script split_nums.py that will:
# -ask the user for a number
# -split the given number in halves (e.g. 123456 -> split to 123 and 456, 12345 -> 12 and 345)
# -convert both halves into an integer
# -if both halves are an even integer, print: 'Success' - e.g. 12 and 34
# -if only the first part is even, print: 'First' - e.g. 12 and 345
# -if the second part is even, print: 'Second' - e.g. 123 and 456
# -if neither of the numbers is even print: 'Neither' - 123 and 455
# -if nothing has been entered (the user just hit Enter), print: 'No input provided'

#Example of running the script:
#Users/PythonBeginner/Lesson1$ python split_nums.py
#Please, give me a number: 35
#Neither
#/Users/PythonBeginner/Lesson1$ python split_nums.py
#Please, give me a number:
#No input provided

number = input("Please, give me a number:")
if not number:
    print("No input provided")
else:
    half = int(len(number))//2
    first, second = int(number[:half]), int(number[half:])
    if first%2 == 0 and second%2 == 0:
        print("Success")
    elif first%2 == 0 and second%2 != 0:
        print("First")
    elif first%2 != 0 and second%2 == 0:
        print("Second")
    else:
        print("Neiter")
