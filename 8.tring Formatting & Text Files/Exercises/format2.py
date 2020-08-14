person_data = {'name':'Bob', 'age' : 37}
formatted = 'My name is %(name)s , and I am %(age)d years old' % person_data
print(formatted)


person_data = {'name':'Bob', 'age' : 37}
formatted = 'My name is {name} , and I am {age} years old'.format(**person_data)
print(formatted)


person_data = ['Bob', 37]
formatted = 'My name is {0} , and I am {1} years old'.format(*person_data)
print(formatted)

person_data = ('Bob', [1,2,3,4])
formatted = 'My name is {0} , and I am {1} years old'.format(*person_data)
print(formatted)

a = {2: [24, 26, 28, 30, 32, 34, 36], 3: [24, 27, 30, 33, 36], 4: [24, 28, 32, 36], 5: [25, 30, 35], 6: [24, 30, 36], 7: [28, 35], 8: [24, 32], 9: [27, 36]}
for i in a.items():
    formatted = 'My name is {} , and I am {} years old'.format(*i)
    print(formatted)
