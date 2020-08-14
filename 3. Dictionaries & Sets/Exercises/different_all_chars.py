string01 = 'Bratislava'
string02 = 'Budapest'

difference = set(string01) ^ set(string02)
print('Different characters:', difference)

all = set(string01) | set(string02)
print('All characters:', all)
