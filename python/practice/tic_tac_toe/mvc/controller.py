import tkinter as tk
from model import Model
from view import MainMenu, GameBoard


class Controller:

    def __init__(self, master):
        self.model = Model(1, 'Computer', 'Player')
        self.view = GameBoard(master)

        for child in self.view.buttons_frame.winfo_children():
            #print(self.buttons_frame.winfo_children()[8])
            child.config(command=lambda button=child: self.model.button_clicked(button))

        self.model.status_label = self.view.status_frame.winfo_children()[0]
        self.model.buttons_frame = self.view.board_frame.winfo_children()[0]
        self.model.game_start()


if __name__ == '__main__':
    root = tk.Tk()
    #root.withdraw()
    app = Controller(root)
    root.mainloop()
