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
    row.insert(0, random.choice(customers))
    row1, row3 =  random.choice(products)
    row.insert(1, row1)
    row.insert(2, random.randrange(101))
    row.insert(3, row3)
    row.insert(4, round(row[2] * row[3], 2))
    return row

def generate_table(rows, header):
    dataset=[]
    dataset.append(header)
    for i in range(rows):
        dataset.append(generate_row(customers, products))
    return dataset



rows = read_row()
#print(generate_row(customers, products))
#final_table = generate_table(rows, header)
print(generate_table(rows, header))
