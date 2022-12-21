from random import randint
from main_game import available_points, current_play, play


def generate_ai_play() -> tuple[int, int]:
    return available_points[randint(0, len(available_points) - 1)]


def computer_turn() -> None:
    current_play[0] = generate_ai_play()
    play(current_play[0])
