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


class SingleplayerLoginScreen:

    def __init__(self, master):
        self.root = master
        self.root.geometry('300x120+800+300')
        self.root.resizable(False, False)
        self.root.title('Tic tac toe')

        self.message_label = tk.Label(self.root, text='Enter your name', font='Arial, 14')
        self.name_entry = tk.Entry(self.root, width=30)
        self.ok_button = tk.Button(self.root, text='OK', width=10)
        self.back_button = tk.Button(self.root, text='Back', width=10)

        self.name_entry.bind("<FocusIn>", lambda args: self.name_entry.delete('0', 'end'))

        self.message_label.place(relx=.5, rely=.1, anchor='c')
        self.name_entry.insert(0, 'Player')
        self.name_entry.place(relx=.5, rely=.35, anchor='c')
        #self.ok_button.place(relx=.5, rely=.7, anchor='c')
        self.ok_button.place(relx=.55, rely=.6)
        self.back_button.place(relx=.09, rely=.6)


class MultiplayerLoginScreen:

    def __init__(self, master):
        self.root = master
        self.root.geometry('300x150+800+300')
        self.root.resizable(False, False)
        self.root.title('Tic tac toe')

        self.message_label = tk.Label(self.root, text='Enter your names', font='Arial, 14')
        self.name_player1_entry = tk.Entry(self.root, width=30)
        self.name_player2_entry = tk.Entry(self.root, width=30)
        self.ok_button = tk.Button(self.root, text='OK', width=10)
        self.back_button = tk.Button(self.root, text='Back', width=10)

        self.name_player1_entry.bind("<FocusIn>", lambda args: self.name_player1_entry.delete('0', 'end'))
        self.name_player2_entry.bind("<FocusIn>", lambda args: self.name_player2_entry.delete('0', 'end'))

        self.message_label.place(relx=.5, rely=.1, anchor='c')
        self.name_player1_entry.insert(0, 'Player 1')
        self.name_player1_entry.place(relx=.5, rely=.3, anchor='c')
        self.name_player2_entry.insert(0, 'Player 2')
        self.name_player2_entry.place(relx=.5, rely=.5, anchor='c')
        self.ok_button.place(relx=.55, rely=.7)
        self.back_button.place(relx=.09, rely=.7)


class LogWindow:

    def __init__(self, master):
        self.root = master
        self.root.geometry('500x450+700+200')
        self.root.resizable(False, False)
        self.root.title('Log file')

        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side='right', fill='y')
        self.text_box = tk.Text(self.root, width=40, height=15, font='Arial, 14')
        self.back_button = tk.Button(self.root, text='Back', width=10)

        self.text_box.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_box.yview)

        self.text_box.pack(pady=20)
        self.back_button.pack()


class GameBoard:

    def __init__(self, master):
        self.root = master
        self.root.geometry('450x500+620+200')
        self.root.resizable(False, False)
        self.root.title('Tic tac toe')

        menubar = tk.Menu(self.root)
        self.control_menu = tk.Menu(self.root, tearoff=0)
        # self.control_menu.add_command(label="Restart", font='Arial, 14')
        # self.control_menu.add_command(label="Exit", font='Arial, 14')
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
# app = Log(root)
# root.mainloop()
