# Your task is to create a script called dist.py. The program should ask for x and y coordinates
# for 2 points and calculate the distance between those 2 points. The output should be a float,
#therefore let's round the result to 2 decimal places.
# -The distance should be straight line between the two points.
# -The coordinates cannot be negative numbers.

#Example of running the script:
#/Users/PythonBeginner/Lesson1$ python dist.py
#Point A, X Coordinate: 234
#Point A, Y Coordinate: 34
#Point B, X Coordinate: 27
#Point B, Y Coordinate: 114
#The distance between the points A and B is 221.92
#You may want to look ak the:
#Euclidean distance,
#math libraries - method sqrt(),
#the built-in function round() and abs()

import math

AX = int(input("Point A, X Coordinate: "))
AY = int(input("Point A, Y Coordinate: "))
BX = int(input("Point B, X Coordinate: "))
BY = int(input("Point B, Y Coordinate: "))

A = abs(AX - BX)
B = abs(AY - BY)

distance = round(math.sqrt(A**2 + B**2), 2)
print("The distance between the points A and B is", distance)
