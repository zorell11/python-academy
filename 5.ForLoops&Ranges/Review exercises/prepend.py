string = input("Please write here any sentence: ")

if string[:7]  == 'However':
    print(string)
else:
    print("However, " + string[0].lower() + string[1:])
