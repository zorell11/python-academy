# Would it be possible to iterate over a tuple that consists of 3-item tuples? How should we do that?

data = (('Age',43,True),('Name','John',True),('Surname','Smith',False))

for i, j, k in data:
    print(i, j, k)
