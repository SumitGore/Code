import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("450x550")
        self.window.resizable(False, False)
        
        # Game variables
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        # Improved colors and styling
        self.bg_color = "#1a1a2e"
        self.button_color = "#16213e"
        self.button_hover = "#0f3460"
        self.text_color = "#eee"
        self.x_color = "#ff6b6b"
        self.o_color = "#4ecdc4"
        self.accent_color = "#feca57"
        
        self.window.configure(bg=self.bg_color)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title with better styling
        title_label = tk.Label(
            self.window,
            text="🎮 TIC TAC TOE 🎮",
            font=("Arial", 26, "bold"),
            bg=self.bg_color,
            fg=self.accent_color,
            pady=15
        )
        title_label.pack()
        
        # Current player display with better styling
        self.status_label = tk.Label(
            self.window,
            text="Player X's Turn",
            font=("Arial", 18, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            pady=10
        )
        self.status_label.pack()
        
        # Game board frame with padding
        self.board_frame = tk.Frame(
            self.window, 
            bg=self.bg_color,
            pady=20
        )
        self.board_frame.pack()
        
        # Create 3x3 grid of improved buttons
        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Arial", 28, "bold"),
                    width=4,
                    height=2,
                    bg=self.button_color,
                    fg=self.text_color,
                    activebackground=self.button_hover,
                    activeforeground=self.text_color,
                    relief="flat",
                    bd=0,
                    cursor="hand2",
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=3, pady=3)
                
                # Add hover effects
                button.bind("<Enter>", lambda e, btn=button: self.on_button_hover(btn, True))
                button.bind("<Leave>", lambda e, btn=button: self.on_button_hover(btn, False))
                
                button_row.append(button)
            self.buttons.append(button_row)
        
        # Control buttons frame with better spacing
        control_frame = tk.Frame(self.window, bg=self.bg_color, pady=20)
        control_frame.pack()
        
        # Improved Reset button
        self.reset_button = tk.Button(
            control_frame,
            text="🔄 New Game",
            font=("Arial", 14, "bold"),
            bg="#27ae60",
            fg="white",
            activebackground="#2ecc71",
            width=12,
            height=2,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.reset_game
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Add hover effect to reset button
        self.reset_button.bind("<Enter>", lambda e: self.reset_button.config(bg="#2ecc71"))
        self.reset_button.bind("<Leave>", lambda e: self.reset_button.config(bg="#27ae60"))
        
        # Improved Quit button
        self.quit_button = tk.Button(
            control_frame,
            text="❌ Quit",
            font=("Arial", 14, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            width=12,
            height=2,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.window.quit
        )
        self.quit_button.pack(side=tk.LEFT, padx=10)
        
        # Add hover effect to quit button
        self.quit_button.bind("<Enter>", lambda e: self.quit_button.config(bg="#c0392b"))
        self.quit_button.bind("<Leave>", lambda e: self.quit_button.config(bg="#e74c3c"))
        
        # Game mode frame with better styling
        mode_frame = tk.Frame(self.window, bg=self.bg_color, pady=15)
        mode_frame.pack()
        
        # Mode label
        mode_label = tk.Label(
            mode_frame,
            text="Game Mode:",
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        mode_label.pack()
        
        # Game mode selection with improved styling
        self.game_mode = tk.StringVar(value="player")
        
        radio_frame = tk.Frame(mode_frame, bg=self.bg_color, pady=10)
        radio_frame.pack()
        
        self.player_mode = tk.Radiobutton(
            radio_frame,
            text="👥 Player vs Player",
            variable=self.game_mode,
            value="player",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            selectcolor=self.button_color,
            activebackground=self.bg_color,
            activeforeground=self.accent_color,
            cursor="hand2",
            command=self.reset_game
        )
        self.player_mode.pack(side=tk.LEFT, padx=15)
        
        self.computer_mode = tk.Radiobutton(
            radio_frame,
            text="🤖 Player vs Computer",
            variable=self.game_mode,
            value="computer",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            selectcolor=self.button_color,
            activebackground=self.bg_color,
            activeforeground=self.accent_color,
            cursor="hand2",
            command=self.reset_game
        )
        self.computer_mode.pack(side=tk.LEFT, padx=15)
    
    def on_button_hover(self, button, is_entering):
        """Handle button hover effects"""
        if button['state'] != 'disabled':
            if is_entering:
                button.config(bg=self.button_hover)
            else:
                button.config(bg=self.button_color)
    
    def button_click(self, row, col):
        index = row * 3 + col
        
        # Check if button is already clicked or game is over
        if self.board[index] != "" or self.game_over:
            return
        
        # Make the move
        self.make_move(row, col, self.current_player)
        
        # Check for winner
        if self.check_winner():
            self.game_over = True
            winner = self.current_player
            self.highlight_winning_line()
            self.status_label.config(text=f"🎉 Player {winner} Wins! 🎉", fg=self.accent_color)
            self.window.after(100, lambda: messagebox.showinfo("Game Over", f"Player {winner} wins! 🎊"))
            return
        
        # Check for tie
        if self.check_tie():
            self.game_over = True
            self.status_label.config(text="🤝 It's a Tie! 🤝", fg=self.accent_color)
            self.window.after(100, lambda: messagebox.showinfo("Game Over", "It's a tie! 🤜🤛"))
            return
        
        # Switch player
        self.current_player = "O" if self.current_player == "X" else "X"
        
        # Computer move if in computer mode
        if self.game_mode.get() == "computer" and self.current_player == "O":
            self.status_label.config(text="🤖 Computer thinking...", fg="#ff9ff3")
            self.window.after(800, self.computer_move)  # Slightly longer delay
        else:
            player_symbol = "❌" if self.current_player == "X" else "⭕"
            self.status_label.config(text=f"{player_symbol} Player {self.current_player}'s Turn", fg=self.text_color)
    
    def make_move(self, row, col, player):
        index = row * 3 + col
        self.board[index] = player
        
        # Update button with improved styling
        color = self.x_color if player == "X" else self.o_color
        symbol = "✖" if player == "X" else "⭕"
        
        self.buttons[row][col].config(
            text=symbol, 
            fg=color, 
            bg=self.button_hover,
            state="disabled",
            cursor="arrow"
        )
    
    def highlight_winning_line(self):
        """Highlight the winning combination"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                for i in combo:
                    row, col = i // 3, i % 3
                    self.buttons[row][col].config(bg=self.accent_color, fg="#1a1a2e")
                break
    
    def computer_move(self):
        if self.game_over:
            return
        
        # Get available moves
        available_moves = [i for i in range(9) if self.board[i] == ""]
        
        if available_moves:
            # Simple AI: Try to win, then block, then random
            move = self.get_best_move()
            if move == -1:
                move = random.choice(available_moves)
            
            row, col = move // 3, move % 3
            self.make_move(row, col, "O")
            
            # Check for winner
            if self.check_winner():
                self.game_over = True
                self.highlight_winning_line()
                self.status_label.config(text="🤖 Computer Wins! 🤖", fg=self.o_color)
                self.window.after(100, lambda: messagebox.showinfo("Game Over", "Computer wins! 🤖"))
                return
            
            # Check for tie
            if self.check_tie():
                self.game_over = True
                self.status_label.config(text="🤝 It's a Tie! 🤝", fg=self.accent_color)
                self.window.after(100, lambda: messagebox.showinfo("Game Over", "It's a tie! 🤜🤛"))
                return
            
            # Switch back to player
            self.current_player = "X"
            self.status_label.config(text="❌ Player X's Turn", fg=self.text_color)
    
    def get_best_move(self):
        # Simple AI strategy (same as before)
        # 1. Try to win
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                if self.check_winner_for_player("O"):
                    self.board[i] = ""
                    return i
                self.board[i] = ""
        
        # 2. Block player from winning
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "X"
                if self.check_winner_for_player("X"):
                    self.board[i] = ""
                    return i
                self.board[i] = ""
        
        # 3. Take center if available
        if self.board[4] == "":
            return 4
        
        # 4. Take corners
        corners = [0, 2, 6, 8]
        for corner in corners:
            if self.board[corner] == "":
                return corner
        
        return -1
    
    def check_winner(self):
        return self.check_winner_for_player(self.current_player)
    
    def check_winner_for_player(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    
    def check_tie(self):
        return all(cell != "" for cell in self.board)
    
    def reset_game(self):
        # Reset game variables
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        
        # Reset buttons with improved styling
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    text="",
                    state="normal",
                    bg=self.button_color,
                    fg=self.text_color,
                    cursor="hand2"
                )
        
        # Reset status
        self.status_label.config(text="❌ Player X's Turn", fg=self.text_color)
    
    def run(self):
        self.window.mainloop()

# Create and run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
