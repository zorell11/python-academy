#!/usr/bin/env python3

lenght = int(input("add the lenght of the board: "))
char = input("add that will serve to fill in the black squares: ")

for i in range(lenght):
    for j in range(lenght):
        if (j+i)%2 == 0:
            print(char, end="")
        else:
            print(" ", end="")
    print()

#### engeto solution

size = 5
sym = ['#',' ']
desk = []

for row in range(size):
    line = []

    for cell in range(size):
        i = (row+cell) % len(sym)
        line.append(sym[i])

    desk.append(''.join(line))

print('\n'.join(desk))
