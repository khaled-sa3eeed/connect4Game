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