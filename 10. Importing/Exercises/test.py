import test
var1 = 52
var2 = 53
print(__name__ + ' file is executed')
def func(v1,v2):
    result = v1 * v2
    return result

#print(func(var1, var2))
if __name__ == "__main__":
    print(func(var1,var2))
