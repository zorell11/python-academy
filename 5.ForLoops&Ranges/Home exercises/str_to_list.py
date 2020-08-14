
number = input("Hello, please write your numbers and press enter to confirm: ")
number1 = number.split(",")

result = []

for i in number1:
    i = int(i.strip())
    result.append(i)

print("List: ", result)
