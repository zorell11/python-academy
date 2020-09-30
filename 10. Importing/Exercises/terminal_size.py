import os

print('testing the terminal size')

term_size = os.get_terminal_size().columns
print('*' * term_size)
