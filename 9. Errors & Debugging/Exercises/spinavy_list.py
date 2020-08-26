
def sum_list(lst):
    sum = 0
    for i in lst:
        try:
            sum += float(i)
        except:
            continue

    return int(sum)

def main():
    test = [1, 'asda', {'zvire':'kocka'}, '3.0', 2.0, [], '\n', '4']

    print(sum_list(test))

main()
