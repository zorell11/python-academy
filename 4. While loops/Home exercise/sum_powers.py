number = int(input("Please enter your number: "))
sum = 0
while number:
    sum += number**number
    number -= 1

print("The result is: ", sum)
