seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]

numbers = {}

for i in seq:
    numbers.setdefault(i, 0)
    numbers[i] += 1

print(numbers)

ordered_data = sorted(numbers, key=numbers.get, reverse=True)

col1_width = len(' Item ') + 2
col2_width = len(' Count ') + 2



print('Item'.ljust(col1_width) + '|' + 'Count'.center(col2_width))
print('#' * (col1_width + col2_width))
for category in ordered_data:
    print(str(category).ljust(col1_width) + '|' + str(numbers[category]).center(col2_width))
