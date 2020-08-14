table = [['Name','Age','Email'],
         ['bob', '23', 'bob@abc.com'],
         ['ann', '25', 'ann@abc.com'],
         ['fred', '43', 'fred@abc.com']]


MENU = """
----------------------------------------
What do we want to do? Enter the number
    1-Create table | 2-Insert new row | 3-Insert new column |
    4-Update a cell | 5-Column Total | 6-Row Total |
    7-Print Table | 8-Export do List of Dicts |
    OPTION: """

INTERACRION = """
----------------------------------------
Press enter to repeat or q to quit: """
LINE = (41 * '-')
condition = True


while condition != 'q':
    option = int(input(MENU))
    print(LINE)

    if option == 1:
        table = []
        print("Enter header names separated by comma (e.g. Name,Age,Email)")
        header = input()
        table.append(header.split(','))
        print(table)

    elif option ==2:
        where = int(input('ROW NUMBER: '))
        print('Enter the comma separated values (e.g. Bob,23,bob@abc.com): ')
        row = input().split(',')
        if  0 < where < len(table):
            table.insert(where, row)
        else:
            table.insert(len(table), row)
        print(table)

    elif option == 3:
        column = input('COLUMN NAME: ')
        table[0].append(column)
        for i in range(1, len(table)):
            out_value = ''
            for j in range(len(table[i])):
                out_value = out_value + table[i][j] + ' | '
            new_value = input('ENTER VALUE: ' + out_value)
            table[i].append(new_value)
        print(table)

    elif option == 4:
        row = int(input('ROW NUMBER: '))
        column = int(input('COLUMN NUMBER: '))
        if row in range(len(table)) and column in range(len(table[0])):
            table[row][column] = input('VALUE (current value: ' + table[row][column] + '): ')
        else:
            print('No such row or column')

    elif option == 5:
        print('Select the column name')
        print(('|').join(table[0]))
        column_name = input()
        column_total = 0
        if column_name in table[0]:
            index = table[0].index(column_name)
            for i in range(1, len(table)):
                if table[i][index].isnumeric():
                    column_total += int(table[i][index])
            print('COLUMN TOTAL FOR', column_name, ':', column_total)
        else:
            print('No column name', column_name)

    elif option == 6:
        row = int(input('Select the row number in range 1 to ' + str(len(table[0])) + '(excluding header): '))
        row_total = 0
        if 0 < row < len(table):
            for i in table[row]:
                if i.isnumeric():
                    row_total += int(i)
            print(row_total)

    elif option == 7:
        fromm = int(input('FROM: '))
        till = int(input('TILL: ')) + 1
        if till > len(table):
            till = len(table)
        if fromm > len(table):
            fromm = len(table)
        print(LINE)
        for i in range(fromm, till):
            row = table[i]
            print('|'.join(row))
            #for j in table[i]:
            #    print(j, end ='|')
            #print()


    elif option == 8:
        d = {}
        export = []
        if len(table) < 1:
            print(export)
        else:
            for i in table[1:]:
                d.update(zip(table[0], table[1]))
                export.append(d)
        print(LINE)
        print(export)




    condition = input(INTERACRION)
