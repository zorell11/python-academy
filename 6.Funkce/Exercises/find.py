# Your task is to create a function my_find, that will imitate of a built-in string method .find() that will accept 2 argumentss:
#-any sequence we want to search through
#-and object, we want to find in the sequence
#The value returned from this function should be:
#The index at which the first occurrence of the searched object has been found
#or the value -1 if the object has not been found
#When you will use your function to search for a character in a string, keep in mind that lowercase character ("c") and uppercase character ("C") are two completely different characters for Python.



def my_find(lst, object):
    if object in lst:
        return lst.index(object)
    #else:
    return -1


print(my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}] , {'name': 'John'}))
print(my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}] , 'banana'))
