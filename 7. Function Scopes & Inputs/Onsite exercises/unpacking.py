def list_divisibles(start,stop,divisor):
    divisibles=[]
    for num in range(start,stop):
        if num % divisor == 0:
            divisibles.append(num)
    return divisibles

print(list_divisibles(3,10,3))
args = {'start':3, 'stop':10, 'divisor':3}
print(list_divisibles(**args))
args1=[3,10,3]
print(list_divisibles(*args1))
