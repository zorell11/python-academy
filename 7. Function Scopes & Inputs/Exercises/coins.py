# Create a function change_coins that will simulate a ticket machine in that it will return the least possible amount of coins.
#Our machine should work with coins of the following denominations: 1, 2, 5, 10, 20, 50
#For example, if the amount to be returned by the machine is 124, the returned coins should be:
# two 50, one 20, two 2
#And this is how it will look like in a terminal:

COINS = [1, 2, 5, 10, 20, 50]

def change_coins(number):
    change = {}
    for i in COINS[::-1]:
        if number >= i:
            a, number = divmod(number, i)
            change.update({i : a})
    return change


def main():
    print(change_coins(124))
    print(change_coins(0))
    print(change_coins(121))


main()
