import math

# Display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check for winner
def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check for draw
def is_full(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

# Get available moves
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ['X', 'O']]

# Minimax algorithm
def minimax(board, is_maximizing, ai_player, human_player):
    if check_winner(board, ai_player):
        return 1
    if check_winner(board, human_player):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in get_empty_cells(board):
            board[i][j] = ai_player
            score = minimax(board, False, ai_player, human_player)
            board[i][j] = f"{3*i+j+1}"  # undo move
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in get_empty_cells(board):
            board[i][j] = human_player
            score = minimax(board, True, ai_player, human_player)
            board[i][j] = f"{3*i+j+1}"  # undo move
            best_score = min(best_score, score)
        return best_score

# AI Move
def ai_move(board, ai_player, human_player):
    best_score = -math.inf
    move = None
    for (i, j) in get_empty_cells(board):
        board[i][j] = ai_player
        score = minimax(board, False, ai_player, human_player)
        board[i][j] = f"{3*i+j+1}"
        if score > best_score:
            best_score = score
            move = (i, j)
    if move:
        board[move[0]][move[1]] = ai_player

# Main game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    human_player = input("Choose your symbol (X/O): ").upper()
    ai_player = 'O' if human_player == 'X' else 'X'

    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    print_board(board)

    current_player = 'X'

    while True:
        if current_player == human_player:
            move = int(input("Enter your move (1-9): ")) - 1
            i, j = divmod(move, 3)
            if board[i][j] in ['X', 'O']:
                print("Cell already taken. Try again.")
                continue
            board[i][j] = human_player
        else:
            print("AI is thinking...")
            ai_move(board, ai_player, human_player)

        print_board(board)

        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        current_player = ai_player if current_player == human_player else human_player

# Run the game
if __name__ == "__main__":
    play_game()
