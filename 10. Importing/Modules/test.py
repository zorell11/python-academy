_secret = 'password123'
print('Print is being executed')
var1 = 52
var2 = 53

def func(v1,v2):
    result = v1 * v2
    return result

__all__ = ['var2']


if __name__ == "__main__":
    print(func(var1,var2))
