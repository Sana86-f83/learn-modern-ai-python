def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # row
            return True
        if all([board[j][i] == player for j in range(3)]):  # column
            return True
    if all([board[i][i] == player for i in range(3)]):  # main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # anti-diagonal
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def tic_tac_toe():
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    current_player = "X"

    print("🎮 Welcome to Tic-Tac-Toe!")
    print("Player 1: X | Player 2: O")
    print_board(board)

    while True:
        move = input(f"Player {current_player}, enter a number (1-9) to make your move: ")

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("❌ Invalid input! Please enter a number from 1 to 9.")
            continue

        move = int(move)
        row, col = (move - 1) // 3, (move - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("❌ That spot is already taken! Choose another.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw(board):
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()
