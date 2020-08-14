
string = input("Give me some input: ")

if string.isnumeric():
    print('Numeric')
elif string.isalpha():
    print("Letters Only")
else:
    print("Mixed")
