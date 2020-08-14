def sum(values):
    result = 0
    for value in values:
        result += value
    return result


def count(values, target=None):
    result = 0
    for value in values:
        if not target or value == target:
            result += 1
    return result


def mean(values):
    return sum(values) / count(values)


def modus(values):
    counts = {}
    for value in values:
        counts[value] = counts.setdefault(value, 0) + 1

    result = None
    for k, v in counts.items():
        if not result or result[1] < v:
            result = (k, v)
    return result[0]


def median(values):
    mid_point = len(values) // 2
    seq = sorted(values)
    if len(values) % 2 == 0:
        return (seq[mid_point] + seq[mid_point - 1]) / 2
    else:
        return seq[mid_point]


def main():
    data = [35, 14, 26, 48, 49, 26, 18,
            25, 16, 16, 39, 17, 10, 29]

    actions = {
        'SUM': sum,
        'COUNT': count,
        'MEAN': mean,
        'MODUS': modus,
        'MEDIAN': median
    }

    print("Hi we have the following dataset:\n" + str(data))
    while True:
        print('\nWhat do you want to calculate (type your choice, e.g. SUM or "q" to quit)?\n')
        action = input('| SUM | COUNT | MEAN | MODUS| MEDIAN |\n')

        if action.lower() == 'q':
            print('Good bye')
            break
        elif action.upper() not in actions:
            print('I cannot perform this action: ' + action)
            input('Press ENTER to continue')
            continue

        action = action.upper()
        if action == 'COUNT':
            target = int(input('Please enter a number you want to find:\n'))
            result = actions[action](data, target)
        else:
            result = actions[action](data)

        print('RESULT of ' + action.upper() + ': ' + str(result))
        input('Press ENTER to continue')


main()
