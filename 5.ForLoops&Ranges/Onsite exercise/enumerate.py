numbers = [321,45,32,12,54]

for index, number in enumerate(numbers, 1):
    if index % 2 == 0:
        print(number, ':', number**2)


>>> list(enumerate('For loops support iteration protocol'))
[(0, 'F'), (1, 'o'), (2, 'r'), (3, ' '), (4, 'l'), (5, 'o'), (6, 'o'), (7, 'p'), (8, 's'), (9, ' '), (10, 's'), (11, 'u'), (12, 'p'), (13, 'p'), (14, 'o'), (15, 'r'), (16, 't'), (17, ' '), (18, 'i'), (19, 't'), (20, 'e'), (21, 'r'), (22, 'a'), (23, 't'), (24, 'i'), (25, 'o'), (26, 'n'), (27, ' '), (28, 'p'), (29, 'r'), (30, 'o'), (31, 't'), (32, 'o'), (33, 'c'), (34, 'o'), (35, 'l')]
