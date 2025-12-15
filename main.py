arr = [0,0,0,0,0,0,0]
initial_grid=[[]]

class connect4Game:
    
    def __init__(self):

        global initial_grid
        initial_grid = [[" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "],
                             [" ", " ", " "," "," "," "," "]]
    #________________________________________________________________________________________________________
    def display_grid(self,state):
        print("\n 0   1   2   3   4   5   6")
        print()
        for row in range(6):
            for col in range(7):
                print(' ', state[row][col], ' ', sep='', end='')
                if col < 6:
                    print('|', end='')
            print()
            if row < 5:
                print('---+---+---+---+---+---+---', end='')
                print()
        print()
    #________________________________________________________________________________________________________

    def take_action(self, current_state, col):
      global arr
      new_state = [row[:] for row in current_state]
      player = self.current_player(current_state)

      for row in range(len(new_state)-1, -1, -1):
          if new_state[row][col] == " ":
              new_state[row][col] = player
              arr[col] += 1
              break

      return new_state, col
    #________________________________________________________________________________________________________
    def current_player(self, state):
        countR =0
        countY = 0
        for row in range(6):
            for col in range(7):
                symbol = state[row][col]
                if symbol == 'R':
                    countR += 1
                elif symbol == 'Y':
                    countY += 1
        if countR == countY:
            return 'R'
        return 'Y'


    #________________________________________________________________________________________________________
    def check_terminal(self, current_state, last_col):
      global arr

      piece_count = arr[last_col]
      if piece_count == 0:
          return "Not terminal"

      row = 6 - piece_count

      terminal = False
      full = False
      player = current_state[row][last_col]

      for r in range(3):
          if current_state[r][last_col] != " " and current_state[r][last_col] == current_state[r+1][last_col] and current_state[r][last_col] == current_state[r+2][last_col] and current_state[r][last_col] == current_state[r+3][last_col]:
              terminal = True
              player = current_state[r][last_col]
              break

      if not terminal:
        for j in range(4):
            if current_state[row][j] != " " and current_state[row][j] == current_state[row][j + 1] and current_state[row][j] == current_state[row][j + 2] and current_state[row][j] == current_state[row][j + 3]:
                  terminal = True
                  player = current_state[row][j]
                  break

      if not terminal:
          count1 = 0
          i_start, j_start = row, last_col

          # /
          i, j = i_start, j_start
          while i > 0 and j < 6 and current_state[i][j] == current_state[i - 1][j + 1] and current_state[i][j] != " ":
              count1 += 1
              i -= 1
              j += 1

          # /
          i, j = i_start, j_start
          while i < 5 and j > 0 and current_state[i][j] == current_state[i + 1][j - 1] and current_state[i][j] != " ":
              count1 += 1
              i += 1
              j -= 1

          if (count1 + 1) >= 4:
              terminal = True

      if not terminal:
          count2 = 0
          i_start, j_start = row, last_col

          #  \
          i, j = i_start, j_start
          while i > 0 and j > 0 and current_state[i][j] == current_state[i - 1][j - 1] and current_state[i][j] != " ":
              count2 += 1
              i -= 1
              j -= 1

          # \
          i, j = i_start, j_start
          while i < 5 and j < 6 and current_state[i][j] == current_state[i + 1][j + 1] and current_state[i][j] != " ":
              count2 += 1
              i += 1
              j += 1

          if (count2 + 1) >= 4:
              terminal = True


      empty_count = sum(row.count(" ") for row in current_state)

      if empty_count == 0:
          full = True

      if terminal:
          if player == "R":
              return 1
          elif player == "Y":
              return -1
      elif full:
          return 0
      else:
          return "Not terminal"
    #________________________________________________________________________________________________________
    
    def available_actions(self, current_state):
        actions = []
        for col in range(7):
                if current_state[0][col] == " ":
                    actions.append(col)

        return actions

    #________________________________________________________________________________________________________
    def MinMax(self, current_state, depth=5):
        if depth == 0:
            return 0

        utility_values = []
        available_cols = self.available_actions(current_state)

        if not available_cols:
            return 0

        player = self.current_player(current_state)

        for col in available_cols:
            global arr
            old_arr_value = arr[col]

            next_state, _ = self.take_action(current_state, col)

            result = self.check_terminal(next_state, col)

            if result != "Not terminal":
                score = result
            else:
                score = self.MinMax(next_state, depth - 1)

            arr[col] = old_arr_value

            utility_values.append(score)

        if player == "R":
            return max(utility_values)
        else:
            return min(utility_values)

    #________________________________________________________________________________________________________
    def human_play(self, current_state):

        player = self.current_player(current_state)
        print(f"Your turn, you are playing with {player}")

        available_cols = self.available_actions(current_state)
        while True:
          try:
              col = int(input(f"Choose your column {available_cols}: "))
              if col in available_cols:
                  break
              else:
                  print("Invalid column, try again.")
          except ValueError:
              print("Enter a valid integer column.")

        new_state, last_col = self.take_action(current_state, col)
        self.display_grid(new_state)
        return new_state,last_col


    #________________________________________________________________________________________________________
    def computer_play(self, current_state):
      player = self.current_player(current_state)
      print(f"Computer turn, he is playing with {player}")

      available_cols = self.available_actions(current_state)

      best_col = None
      best_score = None

      for col in available_cols:
          global arr
          old_arr_value = arr[col]

          next_state, _ = self.take_action(current_state, col)
          score = self.MinMax(next_state)

          arr[col] = old_arr_value

          if player == "R":
              if best_score is None or score > best_score:
                  best_score = score
                  best_col = col
          else:
              if best_score is None or score < best_score:
                  best_score = score
                  best_col = col

      print(f"Computer decided to play in column {best_col}")

      new_state, last_col = self.take_action(current_state, best_col)
      self.display_grid(new_state)
      return new_state, last_col

#________________________________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________________________________

# Testing connect 4 game
    def play_game(self):
        global initial_grid
        self.__init__()
        self.display_grid(initial_grid)

        global arr
        arr = [0, 0, 0, 0, 0, 0, 0]

        current_turn = "human"
        while True:
            if current_turn == "human":
                initial_grid, last_col = self.human_play(initial_grid)
                current_turn = "computer"
            else:
                initial_grid, last_col = self.computer_play(initial_grid)
                current_turn = "human"

            result = self.check_terminal(initial_grid, last_col)
            if result != "Not terminal":
                if result == 1:
                    print("R wins!")
                elif result == -1:
                    print("Y wins!")
                elif result == 0:
                    print("It's a draw!")
                return

import tkinter as tk
from tkinter import messagebox

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


my_game = connect4Game()

root = tk.Tk()
gui = Connect4GUI(root, my_game)
root.mainloop()
