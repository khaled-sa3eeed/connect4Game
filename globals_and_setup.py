arr = [0, 0, 0, 0, 0, 0, 0]
initial_grid = [[" ", " ", " "," "," "," "," "],
                    [" ", " ", " "," "," "," "," "],
                    [" ", " ", " "," "," "," "," "],
                    [" ", " ", " "," "," "," "," "],
                    [" ", " ", " "," "," "," "," "],
                    [" ", " ", " "," "," "," "," "]]

class connect4Game:
    def __init__(self):
        from init import __init__ as initialize_game_func
        initialize_game_func(self)
    
    def display_grid(self, state):
        from display_grid import display_grid
        display_grid(self, state)

    def take_action(self, current_state, col):
        from take_action import take_action
        return take_action(self, current_state, col)
        
    def current_player(self, state):
        from current_player import current_player
        return current_player(self, state)

    def check_terminal(self, current_state, last_col):
        from check_terminal import check_terminal
        return check_terminal(self, current_state, last_col)

    def available_actions(self, current_state):
        from available_actions import available_actions
        return available_actions(self, current_state)
        
    def MinMax(self, current_state, depth=5):
        from MinMax import MinMax
        return MinMax(self, current_state, depth)

    def human_play(self, current_state):
        from human_play import human_play
        return human_play(self, current_state)

    def computer_play(self, current_state):
        from computer_play import computer_play
        return computer_play(self, current_state)

    def play_game(self):
        from play_game import play_game
        play_game(self)
