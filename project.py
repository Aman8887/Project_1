# Initialize the board
board = [" " for _ in range(9)]  # Empty cells

# Function to print the board
def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to handle player moves
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("That position is already taken. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Choose a number from 1 to 9.")
# Function to check for a winner
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (for a draw)
def check_draw():
    return " " not in board
def play_game():
    current_player = "X"
    while True:
        print_board()
        player_move(current_player)
        
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_draw():
            print_board()
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

play_game()
