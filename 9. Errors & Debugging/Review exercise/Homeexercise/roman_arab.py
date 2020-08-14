
I =	1
V =	5
X =	10
L =	50
C =	100
D =	500
M =	1000



mapping  = {1 : 'I', 4 : 'IV', }

sorted(mapping, reverse=True)
result=''
arab = 3999
for num in sorted(mapping, reverse=True):
    roman = mapping[num]
    result += roamn * (arab // num)
    arab %= num

print(result)
