print('''
===========================
Welcome to Tic Tac Toe
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row



Let's start the game
''')

def print_board():
    print('------')
    for i in BOARD:
        print('{:1}|{:1}|{:1}'.format(*i))
        print('------')

def ask_user(player):
    value_ask_user = True
    while value_ask_user:
        try:
            move = int(input("Player {} | Please enter your move number: ".format(player)))
            row, coulumn = divmod(move-1, 3)
            if move == '\n' or move == ' ':
                print('Please enter numbers only.')
            elif BOARD[row][coulumn] != '':
                print("Grid {} is already used, please choose another one.".format(move))
            else:
                BOARD[row][coulumn] = player
                value_ask_user = False
        except ValueError:
            print('Please enter numbers only.')
        except IndexError:
            print('Please enter numbers from 1 to 9.')
        return row, coulumn

def check_row(place, player):
    parameters = ((1, 2), (1, -1), (-1, -2))
    for i in parameters:
        try:
            if BOARD[place[0]][place[1]] == BOARD[place[0]][place[1]+i[0]] == BOARD[place[0]][place[1]+i[1]]:
                print("Congratulations, the player {} WON!".format(player))
                return False
        except:
            pass
    return True


def check_coulumn(place, player):
    parameters = ((1, 2), (1, -1), (-1, -2))
    for i in parameters:
        try:
            if BOARD[place[0]][place[1]] == BOARD[place[0]+i[0]][place[1]] == BOARD[place[0]+i[1]][place[1]]:
                print("Congratulations, the player {} WON!".format(player))
                return False
        except:
            pass
    return True

def check_diag1(place, player):
    parameters = ((1, 2), (1, -1), (-1, -2) )
    for i in parameters:
        try:
            if BOARD[place[0]][place[1]] == BOARD[place[0]+i[0]][place[1] + i[0]] == BOARD[place[0]+i[1]][place[1]+i[1]]:
                print("Congratulations, the player {} WON!".format(player))
                return False
        except:
            pass
    return True

def check_diag2(place, player):
    parameters = ((1, 2), (1, -1), (-1, -2) )
    board = [BOARD[0][::-1], BOARD[1][::-1], BOARD[2][::-1]]
    print(board)
    for i in parameters:
        try:
            #print(board[place[0]][place[1]], board[place[0]+i[0]][place[1] + i[0]], board[place[0]+i[1]][place[1]+i[1]])
            if board[place[0]][place[1]] == board[place[0]+i[0]][place[1] + i[0]] == board[place[0]+i[1]][place[1]+i[1]]:
                print("Congratulations, the player {} WON!".format(player))
                return False
        except:
            pass
    return True


MARKS = 3
BOARD = [['', '', ''],
        ['', '', ''],
        ['', '', '']]

#BOARD = [['', '', '', ''],
#        ['', '', '', ''],
#        ['', '', '', ''],
#        ['', '', '', '']]


PLAYER_O = 'o'
PLAYER_X = 'x'


value = True
while value:
    print_board()
    print('=' * 45)
    grid_param_o = ask_user(PLAYER_O)
    if not check_row(grid_param_o, PLAYER_O) or not check_coulumn(grid_param_o, PLAYER_O):
        exit()
    check_diag1(grid_param_o, PLAYER_O)
    check_diag2(grid_param_o, PLAYER_O)
    print('=' * 45)
    print('=' * 45)
    print_board()

    grid_param_o = ask_user( PLAYER_X)
    if not check_row(grid_param_o, PLAYER_X) or not check_coulumn(grid_param_o, PLAYER_X):
        exit()
    print('=' * 45)
    print('=' * 45)
