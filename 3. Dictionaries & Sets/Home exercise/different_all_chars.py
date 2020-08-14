String03 = 'Bratislava'
String04 = 'Budapest'

diff = set(String03)^set(String04)
print('Different characters: ',diff)

all = set(String03) | set(String04)
print('All characters: ', all)
