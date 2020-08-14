day = input('Enter number of the day: ')

if not day:
    print("No input")
elif not day.isnumeric():
    print("provide only numbers")
else:
    print("The solutuon is:")
