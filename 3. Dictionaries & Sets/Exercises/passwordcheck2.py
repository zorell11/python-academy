# We have this dictionary:
#data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}
#In this task, we will try to verify if the user enters a password that belongs to his account.
#The output should looks like:
#~/PythonBeginner/Lesson3 $ python verify.py
#Please enter username: Mark
#Please enter password: 1234
#ermission granted

#If the password will be type incorrectly or is incorrect in general:
#~/PythonBeginner/Lesson3 $ python verify.py
#Please enter username: Mark
#Please enter password: 444
#Password or username is wrong

data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}

username = input('Please enter username: ')
password = input('Please enter password: ')

#if username in list(data.keys()) and data[username] == password:
#    print('Permission granted')
#else:
#    print('Password or username is wrong')

print('Permission granted') if (username in list(data.keys()) and data[username] == password) else print('Password or username is wrong')
