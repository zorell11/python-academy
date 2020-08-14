table = [['Name','Age','Email'],
         ['bob', '23', 'bob@abc.com'],
         ['ann', '25', 'ann@abc.com'],
         ['fred', '43', 'fred@abc.com']]



while True:
    print(40 * '-')
    print('''What do we want to do? Enter the number
    1-Create table | 2-Insert new row | 3-Insert new column |
    4-Update a cell | 5-Column Total | 6-Row Total |
    7-Print Table | 8-Export do List of Dicts |''')

    option = int(input('OPTION: '))
    print(40 * '-')


    if option == 1:
        table = []
        print("Enter header names separated by comma (e.g. Name,Age,Email)")
        header = input()
        table.append(header.split(','))
        print(table)

    elif option == 2:
        row = int(input("ROW NUMBER: "))
        print("Enter the comma separated values (e.g. Bob,23,bob@abc.com): ")
        content = input()
        table.insert(row-1, content.split(','))

    elif option == 3:
        table[0].append(input("COLUMN NAME: "))
        for i in range(1,len(table)):
            val = input('|'.join(table[i]) + '|')
            table[i].append(val)

    elif option == 4:
        row = int(input("ROW NUMBER: "))
        column = int(input("COLUMN NUMBER: "))


    elif option == 7:
        start = int(input("FROM ROW: "))
        end = int(input("TILL ROW: "))
        print(40 * '-')

        for num in range(start,end):
            row = table[num]
            print('|'.join(row))

    elif option == 8:
        data = []
        for header in table[1:]:
            dict = {}
            for i,row in enumerate(table[0]):
                dict[row] = header[i]
            date.append(dict)


    print(40 * '-')
    check = input("Press enter to repeat or q to quit: ")
    if check == 'q':
        exit()
