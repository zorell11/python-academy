import sys, os
from pprint import pprint

modules = sys.modules
pprint(sys.modules)

for mod in modules:
    print(mod)

print('-' * os.get_terminal_size().columns)
print('\n'.join(sys.modules.keys()))
