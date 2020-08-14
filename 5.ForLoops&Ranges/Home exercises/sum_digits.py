

#lst =  [123 , 345, 67]
lst = [1, 22, 321, 64221, 5657, 8321]
result = []
for row in lst:
    num = 0
    for i in str(row):
        num += int(i)
    result.append(num)
print(result)


result_while = []
while lst:
    num = str(lst[0])
    lst = lst[1:]
    result_while.append(0)

    while num:
        result_while[-1] += int(num[0])
        num = num[1:]

print(result_while)
