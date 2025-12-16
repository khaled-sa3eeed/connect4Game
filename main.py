import tkinter as tk
from globals_and_setup import connect4Game
from gui import Connect4GUI

if __name__ == "__main__":
    my_game = connect4Game() 
    root = tk.Tk()
    gui = Connect4GUI(root, my_game)

    root.mainloop()
