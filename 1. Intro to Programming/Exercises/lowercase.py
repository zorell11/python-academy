#Create a python script named change_case.py that will perform the following actions:

#ask the user for input
#transform all letters in the input into lowercase
#rint the resulting lowercase string
#Example of running the script in terminal:

#~/PythonBeginner/Lesson1 $ python change_case.py
#Enter something: Hello World
#Changed to lowercase: hello world


something = input("Enter something: ")
lowercase = something.lower()
print('Changed to lowercase:', lowercase)

print('Changed to lowercase:', input('Enter something: ').lower())
