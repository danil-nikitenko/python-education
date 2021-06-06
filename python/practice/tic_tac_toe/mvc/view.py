import tkinter as tk


class MainMenu:

    def __init__(self, master):
        self.root = master
        self.root.geometry('200x400+860+250')
        self.root.resizable(False, False)
        self.root.title('Tic tac toe')

        self.label_menu = tk.Label(self.root, text='Main Menu', font='Arial, 24')
        self.button_play_single = tk.Button(self.root, text='Singleplayer', height=2, width=15)
        self.button_play_multi = tk.Button(self.root, text='Multiplayer', height=2, width=15)
        self.button_view_log = tk.Button(self.root, text='View log', height=2, width=15)
        self.button_clear_log = tk.Button(self.root, text='Clear log', height=2, width=15)
        self.button_exit = tk.Button(self.root, text='Exit', height=2, width=15)

        self.label_menu.grid(column=0, row=0, pady=10)
        self.button_play_single.grid(column=0, row=1, padx=26, pady=8)
        self.button_play_multi.grid(column=0, row=2, padx=26, pady=8)
        self.button_view_log.grid(column=0, row=3, padx=26, pady=8)
        self.button_clear_log.grid(column=0, row=4, padx=26, pady=8)
        self.button_exit.grid(column=0, row=5, padx=26, pady=8)


class GameBoard:

    def __init__(self, master):
        self.root = master
        self.root.geometry('450x500+620+200')
        self.root.resizable(False, False)
        self.root.title('Tic tac toe')

        menubar = tk.Menu(self.root)
        self.control_menu = tk.Menu(self.root, tearoff=0)
        self.control_menu.add_command(label="Restart", font='Arial, 14')
        self.control_menu.add_command(label="Exit", font='Arial, 14')
        menubar.add_cascade(label="Options", font='Arial, 14', menu=self.control_menu)

        self.status_frame = tk.Frame(self.root, bd=1, relief='raised')
        self.status_label = tk.Label(self.status_frame, height=4, text='Status Label', font='Arial, 14').pack()
        self.board_frame = tk.Frame(self.root, bd=1, relief='raised')
        self.buttons_frame = tk.Frame(self.board_frame)
        for i in range(3):
            for j in range(3):
                tk.Button(self.buttons_frame, font='Arial, 36',
                          height=2, width=3).grid(row=i, column=j, padx=5, pady=5)
        self.buttons_frame.pack()

        self.root.config(menu=menubar)
        self.board_frame.pack(side='bottom', fill='x')
        self.status_frame.pack(side='bottom', fill='x')

    def button_clicked(self, button):
        #button.config(text='X', fg='red')
        board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        i = 0
        for button in self.buttons_frame.winfo_children():
            board[i] = button['text']
            i += 1
        print(board)
        print(button['text'])

    @staticmethod
    def button_change_content(button, content):
        button.config(text=content)


# root = tk.Tk()
# app = GameBoard(root)
# root.mainloop()
