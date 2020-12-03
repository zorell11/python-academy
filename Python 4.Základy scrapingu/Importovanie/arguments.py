import sys


arguments = sys.argv[1:]
for i in arguments:
    f = open(i, 'a')
    f.write(40 * '=' + '\n')
    f.close()

print(arguments)
print( sys.platform)
print(sys.argv)
