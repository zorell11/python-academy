# our training table - in case we do not want to insert new
# rows and columns at the beginning
table = [['Name','Age','Email'],
         ['bob', '23', 'bob@abc.com'],
         ['ann', '25', 'ann@abc.com'],
         ['fred', '43', 'fred@abc.com']]

while True:

    print('-'*40)
    print('What do we want to do? Enter the number')
    print('''
    1-Create table | 2-Insert new row | 3-Insert new column |
    4-Update a cell | 5-Column Total | 6-Row Total |
    7-Print Table | 8-Export do List of Dicts |
    ''')
    selection = int(input('OPTION: '))
    print('-'*40)

    # user wants to create a table
    if selection == 1:
        table = []
        print('Enter header names separated by comma (e.g. Name,Age,Email)')
        header = input()
        table.append(header.split(','))

    # user wants to insert a new row
    elif selection == 2:
        where = int(input('ROW NUMBER: '))
        print('Enter the comma separated values (e.g. Bob,23,bob@abc.com): ')
        row = input().split(',')
        if  0 < where < len(table):
            table.insert(where, row)
        elif where >= len(table):
            table.append(row)

    # user wants to insert a new column
    elif selection == 3:
        col_name = input('COLUMN NAME: ')
        table[0].append(col_name)

        for i,row in enumerate(table[1:]):
            val = input('ENTER VALUE: ' + '|'.join(row) + '|')
            table[i+1].append(val)

    # user wants to update a cell
    elif selection == 4:
        row_num = int(input('ROW NUMBER: '))
        col_num = int(input('COLUMN NUMBER: '))
        if row_num in range(len(table)) and \
           col_num in range(len(table[0])):
           val = input('VALUE (current value: ' + table[row_num][col_num] + '):')
           table[row_num][col_num] = val
        else:
            print('No such row or column')

    # user wants to calculate the total sum of numbers in a column
    elif selection == 5:
        total = 0
        print('Select the column name')
        print('|'.join(table[0]))
        col_name = input()
        if col_name in table[0]:
            col_num = table[0].index(col_name)

            for row in table:
                if row[col_num].isnumeric():
                    total += int(row[col_num])
            print('COLUMN TOTAL FOR ' + col_name + ': ' +str(total))
        else:
            print('No column named ' + col_name)

    # user wants to calculate the total sum of numbers in a row
    elif selection == 6:
        total = 0
        print('Select the row number in range 1 to ' + str(len(table)-1) + '(excluding header)')
        row_num = int(input())

        if 0 < row_num < len(table):
            for cell in table[row_num]:
                if cell.isnumeric():
                    total += int(cell)
            print('ROW TOTAL FOR ROW #' + str(row_num) + ': ' + str(total))

    # user wants to print table content - can select which rows
    elif selection == 7:
        start = int(input('FROM ROW: '))
        end = int(input('TILL ROW: '))
        skip=1
        if input('Skip rows? [y/n]: ')=='y':
            skip = input('How many? (2 for every second etc.): ')

        start = 0 if start not in range(len(table)) else start
        end = len(table) if end>len(table) else end

        print('-'*40)
        for num in range(start,end,skip):
            row = table[num]
            print(' | '.join(row))

    # user wants to export the table (list of lists) into a dictionary
    elif selection == 8:
        data = []
        for row in table[1:]:
            d = {}
            for i,header in enumerate(table[0]):
                d[header] = row[i]
            data.append(d)

        print(data)


    print('-'*40)
    repeat = input('Press enter to repeat or q to quit: ')

    if repeat == 'q':
        break
