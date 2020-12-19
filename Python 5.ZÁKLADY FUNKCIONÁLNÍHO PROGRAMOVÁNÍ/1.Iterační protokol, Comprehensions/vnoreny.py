import pprint

my_list = []
for x in 'abc':
    for y in 'def':
            my_list.append((x + y))

print(my_list)

my_list1 = [x+y for x in 'abc' for y in 'def']
print(my_list1)

matrix = [ ['#' for i in range(5)] for j in range(5)]

pprint.pprint(matrix)
