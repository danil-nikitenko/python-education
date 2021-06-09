"""
Model
"""
import random
import logging

logging.basicConfig(filename='victories.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


class Model:
    """
    Responsible for the game logic
    """
    def __init__(self, game_type, player1, player2):
        self.game_type = game_type
        self.players = {1: player1, 2: player2}
        self.markers = {1: 'X', 2: 'O'}
        self.current_player = 1
        self.score = {1: 0, 2: 0}
        self.turn_count = 0
        self.buttons_frame = None
        self.status_label = None
        logging.info('=====%s vs %s=====', self.players[1], self.players[2])

    def change_marker(self, button):
        """
        change_marker(button: tkinter.Button)

        Changes the board slot with the marker.
        """
        if self.current_player == 1:
            button.config(text='X', disabledforeground='sea green')
        else:
            button.config(text='O', disabledforeground='purple4')
        button['state'] = 'disable'

    def swap_turn(self):
        """
        swap_turn()

        Passes the turn to another player.
        """
        self.current_player = 1 if self.current_player == 2 else 2
        self.status_label.config(text=f'{self.players[self.current_player]}, your turn')

    def reset_game(self):
        """
        reset_game()

        Resets all necessary parameters before starting a new game.
        """
        self.turn_count = 0
        for button in self.buttons_frame.winfo_children():
            button.config(text='', bg='gainsboro')
            button['state'] = 'normal'
        self.game_start()

    def game_start(self):
        """
        game_start() -> None

        Responsible for starting the game.
        """
        self.current_player = random.randrange(1, 3)
        self.status_label.config(text=f'{self.players[self.current_player]}, your turn')
        if self.game_type == 1 and self.current_player == 1:
            button_number = self.minimax(self.get_board(), self.current_player)[0]
            self.button_clicked(self.buttons_frame.winfo_children()[button_number])

    def winner(self):
        """
        winner() -> int

        Returns winner id if the game is end.
        Otherwise returns 0.
        """
        buttons = self.buttons_frame.winfo_children()
        i = j = 0
        for _ in range(3):
            if buttons[i]['text'] == buttons[i + 1]['text'] == buttons[i + 2]['text'] ==\
                    self.markers[self.current_player]:
                buttons[i].config(bg='khaki')
                buttons[i + 1].config(bg='khaki')
                buttons[i + 2].config(bg='khaki')
                return self.current_player
            if buttons[j]['text'] == buttons[j + 3]['text'] == buttons[j + 6]['text'] == \
                    self.markers[self.current_player]:
                buttons[j].config(bg='khaki')
                buttons[j + 3].config(bg='khaki')
                buttons[j + 6].config(bg='khaki')
                return self.current_player
            i += 3
            j += 1
        if buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] == \
                self.markers[self.current_player]:
            buttons[0].config(bg='khaki')
            buttons[4].config(bg='khaki')
            buttons[8].config(bg='khaki')
            return self.current_player
        if buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] == \
                self.markers[self.current_player]:
            buttons[2].config(bg='khaki')
            buttons[4].config(bg='khaki')
            buttons[6].config(bg='khaki')
            return self.current_player
        return 0

    def button_clicked(self, button):
        """
        button_clicked(button: tkinter.Button) -> int

        Handles the button click event on the game board
        """
        self.turn_count += 1
        self.change_marker(button)
        if self.winner() == self.current_player:
            self.disable_buttons()
            if self.game_type == 1:
                self.status_label.config(text='You lose')
            else:
                self.status_label.config(text=f'Congratulations '
                                              f'{self.players[self.current_player]}, you won!')
            self.score[self.current_player] += 1
            logging.info('%s wins.', self.players[self.current_player])
            logging.info('Score: %s/%s.', self.score[1], self.score[2])
            return 0
        elif self.turn_count == 9:
            self.status_label.config(text='That is a tie')
            logging.info('A tie.')
            return 1
        self.swap_turn()
        if self.game_type == 1 and self.current_player == 1:
            self.disable_buttons()
            button_number = self.minimax(self.get_board(), self.current_player)[0]
            if self.button_clicked(self.buttons_frame.winfo_children()[button_number]) != 0:
                self.enable_buttons()
        return 2

    def minimax(self, new_board, new_player):
        """
        minimax(new_board: list, new_player: int) -> tuple

        Recursive function to control computer moves.
        """
        f_spots = self.free_spots(new_board)
        if self.minimax_winner(new_board) == 1:
            return 10
        if self.minimax_winner(new_board) == 2:
            return -10
        if not f_spots:
            return 0

        results = {}
        buffer = tuple(new_board)
        for i in f_spots:
            new_board[i] = self.markers[new_player]
            result = self.minimax(new_board, 1 if new_player == 2 else 2)
            results[i] = result[1] if isinstance(result, tuple) else result
            new_board = list(buffer)

        if new_player == 1:
            return max(results, key=results.get), max(list(results.values()))
        return min(results, key=results.get), min(list(results.values()))

    def get_board(self):
        """
        get_board() -> list

        Returns the game board state as a list with nine items.
        """
        board = []
        for button in self.buttons_frame.winfo_children():
            board.append(button['text'])
        return board

    def disable_buttons(self):
        """
        disable_buttons()

        Disables all not pressed buttons on the game board
        """
        for i in self.free_spots(self.get_board()):
            self.buttons_frame.winfo_children()[i]['state'] = 'disable'

    def enable_buttons(self):
        """
        enable_buttons()

        Enables all not pressed buttons on the game board
        """
        for i in self.free_spots(self.get_board()):
            self.buttons_frame.winfo_children()[i]['state'] = 'normal'

    @staticmethod
    def minimax_winner(brd):
        """
        minimax_winner(brd: list) -> int

        Returns winner id if the game is end or 0 otherwise.
        Used only by minimax method.
        """
        i = j = 0
        for _ in range(3):
            if brd[i] == brd[i + 1] == brd[i + 2] and brd[i]:
                return 1 if brd[i] == 'X' else 2
            if brd[j] == brd[j + 3] == brd[j + 6] and brd[j]:
                return 1 if brd[j] == 'X' else 2
            i += 3
            j += 1
        if brd[0] == brd[4] == brd[8] and brd[0]:
            return 1 if brd[0] == 'X' else 2
        if brd[2] == brd[4] == brd[6] and brd[2]:
            return 1 if brd[2] == 'X' else 2
        return 0

    @staticmethod
    def free_spots(board):
        """
        free_spots() -> list

        Returns the list of free spots on the board.
        """
        f_spots = []
        for i in range(len(board)):
            if board[i] not in ('X', 'O'):
                f_spots.append(i)
        return f_spots
