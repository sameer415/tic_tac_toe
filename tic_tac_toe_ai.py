import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for positions in win_positions:
        if all(board[pos] == player for pos in positions):
            return True
    return False

def is_board_full(board):
    return all(cell != " " for cell in board)

def minimax(board, depth, is_maximizing):
    scores = {"X": 1, "O": -1, "tie": 0}
    if check_winner(board, "X"):
        return scores["X"]
    elif check_winner(board, "O"):
        return scores["O"]
    elif is_board_full(board):
        return scores["tie"]

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def tic_tac_toe():
    def button_click(index):
        if buttons[index]["text"] == " ":
            buttons[index]["text"] = "O"
            board[index] = "O"
            if check_winner(board, "O"):
                messagebox.showinfo("Tic-Tac-Toe", "player o wins!")
                reset_board()
            elif is_board_full(board):
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                reset_board()
            else:
                ai_move = best_move(board)
                buttons[ai_move]["text"] = "X"
                board[ai_move] = "X"
                if check_winner(board, "X"):
                    messagebox.showinfo("Tic-Tac-Toe", "Player X (AI) wins!")
                    reset_board()
                elif is_board_full(board):
                    messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                    reset_board()
    
    def reset_board():
        global board
        board = [" " for _ in range(9)]
        for button in buttons:
            button["text"] = " "

    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    buttons = []

    for i in range(9):
        button = tk.Button(root, text=" ", font='Helvetica 20', height=3, width=6, command=lambda i=i: button_click(i))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

    reset_board()
    root.mainloop()

if __name__ == "__main__":
    tic_tac_toe()
