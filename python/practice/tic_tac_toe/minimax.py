"""
Minimax algorithm realisation.
"""
import logging
import random

logging.basicConfig(filename='victories.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

RED = '\033[91m'
BLUE = '\033[94m'
ENDC = '\033[0m'

MENU = """
Main menu
1. Play versus computer.
2. Play multiplayer.
3. View log.
4. CLear log.
5. Exit.
"""


class Board:
    """
    Class for board representation.
    """
    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __getitem__(self, item):
        return self.board[item]

    def __setitem__(self, key, value):
        self.board[key] = value

    def draw(self):
        """
        draw()

        Prints the board.
        """
        print(f'\n{self.board[0]} | {self.board[1]} | {self.board[2]}')
        print('---------')
        print(f'{self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('---------')
        print(f'{self.board[6]} | {self.board[7]} | {self.board[8]}')

    def change_marker(self, slot, marker):
        """
        change_marker(slot: tuple, marker: str)

        Changes the board slot with the marker.
        """
        if len(slot) == 1:
            self.board[slot[0]] = marker
        else:
            if slot[0] == 0:
                self.board[slot[1]] = marker
            elif slot[0] == 1:
                self.board[slot[1] + 3] = marker
            elif slot[0] == 2:
                self.board[slot[1] + 6] = marker

    def free_spots(self):
        """
        free_spots() -> list

        Returns the list of free spots on the board.
        """
        return list(filter(lambda spot: spot != f'{RED}X{ENDC}' and spot != f'{BLUE}O{ENDC}', self.board))

    def reset(self):
        """
        reset()

        Resets the board
        """
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


class Game:
    """
    Main game class.

    Handles game events.
    """
    def __init__(self, board):
        self.board = board
        self.markers = {1: f'{RED}X{ENDC}', 2: f'{BLUE}O{ENDC}'}
        self.players = {1: '', 2: ''}
        self.current_marker = 1
        self.current_player = 1
        self.score = {1: 0, 2: 0}

    def print_menu(self):
        """
        print_menu() -> int

        Responsible for main menu work.
        """
        print(MENU)
        while True:
            choice = input('Choose an option: ')
            if choice == '1':
                self.set_names_and_score(1)
                self.game_minimax()
                return 0
            if choice == '2':
                self.set_names_and_score(2)
                self.game_multiplayer()
                return 0
            elif choice == '3':
                self.print_log()
                print(MENU)
            elif choice == '4':
                self.clear_log()
            elif choice == '5':
                return 0

    def winner(self):
        """
        winner() -> int

        Returns winner id if the game is end.
        Otherwise returns 0.
        """
        i = j = 0
        for _ in range(3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                return self.current_player
            if self.board[j] == self.board[j + 3] == self.board[j + 6]:
                return self.current_player
            i += 3
            j += 1
        if self.board[0] == self.board[4] == self.board[8]:
            return self.current_player
        if self.board[2] == self.board[4] == self.board[6]:
            return self.current_player
        return 0

    def swap_turn(self):
        """
        swap_turn()

        Passes the turn to another player.
        """
        self.current_player = 1 if self.current_player == 2 else 2
        self.current_marker = 1 if self.current_marker == 2 else 2

    def set_names_and_score(self, key):
        """
        set_names_and_score()

        Sets names and score at the start of the game.
        """
        self.score[1] = self.score[2] = 0
        if key == 1:
            self.players[1] = 'Computer'
            self.players[2] = input('Enter your name: ')
        else:
            self.players[1] = input('Player 1, enter your name: ')
            self.players[2] = input('Player 2, enter your name: ')
        logging.info('=====%s vs %s=====', self.players[1], self.players[2])

    def reset_game(self):
        """
        reset_game()

        Resets all necessary parameters.
        """
        self.board.reset()
        self.current_player = 1
        self.current_marker = 1

    def game_multiplayer(self):
        """
        game_multiplayer()

        Controls the multiplayer game (player vs player).
        """
        self.board.draw()

        for _ in range(9):
            turn = input(f'\n{self.players[self.current_player]}, '
                         f'your turn, enter cell number or coordinates(e.g. 0,0): ')
            turn = tuple(int(x.strip()) for x in turn.split(','))
            self.board.change_marker(turn, self.markers[self.current_marker])
            self.board.draw()
            if self.winner() == self.current_player:
                print(f'\nCongratulations {self.players[self.current_player]}, you won!')
                self.score[self.current_player] += 1
                logging.info('%s wins.', self.players[self.current_player])
                logging.info('Score: %s/%s.', self.score[1], self.score[2])
                break
            self.swap_turn()
        if self.winner() == 0:
            print('\nThat is a tie.')
            logging.info('A tie.')
        if input('\nPlay one more game(1-yes, 2-no)?\n') == '1':
            self.reset_game()
            self.game_multiplayer()

    def game_minimax(self):
        """
        game_minimax()

        Controls the single player game (computer vs player).
        """
        self.current_player = random.randrange(1, 3)

        for _ in range(9):
            if self.current_player == 1:
                print('\nComputer turn:')
                self.board.change_marker((self.minimax(self.board, self.current_player)[0],),
                                         self.markers[self.current_player])
            else:
                self.board.draw()
                turn = input(f'\n{self.players[self.current_player]}, '
                             f'your turn, enter cell number or coordinates(e.g. 0,0): ')
                turn = tuple(int(x.strip()) for x in turn.split(','))
                self.board.change_marker(turn, self.markers[self.current_player])
            if self.winner() == 1:
                self.board.draw()
                print(f'\nYou lose')
                self.score[self.current_player] += 1
                logging.info('Computer won.')
                logging.info('Score: %s/%s.', self.score[1], self.score[2])
                break
            self.swap_turn()
        if self.winner() == 0:
            self.board.draw()
            print('\nThat is a tie.')
            logging.info('A tie.')
        if input('\nPlay one more game(1-yes, 2-no)?\n') == '1':
            self.reset_game()
            self.game_minimax()

    def minimax(self, new_board, new_player):
        """
        minimax(new_board: Board, new_player: int) -> tuple

        Recursive function to control computer moves.
        """
        f_spots = new_board.free_spots()
        if self.minimax_winner(new_board) == 1:
            return 10
        if self.minimax_winner(new_board) == 2:
            return -10
        if not f_spots:
            return 0

        results = {}
        buffer = tuple(new_board.board)
        for i in f_spots:
            new_board[i] = self.markers[new_player]
            result = self.minimax(new_board, 1 if new_player == 2 else 2)
            results[i] = result[1] if isinstance(result, tuple) else result
            new_board.board = list(buffer)

        if new_player == 1:
            return max(results, key=results.get), max(list(results.values()))
        return min(results, key=results.get), min(list(results.values()))

    @staticmethod
    def minimax_winner(brd):
        """
        minimax_winner(brd: Board) -> int

        Returns winner id if the game is end or 0 otherwise.
        Used only by minimax method.
        """
        i = j = 0
        for _ in range(3):
            if brd[i] == brd[i + 1] == brd[i + 2]:
                return 1 if brd[i] == f'{RED}X{ENDC}' else 2
            if brd[j] == brd[j + 3] == brd[j + 6]:
                return 1 if brd[j] == f'{RED}X{ENDC}' else 2
            i += 3
            j += 1
        if brd[0] == brd[4] == brd[8]:
            return 1 if brd[0] == f'{RED}X{ENDC}' else 2
        if brd[2] == brd[4] == brd[6]:
            return 1 if brd[2] == f'{RED}X{ENDC}' else 2
        return 0

    @staticmethod
    def clear_log():
        """
        clear_log()

        Clears file with log victories.
        """
        with open('victories.log', 'w'):
            pass

    @staticmethod
    def print_log(self):
        """
        print_log()

        Prints log into console.
        """
        print('Log:')
        with open('victories.log') as file:
            for line in file:
                print(line.strip())
        while True:
            choice = input('\nPrint \'b\' to exit: ')
            if choice in ('B', 'b'):
                break


def main():
    """
    main()

    Main function. Runs the game.
    """
    board = Board()
    game = Game(board)
    game.print_menu()


if __name__ == "__main__":
    main()
