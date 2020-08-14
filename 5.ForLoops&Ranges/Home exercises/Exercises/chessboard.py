size = int(input('Add the size of the chessboard: '))
for i in range(size):
    for j in range(size):
        if (i+j)%2== 0:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

print()
print()

symbol = ['*', ' ']
for column in range(size):
    for row in range(size):
        index = (column + row) %2
        print(symbol[index], end='')
    print()
