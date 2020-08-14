data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED']]


total_price = 0
total_amount = 0
zentiva = 0
for i in data[1:]:
    total_price += i[2]*i[3]
    total_amount += i[3]
    if i[4] == 'Zentiva':
        zentiva += i[3]



print('Total price: ',total_price)
print('Total amount: ', total_amount)
print('Items from Zentiva: ', zentiva)


##########

d = {}
header = data[0][1:]
for row in data[1:]:
    id = row[0]
    d[id] = {}
    for i,item in enumerate(row[1:]):
        key = header[i]
        d[id].update({key: item})
print("Database dictionary: ", d)
