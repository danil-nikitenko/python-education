"""
Controller
"""
import tkinter as tk
import tkinter.messagebox
from model import Model
from view import MainMenu, SingleplayerLoginScreen, MultiplayerLoginScreen, LogWindow, GameBoard


class Controller:
    """
    Controls model and view parts
    """
    def __init__(self, master):
        self.model = None
        self.view = MainMenu(master)
        self.view.button_play_single.config(command=self.button_singleplayer_clicked)
        self.view.button_play_multi.config(command=self.button_multiplayer_clicked)
        self.view.button_view_log.config(command=self.button_view_log_clicked)
        self.view.button_clear_log.config(command=self.button_clear_log_clicked)
        self.view.button_exit.config(command=self.button_exit_clicked)

    def button_singleplayer_clicked(self):
        """
        button_singleplayer_clicked()

        Handles the singleplayer button click in the main menu
        """
        self.view.root.destroy()
        master = tk.Tk()
        self.view = SingleplayerLoginScreen(master)
        self.view.ok_button.config(command=lambda: self.button_ok_clicked(
                                   1,
                                   'Computer',
                                   self.view.name_entry.get()))
        self.view.back_button.config(command=self.button_back_clicked)

    def button_multiplayer_clicked(self):
        """
        button_multiplayer_clicked()

        Handles the multiplayer button click in the main menu
        """
        self.view.root.destroy()
        master = tk.Tk()
        self.view = MultiplayerLoginScreen(master)
        self.view.ok_button.config(command=lambda: self.button_ok_clicked(
                                   2,
                                   self.view.name_player1_entry.get(),
                                   self.view.name_player2_entry.get()))
        self.view.back_button.config(command=self.button_back_clicked)

    def button_view_log_clicked(self):
        """
        button_view_log_clicked()

        Handles the view log button click in the main menu
        """
        self.view.root.destroy()
        master = tk.Tk()
        self.view = LogWindow(master)
        self.view.back_button.config(command=self.button_back_clicked)
        with open('victories.log') as file:
            self.view.text_box.insert('end', file.read())

    @staticmethod
    def button_clear_log_clicked():
        """
        button_clear_log_clicked()

        Handles the clear log button click in the main menu
        """
        with open('victories.log', 'w'):
            pass
        tkinter.messagebox.showinfo("Clear log", 'Log cleared')

    def button_exit_clicked(self):
        """
        button_exit_clicked()

        Handles the exit button click in the main menu
        """
        self.view.root.destroy()

    def button_ok_clicked(self, mode, player1, player2):
        """
        button_exit_clicked(mode: int, player1: str, player2: str)

        Handles the ok button click on the login screen
        """
        self.view.root.destroy()
        master = tk.Tk()
        self.view = GameBoard(master)
        self.view.control_menu.add_command(label="Restart", font='Arial, 14', command=self.restart)
        self.view.control_menu.add_command(label="Exit", font='Arial, 14', command=self.exit)

        if mode == 1:
            self.model = Model(1, player1, player2)
        else:
            self.model = Model(2, player1, player2)
        for child in self.view.buttons_frame.winfo_children():
            child.config(command=lambda button=child: self.model.button_clicked(button))
        self.model.status_label = self.view.status_frame.winfo_children()[0]
        self.model.buttons_frame = self.view.board_frame.winfo_children()[0]
        self.model.game_start()

    def button_back_clicked(self):
        """
        button_back_clicked()

        Handles the back button click on the login screen
        """
        self.view.root.destroy()
        master = tk.Tk()
        self.__init__(master)

    def restart(self):
        """
        restart()

        Handles the restart menu option on the game board
        """
        self.model.reset_game()

    def exit(self):
        """
        exit()

        Handles the exit menu option on the game board
        """
        self.view.root.destroy()
        master = tk.Tk()
        self.__init__(master)


if __name__ == '__main__':
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()
