# Our task is to create a program that will take time input in 24 hours format and will convert it into english time format including PM and AM.
#Example of running the program:
#$ python3 convert_time.py
#Please enter your time: 17 : 35
#Converted to English: 5 : 35 PM

time = input("Please enter your time: ")

format = time.split(':')

hours = format[0] if int(format[0]) == 12 else int(format[0]) % 12
minutes = int(format[1])
if int(format[0]) > 11:
    hours12 = 'PM'
else:
    hours12 = 'AM'

print('Converted to English:', hours, ':', minutes, hours12 )
