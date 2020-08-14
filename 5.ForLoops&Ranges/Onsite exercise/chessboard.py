size = int(input("Add the chessboard size: "))

for i in range(size):
    for j in range(size):
        if (i+j)%2 == 0:
            print('#', end='')
        else:
            print(' ', end='')
    print()


sign = ['#', ' ']
desk = []
for r,row in enumerate(range(size)):
    line = []
    for c,cell in enumerate(range(size)):
        line.append(sign[(r+c)%len(sign)])
    desk.append(''.join(line))

print('\n'.join(desk))
