def sum_rec(num):
    if num == 0:
        print(num)
        return num
    print(num)
    return num + sum_rec(num-1)

print(sum_rec(5))
