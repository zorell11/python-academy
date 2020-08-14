

def int_convert(*zoznam):
    lst = []
    for i in zoznam:
        try:
            lst.append(int(i))
        except (ValueError,TypeError):
            continue
    return lst


print(int_convert('Hello', '23','12', 'Bob', 'new'))
