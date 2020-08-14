val = [21, 32, 43, 52, 54, 55, 58, 62, 76, 83]
#val = [1,2,3,4,5]

def median(values):
    mid_point = len(values)//2
    values = sorted(values)

    if len(values)%2 == 0:
        return (values[mid_point]+values[mid_point-1])/2

    else:
        return values[mid_point]

print(median(val))
