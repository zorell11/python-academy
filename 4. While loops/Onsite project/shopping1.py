cart = []
repeat = True
# Infinite asking
while repeat:

    item = float(input('Enter the price: '))
    cart.append(item)

    answer = input('Press enter to continue or "q" to quit: ')

    if answer == 'q':
        repeat = False

i = 0
repeat = True
# Infinite listing
while repeat:

    index = i % len(cart)
    print(cart[index])

    answer = input('Press enter to continue or "q" to quit: ')

    if answer == 'q':
        repeat = False
    else:
        i = i + 1

i = 0
total_price = 0
# Calculating total sum
while i < len(cart):
    total_price = total_price + cart[i]
    i = i + 1

print('CART: ' + str(cart))
print('Total Price: ' + str(total_price))
