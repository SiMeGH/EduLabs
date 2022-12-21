from main_game import board_size, check_available_point, current_play, play, turn


def choose_human_play() -> tuple[int, int]:
    player_input: str = input(f"Choose where you would like to place \'{turn[0]}\' (e.g \"1-3\"): ").strip()
    while True:
        if len(player_input) == 3 and player_input.count('-') == 1 and player_input[1] == '-':
            player_point: list[str] = player_input.split('-')
            if player_point[0].isdigit() and \
                    player_point[1].isdigit() and \
                    1 <= int(player_point[0]) <= board_size and \
                    1 <= int(player_point[1]) <= board_size:
                point: tuple[int, int] = int(player_point[0]), int(player_point[1])
                if check_available_point(point):
                    return point
                player_input = input("Point is already occupied. Please enter another: ")
                continue
        player_input = input(f"Point has to be in the format \'#-#\' with number between 1 and {board_size}: ")
        continue


def human_turn() -> None:
    current_play[0] = choose_human_play()
    play(current_play[0])
