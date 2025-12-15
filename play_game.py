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