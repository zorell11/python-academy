# Write a Python script that will ask the user to enter a number from which it will compute the result.
# The result should be the sum of numbers less than or equal to the input number, each raised to power
#of its value. Then the script should print the result to the terminal.
#For example:
# -if the user enters number 5, the program should compute the sum as: 1**1 + 2**2 + 3**3 + 4**4 + 5**5.
# -if the user enters 6, then it should be: 1**1 + 2**2 + 3**3 + 4**4 + 5**5 + 6**6
# ...and so on.
#Example of running the script:
#$ python3 sum_powers.py
#Please enter your number: 5
#The result is: 3413


number = int(input("Please enter your number: "))
result = 0
for i in range(1, number + 1):
    result += i**i
print('The result is: ', result)
