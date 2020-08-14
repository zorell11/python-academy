text = 'zolcsi a'
#text = 'Today is a nice day on Australian beach.'
#text = 'The Czech Republic also known as Czechia, is a nation state in Central Europe bordered by Germany to the west, Austria to the south, Slovakia to the east and Poland to the northeast.[12] The Czech Republic covers an area of 78,866 square kilometres (30,450 sq mi) with mostly temperate continental climate and oceanic climate. It is a unitary parliamentary republic, has 10.5 million inhabitants and the capital and largest city is Prague, with over 1.2 million residents. The Czech Republic includes the historical territories of Bohemia, Moravia, and Czech Silesia.'

text = text.split()

lenghts = []
first_letters = []

for i in text:
    lenghts.append(len(i))
    first_letters.append(i[0])


output = ''

while first_letters:
    l = lenghts.pop(0)

    if l > len(first_letters):
        output = output + ''.join(first_letters)
        first_letters.clear()

    else:
        output = output + ''.join(first_letters[:l]) + ' '
        del first_letters[:l]

print(output)
