def read_points():
    start = int(input("START POINT:"))
    end = int(input("END POINT:"))
    return (start, end)

def count_divisable_numbers(start, end, DIVISORS):
    d = {}
    for i in DIVISORS:
        nums = []
        for j in range(start, end +2):
            if j % i ==0:
                nums.append(str(j))
        d[i] = ', '.join(nums)
    return d

def print_table(divisable_numbers):
    header = ['Divisor', 'Numbers Divided']
    c1 = len(header[0]) + 2
    c2 = max(len(header[1]), c2_lenght(divisable_numbers)) + 2
    line = ('=' * (c1 + c2 + 3))
    head = '|{0:^' + str(c1) + '}|{0:^' + str(c2) + '}|'
    head = head.format(*header)
    print(line)
    print(head)
    print(line)
    for i in divisable_numbers.items():
        table = '|{:^' + str(c1) + '}|{:^' + str(c2) + '}|'
        table = table.format(*i)
        print(table)
    print(line)


def c2_lenght(divisable_numbers):
    lst = []
    for i in divisable_numbers.values():
        #lst.append(len(str(i)))
        lst.append(len(i))
    return max(lst) -2



def main():
    START = 2
    END = 9
    DIVISORS = list(range(START, END + 1))
    start, end = read_points()
    divisable_numbers = count_divisable_numbers(start, end, DIVISORS)
    print_table(divisable_numbers)



main ()
