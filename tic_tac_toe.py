import math
import random

board = [' ' for _ in range(9)]

def print_board():
    numbered_board = [str(i) if board[i] == ' ' else board[i] for i in range(9)]
    for row in [numbered_board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

def winner(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def is_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if winner(board, 'O'):
        return 1
    elif winner(board, 'X'):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def player_move():
    move = -1
    while move not in range(9) or board[move] != ' ':
        try:
            move = int(input("Enter your move (0-8): "))
        except ValueError:
            pass
    return move

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print("Choose game mode: 1. Player vs Player  2. Player vs AI")
    mode = input("Enter 1 or 2: ")

    print_board()
    current_player = 'X'

    while not is_full(board) and not winner(board, 'X') and not winner(board, 'O'):
        if mode == '1' or (mode == '2' and current_player == 'X'):
            move = player_move()
        else:
            print("AI is making a move...")
            move = ai_move()

        board[move] = current_player
        print_board()

        if winner(board, current_player):
            print(f"Player {current_player} wins!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
