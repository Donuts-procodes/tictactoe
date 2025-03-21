import os

def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]  
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tic_tac_toe():
    board = [" "] * 9 
    current_player = "X"

    for turn in range(9): 
        print_board(board)
        
        while True:
            try:
                move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
                if 0 <= move < 9 and board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Enter a valid number between 1-9.")

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            return

        current_player = "O" if current_player == "X" else "X" 

    print_board(board)
    print("It's a draw! 🤝")

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe! 🎮")
    while True:
        tic_tac_toe()
        if input("Play again? (Y/n): ").strip().lower() == "n":
            break
