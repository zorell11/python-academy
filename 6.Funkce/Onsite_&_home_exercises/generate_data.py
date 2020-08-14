import random

customers = ['Bettison, Elnora',
             'Doro, Jeffrey',
             'Idalia, Craig',
             'Conyard, Phil',
             'Skupinski, Wilbert',
             'McShee, Glenn',
             'Pate, Ashley',
             'Woodison, Annie']

products = [('DROXIA', 33.86),('WRINKLESS PLUS',23.55),
            ('Claravis', 9.85), ('Nadolol', 12.35),
            ('Quinapril', 34.89), ('Doxycycline Hyclate', 23.43),
            ('Metolazone', 43.06), ('PAXIL', 14.78)]

header = ['Name','Item','Amount','Unit_Price', 'Total_Price']


def read_row():
    row = int(input("Zadaj pocet riadkov tabulky: "))
    return row


def generate_row(customers, products):
    row = []
    row[0] = random.choice(customers)
    row[1], row[3] = random.choice(products)
    row[2] = random.randrange(101)
    row[4] = row[2] * row[3]
    return row


rows = read_row()
print(generate_row(customers, products))
