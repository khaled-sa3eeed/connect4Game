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
