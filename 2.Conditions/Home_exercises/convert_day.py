DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day = input("Please enter the number of the day: ")

if day.isnumeric():
    print(DAYS[int(day)-1])
elif day == "":
    print("No input provided")
else:
    print("Enter only numbers, please")


##########

if not day:
    print("No input provided")
elif day not in ['1', '2', '3', '4', '5', '6', '7']:
    print('Enter only numbers between 1 and 7, please')
else:
    print(DAYS[int(day)-1])
