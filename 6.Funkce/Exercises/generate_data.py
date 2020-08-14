#Create a function that will generate a table containing the following headers:
# 'Name','Item','Amount','Unit_Price', 'Total_Price'
#The function should take only one input - number of rows, the generated table should have.
#The data should be generated from the following variables:
# -values from customers should randomly populate the column Name

# -values from products should randomly populate the columns Item - the first part of the tuple,
#  Unit_Price - second part of the tuple

# -values for the column Amount should be generated randomly from numbers in range 1 to 100 (including)
# -values for the column Total_Price should be calculated as the product of Amount and Unit_Price
#The resulting list could look like this:

#dataset = [ ['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price'],
#            ['Bettison, Elnora', 'Doxycycline Hyclate', 98, 23.43, 2296.14],
#            ['McShee, Glenn', 'DROXIA', 27, 33.86, 914.22],
#            ['Conyard, Phil', 'Nadolol', 44, 12.35, 543.4],
#            ['Bettison, Elnora', 'Claravis', 91, 9.85, 896.35],
#            ['Idalia, Craig', 'Nadolol', 83, 12.35, 1025.05],
#            ['Woodison, Annie', 'Metolazone', 46, 43.06, 1980.76],
##            ['Skupinski, Wilbert', 'Nadolol', 60, 12.35, 741.0],
#            ...
#Save the code in the file generate_data.py. You will use this module again for the homework exercise
#about Statistics (the advanced version) in the following lesson.

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


def generate(row):
    dataset = [header]
    for i in range(1, row +1):
        name = random.choice(customers)
        item, unit_price = random.choice(products)
        amount = random.randint(1, 100)
        total_price = unit_price * amount
        dataset.append([name, item, amount, unit_price, round(total_price, 2)])
    return dataset

print(generate(5))
table = generate(5)

for i in table:
    for j in i:
        print(j, end='  ')
    print()
