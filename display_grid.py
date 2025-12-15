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