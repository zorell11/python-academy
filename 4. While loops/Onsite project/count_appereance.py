colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black' , 'red', 'green']

col_num = {}

while colors:
    color = colors.pop()
    col_num[color] = col_num.get(color,0) + 1

print(col_num)
