
length = int(input("Zadaj sirku sachovnice: "))

sign = ['#', ' ']
board = []
for row in range(length):
    line = []
    for cell in range(length):
        i = (row+cell) % 2
        line.append(sign[i])
    board.append(''.join(line))
print('\n'.join(board))


#############################
def show_board(size):
    index = 0
    for row in range(size):
        print()
        for col in range(size):
            index += 1
            char = '#' if index % 2 == 1 else ' '
            print(char, end='')
    print()

show_board(5)
