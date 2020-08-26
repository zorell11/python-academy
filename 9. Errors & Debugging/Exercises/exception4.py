try:
    num = [1,2,3,4][4]
    print(num*4)
except:
    print('Zachytil jsem chybu.')
except IndexError:
    print('Zachytil jsem index error.')
finally:
    print('Konec')
