my_str = 'while loops are more genEral'

while my_str:
    if my_str[0].isupper():
        print('I have found capital letter: ', my_str[0])
    my_str = my_str[1:]
