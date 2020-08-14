def message(guess):
    if guess <= 10:
        return 'amazing'
    elif 10 < guess <= 30:
        return 'average'
    elif 30 < guess <= 60:
        return 'not so good'
    elif guess > 60:
        return 'awful :D '

a = int(input("add number: "))
print(type(a))
input()
print(message(a))
