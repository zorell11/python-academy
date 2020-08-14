rows = int(input("Zadaj pocet riadkov: "))

if rows == 1:
    pascal = [1]
elif rows == 2:
    pascal = [[1],[1, 1]]
elif rows > 2:
    pascal = [[1],[1, 1]]
    for row in range(1, rows+1):
        pascal = []
        for element in range(1, rows+1):
