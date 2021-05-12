"""
A simple hangman game.
"""

#from tkinter import *
import tkinter as tk
import random
from PIL import Image, ImageTk

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
images = {
    0: './images/Hangman-0.png',
    1: './images/Hangman-1.png',
    2: './images/Hangman-2.png',
    3: './images/Hangman-3.png',
    4: './images/Hangman-4.png',
    5: './images/Hangman-5.png',
    6: './images/Hangman-6.png'
}


class Menu:
    """
    Menu class.

    Generates main menu of the game.
    """
    def __init__(self, master):
        self.root = master
        self.root.geometry('200x300+860+250')
        self.root.resizable(False, False)
        self.root.title('Hangman')
        self.new_game = None

        self.label_menu = tk.Label(self.root, text='Main Menu', font='Arial, 24')
        self.button_play = tk.Button(self.root, text='Play', height=3, width=15, command=self.play)
        self.button_exit = tk.Button(self.root, text='Exit', height=3, width=15, command=self.exit)
        self.label_menu.grid(column=0, row=0, pady=10)
        self.button_play.grid(column=0, row=1, padx=26, pady=20)
        self.button_exit.grid(column=0, row=2, padx=26, pady=20)

    def play(self):
        """
        play()

        Launches the game.
        """
        self.exit()
        self.root = tk.Tk()
        self.new_game = Game(self.root)
        self.root.mainloop()

    def exit(self):
        """
        exit()

        Closes the game.
        """
        self.root.destroy()


class Game:
    """
    Game class.

    Main class, controls all parts of the game.
    """
    def __init__(self, master):
        self._misses = 0
        self._word = ''
        self._coded_word = ''
        self._answer = ''
        self.root = master
        self.root.geometry('675x600+620+200')
        self.root.resizable(False, False)
        self.root.title('Hangman')

        self.field_frame = tk.Frame(self.root, height=300, width=600)
        self.img = ImageTk.PhotoImage(Image.open(images[0]))
        self.img_label = tk.Label(self.field_frame, image=self.img)
        self.word_label = tk.Label(self.field_frame, font='Arial 14')
        self.misses_label = tk.Label(self.field_frame, text='Misses: ', font='Arial 14')
        self.result_label = tk.Label(self.field_frame, text='Guess an animal', font='Arial 24')
        self.answer_label = tk.Label(self.field_frame, font='Arial 14', fg='#ff0000')
        self.print_field()

        self.button_frame = tk.Frame(self.root, height=164, width=600)
        self.print_buttons(self.button_frame)

        self.field_frame.pack(side='top', fill='both')
        self.button_frame.pack(side='bottom', fill='both', expand=1)
        self.result_label.place(relx=0.3, rely=0.1)
        self.answer_label.place(relx=0.6, rely=0.75)

    def print_field(self):
        """
        print_field()

        Prints the top of the playing field (image and words on the right).
        """
        # choose a random word from words
        self._word = random.choice(words)
        # variable to write the guessed letters
        self._answer = list(self.word_to_underscore(self._word))
        # variable consisting of underscore characters to display on the screen
        self._coded_word = self.word_to_underscore(self._word, 1)
        self.word_label['text'] = f'Word: {self._coded_word}'
        # load a picture
        self.img = ImageTk.PhotoImage(Image.open(images[self._misses]))
        self.img_label['image'] = self.img
        self.img_label.place(relx=0.3, rely=0.25)
        self.word_label.place(relx=0.6, rely=0.45)
        self.misses_label.place(relx=0.6, rely=0.6)

    def print_buttons(self, frame):
        """
        print_buttons(frame)

        Prints all buttons on the frame.
        """
        letters = 'a b c d e f g h i g k l m n o p q r s t u v w x y z'.split(' ')
        x_coord = 10
        # place buttons with letters in loops
        for letter in letters[:9]:
            button = tk.Button(frame, text=letter, height=1, width=1)
            button.config(command=lambda l=letter, btn=button: self.letter_button_clicked(l, btn))
            button.place(x=x_coord, y=40)
            x_coord += 77
        x_coord = 10
        for letter in letters[9:18]:
            button = tk.Button(frame, text=letter, height=1, width=1)
            button.config(command=lambda l=letter, btn=button: self.letter_button_clicked(l, btn))
            button.place(x=x_coord, y=80)
            x_coord += 77
        x_coord = 48
        for letter in letters[18:]:
            button = tk.Button(frame, text=letter, height=1, width=1)
            button.config(command=lambda l=letter, btn=button: self.letter_button_clicked(l, btn))
            button.place(x=x_coord, y=120)
            x_coord += 77
        button_exit = tk.Button(frame, text='Exit', height=3, width=12,
                                font='Arial 14', command=self.button_exit_clicked)
        button_restart = tk.Button(frame, text='Restart', height=3, width=12,
                                   font='Arial 14', command=self.button_restart_clicked)
        button_exit.place(x=65, y=180)
        button_restart.place(x=458, y=180)

    def letter_button_clicked(self, letter, button):
        """
        letter_button_clicked(letter, button)

        Called when a letter button is pressed.
        Checks if hidden word contains a letter.
        """
        # check if the game is over
        if self._misses < 6 and ''.join(self._answer) != self._word:
            button['state'] = 'disable'
            # check if hidden word contains a letter
            # and change the game state if so
            if letter in self._word:
                positions = [pos for pos, char in enumerate(self._word) if char == letter]
                new_coded_word = list(self._coded_word)
                for i in positions:
                    new_coded_word[i * 2] = letter.upper()
                    self._coded_word = ''.join(new_coded_word)
                    self._answer[i] = letter
            # if letter not in word add it to misses list and update a picture
            else:
                self._misses += 1
                self.misses_label['text'] += letter + ' '
                self.img = ImageTk.PhotoImage(Image.open(images[self._misses]))
                self.img_label['image'] = self.img
            # update word_label
            self.word_label['text'] = 'Word: ' + self._coded_word

            # check if player won or lost
            if ''.join(self._answer) == self._word:
                self.result_label['text'] = 'You win!!!'
                self.result_label.place(relx=0.4, rely=0.1)
            elif self._misses == 6:
                self.result_label['text'] = 'You are dead :('
                self.result_label.place(relx=0.33, rely=0.1)
                self.answer_label['text'] = f'Answer: {self._word}'

    def button_restart_clicked(self):
        """
        button_restart_clicked()

        Called when a restart button is pressed.
        Restarts the game.
        """
        # update all necessary parameters before starting new game
        self._misses = 0
        self.misses_label['text'] = 'Misses: '
        self.result_label['text'] = 'Guess an animal'
        self.answer_label['text'] = ''
        self.result_label.place(relx=0.3, rely=0.1)
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        self.print_buttons(self.button_frame)
        self.print_field()

    def button_exit_clicked(self):
        """
        button_exit_clicked()

        Called when an exit button is pressed.
        Closes the game.
        """
        self.root.destroy()

    @staticmethod
    def word_to_underscore(word, spaces=0):
        """
        word_to_underscore(word, spaces=0) -> str

        Replaces all characters in a string with underscores.
        Underscores will be separated by spaces if spaces argument not equal to 0.
        """
        u_word = word
        if spaces == 0:
            for i, letter in enumerate(word):
                u_word = u_word.replace(word[i], '_')
        else:
            for i, letter in enumerate(word):
                u_word = u_word.replace(word[i], '_ ')
        return u_word


root = tk.Tk()
app = Menu(root)
root.mainloop()
