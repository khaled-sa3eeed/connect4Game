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
