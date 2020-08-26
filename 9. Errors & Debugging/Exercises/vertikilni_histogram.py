def vert_histogram(lst, num):
    table = []
    number = []
    for i in range(max(lst), 0, -1):
        number.append(str(i) + '|')
    table.append(number)
    for i in lst:
        graph = []
        for j in range(max(lst)):
            if i>j:
                graph.append(num * '*')
            else:
                graph.append(num * ' ')
        table.append(graph[::-1])
    return rotate(table)

def rotate(lst):
    full_table =[]
    for i in range(len(lst[0])):
        line = []
        for j in range(len(lst)):
            line.append(lst[j][i] )
        full_table.append(line)
    return full_table

def print_histogram(table):
    table_line = '{:>3}' +(len(table[0])-1) * '{:} '
    table_out = []
    for i in table:
        table_line1 = table_line.format(*i)
        table_out.append(table_line1)
    print('\n'.join(table_out))

def main():
    hist = vert_histogram([4, 5, 7, 9, 6, 3, 2], 4)
    print_histogram(hist)
    print()
    hist = vert_histogram([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    print_histogram(hist)

main()
