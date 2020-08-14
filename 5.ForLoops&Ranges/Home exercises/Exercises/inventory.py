data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED']]

total_price = 0
item_amount = 0
zentiva_item = 0
for row in data[1:]:
    total_price += row[2]
    item_amount += row[3]
    if row[4] == 'Zentiva':
        zentiva_item += row[3]

print("The total price of our inventory is:", total_price)
print('The total amount of items in our warehouse are:', item_amount)
print('From the company called Zentiva we have following amount of items:', zentiva_item)


d = {}
header = data[0][1:]

for row in data[1:]:
    id = row[0]
    d[id] = {}
#print(d)
    for index, item in enumerate(row[1:]):
        key = header[index]
        d[id].update({key : item})

print(d)
