import math

AX = int(input("Point A, X Coordinate: "))
AY = int(input("Point A, Y Coordinate: "))
BX = int(input("Point B, X Coordinate: "))
BY = int(input("Point B, Y Coordinate: "))

X = abs(AX - BX)
Y = abs(AY - BY)
print(X, Y)

distance = math.sqrt(X**2 + Y**2)
print("The distance between the points A and B is", round(distance,2))
