print("""
================================================================================
Welcome to the DESTINATIO,
place where people plan their trips
================================================================================
We can offer you the following destinations:
--------------------------------------------------------------------------------
1 - Prague  | 1000
2 - Wien    | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
--------------------------------------------------------------------------------

""")
selection = int(input("Please enter the destination number to select: "))
DESTINATIONS = [ 'Prague', 'Wien', 'Brno', 'Svitavy', 'Zlin', 'Ostrava']
PRICES = [ 1000, 1100, 2000, 1500, 2300, 3400]

destination = DESTINATIONS[selection - 1]
price = PRICES[selection - 1]


print("""
================================================================================
REGISTRATION:
--------------------------------------------------------------------------------
In order to complete your reservations, please share few details about yourself with us.
--------------------------------------------------------------------------------
""")
name = input("NAME: ")
print("=" * 41)
surname = input("SURNAME: ")
print("=" * 41)
birth = int(input("YEAR of BIRTH: "))
print("=" * 41)
email = input("EMAIL: ")
print("=" * 41)
password = input('PASSWORD: ')
print("=" * 60)

print("Thank you", name)
print("We have made your reservation to", destination)
print("The total price is", price)
