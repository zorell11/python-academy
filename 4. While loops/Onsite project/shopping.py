cart = []

repeat = True
while repeat:
    item = float(input('Enter the price: '))
    cart.append(item)

    answer = input('Press enter to continue or "q" to quit: ')

    if answer == 'q':
        repeat = False

repeat = True
while 

total_price = sum(cart)
print('Cart: ' + str(cart))
print('Total price is: ', total_price)
