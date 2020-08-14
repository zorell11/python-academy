# Pozdrav klienta
print('=' * 80)
print('''Welcome to the DESTINATIO,
place where people plan their trips''')
print('=' * 80)

# Nabídni mu destinaci
print('We can offer you the following destinations:')
print('-' * 80)
print('''
1 - Prague | 1000
2 - Wien | 1100
3 - Brno | 2000
4 - Svitavy | 1500
5 - Zlin | 2300
6 - Ostrava | 3400
''')
print('-' * 80)

# Získej vstup uživatele o destinaci
selection = int(input('Please enter the destination number to select: '))

# Přiřaď proměnným příslušná data
DESTINATIONS = ['Prague', 'Wien','Brno','Svitavy','Zlin','Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]
DISCOUNT_25 = ['Svitavy', 'Ostrava']

# Zkontroluj, zde byl vložen vhodný vstupsf

if 0 < selection < (len(DESTINATIONS) + 1):
    # Získej data z proměnných podle vstupu uživatele
    destination = DESTINATIONS[selection-1]
    price = PRICES[selection-1]
    print(destination)

    # Spočítej cenu a zkontroluj, zda je vhodný aplikovat slevu pro zvolenou destinaci
    if destination in DISCOUNT_25:
        price -= price*0.25
        print("Lucky you! You have just earned 25% discount for your destination -", destination)
        print("Press enter to continue")
        input()

# Začni registraci
    print("""
================================================================================
REGISTRATION:
--------------------------------------------------------------------------------
In order to complete your reservations, please share few details about yourself with us.
--------------------------------------------------------------------------------
""")

# Získej vstup uživatele o jeho osobních datech
    name = input('NAME: ')
    print('=' * 40)
    surname = input('SURNAME: ')
    print('=' * 40)
    birth_year = int(input('YEAR of BIRTH: '))
    print('=' * 40)
    email = input('EMAIL: ')
    print('=' * 40)
    password = input('PASSWORD: ')
    print('=' * 80)

# Zkotroluj, jestli je uživatel starší než 15 let
    actual_year = 2020
    if actual_year - birth_year >= 15:
        age = True
    else:
        age = False

# Zkontroluj, jestli email obsahuje zavináč - @
    if email.find('@') == -1:
        mail = False
    else:
        mail = True

# Zkontroluj, jestli heslo
# - má aspoň 8 znaků
# - nezačíná ani nekončí číslem
# - a obsahuje písmena i čísla
    if len(password)>=8 and not password[0].isnumeric() and not password[-1].isnumeric() and password.isalnum():
        passwd = True
    else:
        passwd = False

# Poděkuj uživateli použitím jeho jména a informuj jej/jí o provedení rezervace
    if age and mail and passwd:
        print("Thank you", name)
        print("We have made your reservation to:", destination)
        print("The total price is", price)
    else:
        print("""Registration failed. Following conditions should be done:
- age is minimum 15 years
- email must contain - @
- password must have at least 8 characters, cannot begin ans end with number and must contain latters and numbers.
""")

else:
    print("Wrong destination number. Choose between 1 and 6")
