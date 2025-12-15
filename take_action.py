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