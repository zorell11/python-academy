
table = [['Amount1','Amount2', 'Amount3'],
         [  321,       43,       432],
         [ 3213,       42,       482],
         [  543,        38,      232]]

def row_tables(table):
    solution = []
    for i in table[1:]:
        solution.append(sum(i))
    return solution

print(row_tables(table))

def row_tables_list_comprehension(table):
    return [sum(i) for i in table[1:]]

print(row_tables_list_comprehension(table))

def row_tables_map_solution(table):
    return map(sum, table[1:])

print(list(row_tables_map_solution(table)))


def row_totals1(table, *, header=True):
    if header:
        table = table[1:]

    return map(sum, table)

print(row_totals1(table))
