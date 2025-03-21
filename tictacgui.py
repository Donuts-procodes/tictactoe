import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x450")
current_player = "X"
board = [" "] * 9
buttons = []
def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]  
    ]
    for condition in win_conditions:
        a, b, c = condition
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a] 
    return None

def on_click(index):
    global current_player

    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")  

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"🎉 Player {winner} wins!")
            reset_game()
            return

        if " " not in board:  
            messagebox.showinfo("Game Over", "It's a draw! 🤝")
            reset_game()
            return
        current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player
    board = [" "] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text=" ", state="normal")  
        
frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text=" ", font=("Arial", 20), height=2, width=5, command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Restart", font=("Arial", 15), command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()
