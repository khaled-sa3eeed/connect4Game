
def available_actions(self, current_state):
        actions = []
        for col in range(7):
                if current_state[0][col] == " ":
                    actions.append(col)

        return actions
