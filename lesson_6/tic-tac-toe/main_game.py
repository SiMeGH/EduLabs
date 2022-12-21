from draw_board import draw_board
from game_init import *
from ai_turn import computer_turn
from human_turn import human_turn


def check_available_point(point: tuple[int, int]) -> bool:
    if point in available_points:
        return True
    return False


def play(point: tuple[int, int]) -> None:
    turn[1] += 1
    value: int = players[turn[0]]['value']
    win_cons[point[0] - 1] += value
    win_cons[point[1] - 1 + board_size] += value
    if point[0] == point[1]:
        win_cons[-2] += value
    if point[0] + point[1] == board_size + 1:
        win_cons[-1] += value
    available_points.remove(point)
    drawing_points[point[0] - 1][point[1] - 1] = turn[0]


def change_turn() -> None:
    if turn[0] == 'X':
        turn[0] = 'O'
        return
    turn[0] = 'X'


def check_game_end() -> None:
    if players[turn[0]]['value'] * board_size in win_cons:
        game_state[0] = 'Win'
    elif turn[1] == board_size ** 2:
        game_state[0] = 'Draw'


def enter_game_loop() -> None:
    while True:
        if mode == 'C':
            if players[turn[0]]['player'] == 'C':
                computer_turn()
                draw_board()
                check_game_end()
                if game_state[0] in ('Win', 'Draw'):
                    break
                change_turn()
                human_turn()
                check_game_end()
                if game_state[0] in ('Win', 'Draw'):
                    draw_board()
                    break
                change_turn()
            else:
                draw_board()
                human_turn()
                check_game_end()
                if game_state[0] in ('Win', 'Draw'):
                    break
                change_turn()
                computer_turn()
                check_game_end()
                if game_state[0] in ('Win', 'Draw'):
                    draw_board()
                    break
                change_turn()
        else:
            draw_board()
            human_turn()
            check_game_end()
            if game_state[0] in ('Win', 'Draw'):
                draw_board()
                break
            change_turn()


def print_game_end() -> None:
    if game_state[0] == 'Win':
        print(f"{turn[0]} is the winner!")
    else:
        print("It's a draw!")


def choose_to_play() -> bool:
    play_again: str = input("Would you like to play again? y/n: ")
    if play_again == 'y':
        return True
    return False


if __name__ == '__main__':
    while True:
        print("Welcome to Tic-Tac-Toe!")

        # fundamental game requirements
        mode: str = choose_mode()
        board_size: int = choose_board_size()

        # creates relevant data
        players: dict = assign_players()
        available_points: list[tuple[int, int]] = generate_available_points()
        drawing_points: list[list[str]] = generate_drawing_points()
        turn: list[str, int] = ['X', 0]
        win_cons: list[int] = generate_win_cons()
        game_state: list[str] = ['Play']
        current_play: list[tuple[int, int]] = [(0, 0)]

        # game loop
        enter_game_loop()
        prepare_next_part()
        print_game_end()
        if not choose_to_play():
            break
        prepare_next_part()
    print('Bye bye!')
