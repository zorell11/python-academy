data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED']]


def list_to_dict2(data):
    d = {}
    header = data[0][1:]
    for row in data[1:]:
        id = row[0]
        d[id] = {}
        for number,item in enumerate(row[1:]):
            d[id].update({header[number] : item})
    return d


def list_to_dict1(data):
    d = {}
    header = data[0]
    for number1,row in enumerate(data[1:], 1):
        d1 = {}
        for number,i in enumerate(row):
            d1.update({header[number]:i})
        d.update({number1: d1})
    return d



def total_price(data:list):
    total_price = 0
    for line in data[1:]:
        price = line[2] * line[3]
        total_price += price
    return total_price


def total_amount(data:list):
    amount = 0
    for line in data[1:]:
        amount += line[3]
    return amount


def zentiva_items(data:list):
    items = 0
    for i in data[1:]:
        if i[4] == 'Zentiva':
            items += i[3]
    return items



def print_to_screen(data):
    print('Total price: ', total_price(data))
    print('TOtal amount of items:', total_amount(data))
    print('Zentive items: ', zentiva_items(data))
    print("Database dictionary: ", list_to_dict1(data))
    print("Database dictionary: ", list_to_dict2(data))


def main():
    print_to_screen(data)


if __name__ == "__main__":
    main()
