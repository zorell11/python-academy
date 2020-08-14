table = [['Name','Age','Email'],
         ['bob', '23', 'bob@abc.com'],
         ['ann', '25', 'ann@abc.com'],
         ['fred', '43', 'fred@abc.com']]

print(table)

where = int(input('ROW NUMBER: '))
print('Enter the comma separated values (e.g. Bob,23,bob@abc.com): ')
row = input().split(',')
if  0 < where < len(table):
    table.insert(where, row)
else:
    table.insert(len(table), row)
print(table)


#########################
#print('Select the column name')
#print(('|').join(table[0]))
#column_name = input()
#column_total = 0
#if column_name in table[0]:
#    index = table[0].index(column_name)
#    for i in range(1, len(table)):
#        if table[i][index].isnumeric():
#            column_total += int(table[i][index])
#    print('COLUMN TOTAL FOR', column_name, ':', column_total)

#else:
#    print('No column name', column_name)


#########################
#row = int(input('Select the row number in range 1 to ' + str(len(table[0])) + '(excluding header): '))
#row_total = 0
#if 0 < row < len(table):
#    for i in table[row]:
#        if i.isnumeric():
#            row_total += int(i)
#    print(row_total)

#########################

#row = int(input('ROW NUMBER: '))
#column = int(input('COLUMN NUMBER: '))
#if row in range(len(table)) and column in range(len(table[0])):
#    table[row][column] = input('VALUE (current value: ' + table[row][column] + '): ')
#    print('No such row or column')
#table[row][column] = value

#print(table)


#########################
#column = input('COLUMN NAME: ')
#table[0].append(column)
#for i in range(1, len(table)):
#    out_value = ''
#    for j in range(len(table[i])):
#        out_value = out_value + table[i][j] + ' | '
#    new_value = input('ENTER VALUE: ' + out_value)
#    table[i].append(new_value)
#print(table)


#########################
#d = {}
#export = []
#if len(table) < 1:
#    print(export)
#else:
#    for i in table[1:]:
#        d.update(zip(table[0], table[1]))
#        export.append(d)

#print(export)
#########################


#fromm = int(input('FROM: '))
#till = int(input('TILL: ')) + 1
#if till > len(table):
#    till = len(table)
#if fromm > len(table):
#    fromm = len(table)
#for i in range(fromm, till):
##        print(j, end ='|')
#    print()
#########################
