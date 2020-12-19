def factory(num):
    print('premenna num: {}'.format(num))

    def add_num(n):
        print('premenna n: {}'.format(n))
        return n + num
    return add_num


add_two = factory(2)
print(add_two(5))
