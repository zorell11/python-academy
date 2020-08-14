city = input('What city do you live in? ')
size = int(input('How many people live in your city? '))
how = 'big' if size > 1000 else 'small'
print('If there are %d living in %s, that it is %s city' %(size, city, how))


celsius = int(input('What is the current temperature?'))
fahrenheit = celsius * (9/5) + 32
print("That {} celsius degree is {} fahrenheit degree".format(celsius, fahrenheit))

n = input('Your First Name: ')
s = input('Your Surname: ')
greetinfs = 'Nice to meet you {name} {surname}'
print(greetinfs.format(surname=s, name=n))


n = input('Your First Name: ')
s = input('Your Surname: ')
greetings = 'Nice to meet you {2} {0}'
print(greetings.format(s, n, s))
