lst = []
lenght = 6
for i in range(1, lenght):
    lst.append(lenght * [i])
print(lst)

#for i in 'nigger':
#    lst.append(lenght * [i])
#print(lst)

for i in range(len(lst)):
    for j in range(len(lst)):
        print(lst[j][i], end='')
    print()


full_table =[]
for i in range(len(lst)):
    line = []
    for j in range(len(lst)):
        line.append(lst[j][i] )
    full_table.append(line)

print(full_table)

table_line = len(full_table) * '{:}\t'
table_out = []
for i in full_table:
    table_line = table_line.format(*i)
    table_out.append(table_line)
print('\n'.join(table_out))
