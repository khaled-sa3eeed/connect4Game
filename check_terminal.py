from globals_and_setup import arr
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
