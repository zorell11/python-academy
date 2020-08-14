# greet the client

print('''Welcome to the DESTINATIO,
place where people plan their trips''')


# offer destinations
print('We can offer you the following destinations:')

print('''
1 - Prague  | 1000
2 - Wien    | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
''')

print('=' * 40)

DESTINATIONS = ['Prague', 'Wien','Brno','Svitavy','Zlin','Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]
DISCOUNT_25 = ['Svitavy', 'Ostrava']



selection = int(input("Please enter the destination number to select: "))
print('=' * 40)
print("REGISTRATION: ")
print('-' * 40)
print("In order to complete your reservations, please share few details about yourself with us.")
print('-' * 40)
name = input("NAME: ")
print('=' * 40)
surname = input("SURNAME: ")
print('=' * 40)
birth = input("YEAR of BIRTH: ")
print('=' * 40)
email = input("EMAIL: ")
print('=' * 40);
passwd = input("PASSWORD: ")
print('=' * 40);

destination = DESTINATIONS[selection - 1]
#price = PRICES[selection - 1] * 0.75
price = PRICES[selection -1]

print("Thanj you", name)
print('We have made your reservation to', destination)
print("The total price is", price )
