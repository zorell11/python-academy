def triangle(row):
    result = []
    for i,j in enumerate(range(1, row + 1)):
        result.append( j * '*' )
    print(result)

print(triangle(5))
