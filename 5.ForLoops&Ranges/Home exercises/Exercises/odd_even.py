# Write a Python program that will prompt user for a number and then will determine, whether the number is odd or even. You should use ternary operator to solve this task.
# Example of running the task:
#$ python3 odd_even.py
#Please, enter a number: 35
#ODD
#$ python3 odd_even.py
#Please, enter a number: 36
#EVEN

number = int(input('Please, enter a number: '))
output = 'EVEN' if number%2==0 else 'ODD'
print(output)

print('EVEN' if int(input('Please, enter a number: '))%2==0 else 'ODD')
