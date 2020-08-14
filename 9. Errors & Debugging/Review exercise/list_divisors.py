
start = int(input("START POINT: "))
end = int(input("END POINT: "))

d = {}
for i in range(2,9):
    prem = []
    for j in range(start,end):
        if j % i == 0:
            prem.append(j)
    print(prem)
    print('| {0:^4} | {1:^15} |'.format(i, *prem))
    
