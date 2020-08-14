String01 = 'Bratislava'
String02 = 'Budapest'

common = set(String01) & set(String02)
unique = set(String01) - set(String02)
print('Common characters: ', common)
print('Unique characters in String01: ', unique)
