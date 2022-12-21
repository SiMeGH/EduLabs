from random import randint
from main_game import mode, board_size


def prepare_next_part() -> None:
    print('___________\n')


def print_invalid_input() -> None:
    print("Invalid input.")


def choose_mode() -> str:
    print("Do you want to play against another human or the computer?")
    while True:
        mode_choice: str = input("Type 'H' or 'C': ").strip().upper()
        if mode_choice in ('C', 'H'):
            prepare_next_part()
            return mode_choice
        print_invalid_input()


def choose_board_size() -> int:
    while True:
        board_choice: str = input("Choose a board size between 3 and 9: ").strip()
        if board_choice.isdigit() and 3 <= int(board_choice) <= 9:
            prepare_next_part()
            return int(board_choice)
        print_invalid_input()


def assign_players() -> dict:
    player_info: dict = {
        'X': {'value': 1, 'player': None},
        'O': {'value': -1, 'player': None}
    }
    main_player: int = randint(1, 2)
    if main_player == 1:
        player_info['X']['player'] = 'main'
        player_info['O']['player'] = mode
    else:
        player_info['X']['player'] = mode
        player_info['O']['player'] = 'main'
    return player_info


def generate_win_cons() -> list[int]:
    return [0] * (board_size * 2 + 2)


def generate_available_points() -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = []
    for i in range(1, board_size + 1):
        for j in range(1, board_size + 1):
            points.append((i, j))
    return points


def generate_drawing_points() -> list[list[str]]:
    points: list[list[str]] = [[]] * board_size
    for i in range(board_size):
        points[i] = [' '] * board_size
    return points
