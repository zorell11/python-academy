from pprint import pprint as pp


grid = int(input("Grid Size: "))

############################
lst = list(range(grid))
print('[', end='')
for i in range(grid):
    print(str(lst) + ',',)
print(str(lst) + ']')
###########################

print()
print()
table = []
lst1 = list(range(grid))
for i in range(grid):
    table.append(lst1)
pp(table)
