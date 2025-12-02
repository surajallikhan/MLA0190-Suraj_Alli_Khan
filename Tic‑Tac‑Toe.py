import math

PLAYER, AI = 'X', 'O'

def empty_cells(board):
    return [i for i, c in enumerate(board) if c == ' ']

def check_winner(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(b[i]==b[j]==b[k]==p for i,j,k in wins)

def terminal(board):
    return check_winner(board, PLAYER) or check_winner(board, AI) or not empty_cells(board)

def minimax_ttt(board, max_turn):
    if check_winner(board, AI):    return 1
    if check_winner(board, PLAYER):return -1
    if not empty_cells(board):     return 0
    if max_turn:
        best = -math.inf
        for i in empty_cells(board):
            board[i] = AI
            best = max(best, minimax_ttt(board, False))
            board[i] = ' '
        return best
    else:
        best = math.inf
        for i in empty_cells(board):
            board[i] = PLAYER
            best = min(best, minimax_ttt(board, True))
            board[i] = ' '
        return best

def best_move(board):
    best_val, move = -math.inf, None
    for i in empty_cells(board):
        board[i] = AI
        val = minimax_ttt(board, False)
        board[i] = ' '
        if val > best_val:
            best_val, move = val, i
    return move

def print_board(b):
    for i in range(0,9,3):
        print(b[i], b[i+1], b[i+2])
    print()

if __name__ == "__main__":
    board = [' ']*9
    while True:
        print_board(board)
        if terminal(board): break
        p = int(input("Your move (0-8): "))
        if board[p] != ' ': continue
        board[p] = PLAYER
        if terminal(board): break
        m = best_move(board)
        board[m] = AI
    print_board(board)
    if check_winner(board, PLAYER): print("You win")
    elif check_winner(board, AI):   print("AI wins")
    else:                            print("Draw")