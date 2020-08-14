str1 = 'New York'
str2 = 'Yorkshire'

print("Strings are: ", str1 + "," + str2)

common = set(str1) & set(str2)
print('Common letters: ', common)


unique1 = set(str1) - set(str2)
unique2 = set(str2) - set(str1)
print("Unique to str1:", unique1)
print("Unique to str2:", unique2)

sym_diff = set(str1) ^ set(str2)
sym_diff2 = set(str2) ^ set(str1)
print("Symmetric difference:", sym_diff)
print("Symmetric difference2:", sym_diff2)

united = set(str1) | set(str2)
print("united:", united)
