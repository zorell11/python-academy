
def sum(values):
    result = 0
    for i in values:
        result +=i
    return result

def count(values, item):
    result = 0
    for value in values:
        if item == value:
            result += 1
    return result

def mean(values):
    return sum(values)/len(values)

def modus(values):
    result = {}
    for i in values:
        if i in result:
            result[i] +=1
        else:
            result.setdefault(i,1)
    return

def median(values):
    print("funkcia count")





def main():
    data = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]
    actions = {'SUM': sum, 'COUNT': count, 'MEAN': mean, 'MODUS': modus, 'MEDIAN': median}
    while True:

        print('What you want to calculate (select a number or "q" to quit)?')
        action = input("| SUM | COUNT | MEAN | MODUS| MEDIAN |\n")
        if action.lower() == 'q':
            print('Good Bye')
            exit()

        elif action.upper() not in actions:
            print('I cannot perform this action: ' + action)
            input('Press ENTER to continue')
            continue


        action = action.upper()

        if action == 'COUNT':
            number = int(input("Please enter a number you want to find:"))
            result = actions[action](data, number)
        else:
            result = actions[action](data)

        print('Result of', action, ':', result)



main()
