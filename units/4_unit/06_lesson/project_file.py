def check_direction(x, y, x_move, y_move, board, checking):
    while y < len(board) and  x < len(board[y]):
        if board[y][x] != checking:
            return False
        x += x_move
        y += y_move
    return True

def check_side(board, side):
    # check horizontal
    won = False
    for i in range(len(board)):
        won = won or check_direction(0, i, 1, 0, board, side)
        won = won or check_direction(i, 0, 0, 1, board, side)
    won = won or check_direction(0, 0, 1, 1, board, side)
    won = won or check_direction(0, len(board)-1, 1, -1, board, side)
    return won

def tic_tac_toe_checker(board):
    right_side_won = check_side(board, 'x')
    if right_side_won:
        print("Xs won")
    else:
        left_side_won = check_side(board, "o")
        if left_side_won:
            print("Os won")
        else:
            print("No one won :(")

b1 = [['x', 'o', 'x'], ['x', 'o', 'o'], ['x', 'x', 'o']]
b2 = [['o', 'o', 'x'], ['o', 'o', 'o'], ['x', 'x', 'o']]
b3 = [['o', 'o', 'x'], ['o', 'x', 'o'], ['x', '0', 'x']]
b4 = [['o', 'x', 'x'], ['x', 'o', 'o'], ['x', 'o', 'x']]

tic_tac_toe_checker(b1)
tic_tac_toe_checker(b2)
tic_tac_toe_checker(b3)
tic_tac_toe_checker(b4)