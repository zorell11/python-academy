#úkolem je vytvořit funkci, která umí z CSV souboru načíst sloupce do listu. Výstupem této funkce
#by měl být list, který bude obsahovat listy s obsahem sloupců.

import csv

def get_columns(file):
    f = open(file)
    reader = csv.reader(f)

    columns = {}
    for row in reader:
        for i, item in enumerate(row):
            columns[i] = columns.get(i, []) + [item]

    print(columns)
    columns1 = []
    for i in columns.values():
        columns1.append(i)
    print(columns1)

get_columns('employees.csv')
