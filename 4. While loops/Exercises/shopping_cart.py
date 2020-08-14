# Vytvoř prototyp nákupního košíku, který:
# -Získej od uživatele 3 ceny výrobku (číslo),
# -Přidej je do seznamu, který bude reprezentovat nákupní košík,
# -Spočítej celkovou cenu,
#= -ytiskni obsah nákupního košíku a celkovou cenu.
#Example of running the program:
#$ python3 main.py
#Enter the price (1/3): 23
#Enter the price (2/3): 12
#Enter the price (3/3): 54
#CART: [23.0, 12.0, 54.0]
#Total Price: 89.0

poc_vyrobkov = 3
cart = []
for i in range(1, poc_vyrobkov +1):
    item = float(input('Enter the price (' + str(i) + '/' + str(poc_vyrobkov) + '): '))
    cart.append(item)
print('CART:', cart)
print('Total Price: ', sum(cart))
