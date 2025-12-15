import tkinter as tk
from tkinter import messagebox
arr = [0,0,0,0,0,0,0]
initial_grid=[[]]
class Connect4GUI:
    def __init__(self, master, game):
        self.master = master
        self.master.title("Connect 4")

        self.game = game

        self.rows = 6
        self.cols = 7
        self.cell_size = 80

        self.width = self.cols * self.cell_size
        self.height = self.rows * self.cell_size

        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="blue")
        self.canvas.pack()

        # Restart button
        self.restart_btn = tk.Button(master, text="Restart", command=self.restart_game)
        self.restart_btn.pack(pady=5)

        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<Motion>", self.handle_motion)

        self.hover_col = None
        self.game_over = False

        self.draw_grid(initial_grid)

    # ------------------------------------------------
    def draw_grid(self, state):
        self.canvas.delete("all")

        for r in range(self.rows):
            for c in range(self.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill="#0055AA", outline="black", width=2
                )

                piece = state[r][c]
                color = "white"
                if piece == "R":
                    color = "red"
                elif piece == "Y":
                    color = "yellow"

                margin = 6
                self.canvas.create_oval(
                    x1 + margin, y1 + margin,
                    x2 - margin, y2 - margin,
                    fill=color, outline="black"
                )

        # Hover preview (red piece)
        if self.hover_col is not None and not self.game_over:
            c = self.hover_col
            x1 = c * self.cell_size
            y1 = 0
            x2 = x1 + self.cell_size
            y2 = self.cell_size

            margin = 6
            self.canvas.create_oval(
                x1 + margin, y1 + margin,
                x2 - margin, y2 - margin,
                fill="red", outline="black"
            )

    # ------------------------------------------------
    def handle_motion(self, event):
        if self.game_over:
            return

        col = event.x // self.cell_size
        if 0 <= col < self.cols and arr[col] < self.rows:
            self.hover_col = col
        else:
            self.hover_col = None

        self.draw_grid(initial_grid)

    # ------------------------------------------------
    def handle_click(self, event):
        if self.game_over:
            return

        col = event.x // self.cell_size
        if col < 0 or col >= self.cols or arr[col] >= self.rows:
            return

        self.human_move(col)

    # ------------------------------------------------
    def human_move(self, col):
        global initial_grid

        initial_grid, last_col = self.game.take_action(initial_grid, col)
        self.draw_grid(initial_grid)

        result = self.game.check_terminal(initial_grid, last_col)
        if result != "Not terminal":
            self.end_game(result)
            return

        self.master.after(400, self.computer_move)

    # ------------------------------------------------
    def computer_move(self):
        global initial_grid

        available_cols = self.game.available_actions(initial_grid)
        best_col = None
        best_score = None

        for col in available_cols:
            old = arr[col]
            next_state, _ = self.game.take_action(initial_grid, col)
            score = self.game.MinMax(next_state)
            arr[col] = old

            if best_score is None or score < best_score:
                best_score = score
                best_col = col

        initial_grid, last_col = self.game.take_action(initial_grid, best_col)
        self.draw_grid(initial_grid)

        result = self.game.check_terminal(initial_grid, last_col)
        if result != "Not terminal":
            self.end_game(result)

    # ------------------------------------------------
    def end_game(self, result):
        self.game_over = True
        self.hover_col = None

        if result == 1:
            msg = "Red (Human) Wins!"
        elif result == -1:
            msg = "Yellow (Computer) Wins!"
        else:
            msg = "Draw!"

        messagebox.showinfo("Game Over", msg)

    # ------------------------------------------------
    def restart_game(self):
        global initial_grid, arr

        initial_grid = [[" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "]]
        arr = [0,0,0,0,0,0,0]

