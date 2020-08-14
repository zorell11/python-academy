
LST = [['Name', 'Item', 'Amount', 'Unit_Price', 'Total_Price'],
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

def convert_items_to_string(lst):
    new_lst = []
    for i in lst:
        prem_lst = []
        for j in i:
            prem_lst.append(str(j))
            new_lst.append(prem_lst)
    return new_lst

def col_lenghts(new_lst):
    mod_list = list(zip(*new_lst))
    lenghts = []
    for i in mod_list:
        lenghts.append(len(max(i)))
    return lenghts

def print_table(width, header = ['COLUMN', 'WIDTH']):
    w1 = len(header[0]) + 2
    w2 = len(header[1]) + 2

    firstrow = '| {0:^'+ str(w1) + '} | {1:^'+ str(w2) + '} |'
    firstrow = firstrow.format(*header)
    print(firstrow)

    for num, j in enumerate(width, 1):
        row = '| {0:^'+ str(w1) + '} | {1:^'+ str(w2) + '} |'
        row = row.format('COL '+ str(num), j)
        print(row)

def main():
    lst1 = convert_items_to_string(LST)
    width = col_lenghts(lst1)
    print_table(width)

if __name__ == '__main__':
    main()
