# Create a function that accepts a list of strings and returns only those that are
# convertible to integer. Use try statement to solve this task. Also the input list
# can have any number of strings.
#>>> int_convert('Hello', '23','12', 'Bob', 'new')
#[23, 12]
#>>> int_convert('Hello', '23','12', 'Bob', 'new', '4312','5')
#[23, 12, 4312, 5]




def int_convert(*lst):
    intergers = []
    for i in lst:
        try:
            intergers.append(int(i))
        except:
            continue
    return intergers


print(int_convert('Hello', '23','12', 'Bob', 'new'))
print(int_convert('Hello', '23','12', 'Bob', 'new', '4312','5'))
