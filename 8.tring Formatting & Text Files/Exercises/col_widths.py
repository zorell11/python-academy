table =[['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price'],
['Bettison, Elnora', 'Doxycycline Hyclate', 98, 23.43, 2296.14],
['McShee, Glenn', 'DROXIA', 27, 33.86, 914.22],
['Conyard, Phil', 'Nadolol', 44, 12.35, 543.4],
['Bettison, Elnora', 'Claravis', 91, 9.85, 896.35],
['Idalia, Craig', 'Nadolol', 83, 12.35, 1025.05],
['Woodison, Annie', 'Metolazone', 46, 43.06, 1980.76],
['Woodison, Annie', 'DROXIA', 50, 33.86, 1693.0],
['Skupinski, Wilbert', 'Nadolol', 60, 12.35, 741.0],
['Conyard, Phil', 'WRINKLESS PLUS', 49, 23.55, 1153.95],
['Bettison, Elnora', 'Doxycycline Hyclate', 59, 23.43, 1382.37],
['Skupinski, Wilbert', 'Metolazone', 51, 43.06, 2196.06],
['McShee, Glenn', 'Claravis', 1, 9.85, 9.85]]


def get_widths(table):
    width = [0] * len(table[0])
    for row in table:
        for i, column in enumerate(row):
            if len(str(column)) > width[i]:
                width[i] = len(str(column))

    return width

def print_widths_table(width):
    header = ['COLUMN', 'WIDTH']
    message = '| {:} | {:} |'.format(*header)
    print(message)
    for i, number in enumerate(width):
        body = '| {:^6} | {:^5} |'.format('COL ' + str(i+1), number)
        print(body)


def main():
    col_width = get_widths(table)
    print_widths_table(col_width)

main()
