input1 = ''
input2 = ''
cart = []

while input1 != 'q':
    price = input('Enter the price: ')
    cart.append(float(price))
    input1 = input('Press enter to continue or "q" to quit: ')

prem = 0
while input2 != 'q':
    print('Item no. ' + str(prem) + ': ' + str(cart[prem%len(cart)]))
    input2 = input('Press enter to continue or "q" to quit: ')
    prem += 1


print('CART: ', cart)
print('Total Price:', sum(cart))
