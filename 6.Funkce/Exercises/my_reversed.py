# Your task is to create a function that will imitate the built-in function reversed().
# It will take any sequence as an input and will return a list of items from the original sequence
# in reversed order.



def my_reversed(lst):
    return list(lst[::-1])

print(my_reversed(range(10)))
print(my_reversed(['New', 'Years', 'Eve']))
print(my_reversed('Hello World'))
