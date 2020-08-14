
number = input("Please, give me a number: ")



if number == '':
    print('No input provided')

else:
    mid_point = len(number)//2
    first_half = int(number[:mid_point])
    second_half = int(number[mid_point:])

    if first_half % 2 == 0 and second_half % 2 == 0:
        print("Success")
    elif first_half % 2 == 0:
        print("First")
    elif second_half % 2 == 0:
        print("Second")
    else:
        print("Neither")
