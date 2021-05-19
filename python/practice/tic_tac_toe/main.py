"""
Simple tic tac toe game.
"""
import logging

RED = '\033[91m'
BLUE = '\033[94m'
ENDC = '\033[0m'
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
players = {1: '', 2: ''}
score = {1: 0, 2: 0}
markers = {1: f'{RED}X{ENDC}', 2: f'{BLUE}O{ENDC}'}
current_player = 1
current_marker = 1

logging.basicConfig(filename='victories.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

MENU = """
Main menu
1. Play.
2. View log.
3. CLear log.
4. Exit.
"""


def print_menu():
    """
    print_menu() -> int

    Responsible for main menu work.
    """
    print(MENU)
    while True:
        choice = input('Choose an option: ')
        if choice == '1':
            set_names_and_score()
            game()
            return 0
        if choice == '2':
            print_log()
        elif choice == '3':
            clear_log()
        elif choice == '4':
            return 0


def draw_board():
    """
    draw_board()

    Draws the game board.
    """
    print(f'\n{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')


def change_marker(slot):
    """
    change_marker(slot: int)

    Changes the board slot with the current marker.
    """
    board[slot - 1] = markers[current_marker]


def winner():
    """
    winner() -> int

    Returns winner id if the game is end.
    Otherwise returns 0.
    """
    i = j = 0
    for _ in range(3):
        if board[i] == board[i + 1] == board[i + 2]:
            return current_player
        if board[j] == board[j + 3] == board[j + 6]:
            return current_player
        i += 3
        j += 1
    if board[0] == board[4] == board[8]:
        return current_player
    if board[2] == board[4] == board[6]:
        return current_player
    return 0


def swap_turn():
    """
    swap_turn()

    Passes the turn to another player.
    """
    global current_player, current_marker
    current_player = 1 if current_player == 2 else 2
    current_marker = 1 if current_marker == 2 else 2


def set_names_and_score():
    """
    set_names_and_score()

    Sets names and score at the start of the game.
    """
    score[1] = score[2] = 0
    players[1] = input('Player 1, enter your name: ')
    players[2] = input('Player 2, enter your name: ')
    logging.info('=====%s vs %s=====', players[1], players[2])


def reset_game():
    """
    reset_game()

    Resets all necessary parameters.
    """
    global board, current_marker, current_player
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = 1
    current_marker = 1


def clear_log():
    """
    clear_log()

    Clears file with log victories.
    """
    with open('victories.log', 'w'):
        pass


def print_log():
    """
    print_log()

    Prints log into console.
    """
    print('Log:')
    with open('victories.log') as file:
        for line in file:
            print(line.strip())


def game():
    """
    game()

    Main function that controls the game.
    """
    draw_board()
    for _ in range(9):
        change_marker(int(input(f'\n{players[current_player]}, your turn: ')))
        draw_board()
        if winner() == current_player:
            print(f'\nCongratulations {players[current_player]}, you won!')
            score[current_player] += 1
            logging.info('%s wins.', players[current_player])
            logging.info('Score: %s/%s.', score[1], score[2])
            break
        swap_turn()
    if winner() == 0:
        print('\nThat is a tie.')
        logging.info('A tie.')
    if input('\nPlay one more game(1-yes, 2-no)?\n') == '1':
        reset_game()
        game()


def main():
    """
    main()

    Main function. Runs the game.
    """
    print_menu()


if __name__ == "__main__":
    main()
