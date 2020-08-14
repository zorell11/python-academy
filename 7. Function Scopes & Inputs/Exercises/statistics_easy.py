
def get_choice():
    print('''What do you want to calculate (type your choice , e.g. SUM or "q" to quit)?
| SUM | COUNT | MEAN | MODUS| MEDIAN |''')
    return input()

def sum_f(lst):
    return sum(lst)

def count_f(lst):
    num = int(input('Please enter a number you want to find: '))
    return lst.count(num)

def mean_f(lst):
    return sum(lst)/len(lst)

def modus_f(lst):
    mod = []
    max_occur = 0
    for i in set(lst):
        if lst.count(i) > max_occur:
            max_occur = lst.count(i)
            mod.append(i)
    #print(type(mod), ':'.join(mod))
    return mod

def median_f(lst):
    lst = sorted(lst)
    if len(lst)%2 == 0:
        med1 = lst[len(lst)//2]
        med2 = lst[len(lst)//2 +1]
        return (med1+med2)/2
    else:
        return lst[len(lst)//2]


def main():
    DATASET = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29]
    ACTIONS = {
        'SUM': sum_f,
        'COUNT': count_f,
        'MEAN': mean_f,
        'MODUS': modus_f,
        'MEDIAN': median_f
    }
    print('Hi we have the following dataset:', DATASET)

    while True:
        action = get_choice()
        if action.lower() == 'q':
            print('BYE')
            break
        if action.upper() not in ACTIONS:
            print('I cannot perform this action:', action)
            input('Press ENTER to continue')
            continue
        action = action.upper()
        result = ACTIONS[action](DATASET)
        print('RESULT of ' +  action.upper() + ': ' + str(result))
        input('Press ENTER to continue')

main()
