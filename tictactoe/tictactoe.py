

logo = '''
        88                                                              
  ,d    ""              ,d                            ,d                
  88                    88                            88                
MM88MMM 88  ,adPPYba, MM88MMM ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba,    ,adPPYba,
  88    88 a8"     ""   88    ""     `Y8 a8"     ""   88   a8"     "8a  a8P_____88
  88    88 8b           88    ,adPPPPP88 8b           88   8b       d8  8PP""""""" 
  88,   88 "8a,   ,aa   88,   88,    ,88 "8a,   ,aa   88,  "8a,   ,a8"  "8b,   ,aa
  "Y888 88  `"Ybbd8"'   "Y888 `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"YbbdP"'    `"Ybbd8"'
'''
x, o = 0, 0
board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]


def print_board(board):
    print("     A    B   C")
    for i in range(3):
        print(i + 1, end="    ")
        for j in range(3):
            if j == 2:
                print(f" {board[i][j]}", end='')
            else:
                print(f" {board[i][j]} |", end='')

        print(end='\n')
        if not i >= 2:
            print(" " * 3, end="")
            print("." * 14)


def position(number):
    col_dict = {
        "a": 0,
        "b": 1,
        "c": 2
    }
    p = number % 2
    player = ""
    if p == 0:
        player = "o"
    else:
        player = "x"
    while (True):
        player_row = int(input(f"Which row? player {player}: ")) - 1
        player_column = input(f"Which column? player {player}: ").lower()
        if player_row in [0, 1, 2] or player_column in col_dict:
            break

    if number % 2 != 0 and board[player_row][col_dict[player_column]] == "_":
        board[player_row][col_dict[player_column]] = "x"
    elif number % 2 == 0 and board[player_row][col_dict[player_column]] == "_":
        board[player_row][col_dict[player_column]] = "o"


def check(board):
    diag_a, diag_b, col = "", "", ""
    for i in range(3):
        if board[i] == ['x', 'x', 'x']:
            return 10
        elif board[i] == ['o', 'o', '0']:
            return -10
        for j in range(3):
            col += board[j][i]
        if col == 'xxx':
            return 10
        elif col == 'ooo':
            return -10
        col = ""

        diag_a += board[i][i]
        diag_b += board[2 - i][i]
    if diag_a == "xxx" or diag_b == "xxx":
        return 10
    elif diag_a == 'ooo' or diag_b == 'ooo':
        return -10


def print_score(a, b):
    print(f"Score: {a}-{b}")


def start():
    global x, o
    counter = 0
    is_on = True
    while (is_on):

        print(logo)
        print_score(x, o)
        if check(board) == 10:
            x += 1

            print('win for x')
            print_score(x, o)
            break
        elif check(board) == -10:
            o += 1

            print('win for o')
            print_score(x, o)
            break
        counter += 1
        print_board(board)
        position(counter)


while (True):
    start()
    answer = input("Do you want to play again?(yes/no) ").lower()
    if answer == "no":
        break
    if answer == 'yes':
        board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]
