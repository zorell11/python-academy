file = open('test.txt')
print(file)
text = file.read()
print(text)
more_text = file.read()
print(more_text)
file.close()


file = open('test.txt', 'w')
file.write('This is the first line\nThis is the 2nd line')
file.close()

file = open('test.txt', 'a+')
file.write('This is the third line\nThis is the fourth line')
file.close()

file = open('test.txt')
a = 'true'
print('Showing the content of the file with realine() method:')
while a:
	a = file.readline()
	if a == '':
		a = False
	else:
		print(a, end='')
file.close()
print()

print('Showing the content of the file with realines() method:')
file = open('test.txt')
text = file.readlines()
print(text)
file.close()
