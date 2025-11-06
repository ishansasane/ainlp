# Tic Tac Toe game in Python

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        print(f"Player {players[current_player]}'s turn")
        
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))
        except ValueError:
            print("Invalid input! Please enter numbers 0, 1, or 2.")
            continue
        
        if row not in [0,1,2] or col not in [0,1,2]:
            print("Invalid move! Row and column must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken!")
            continue
        
        board[row][col] = players[current_player]
        print_board(board)
        
        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break
        
        current_player = 1 - current_player  # switch player

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
