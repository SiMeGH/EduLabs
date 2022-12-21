from main_game import board_size, drawing_points


def draw_header() -> None:
    print('\n   ', end='')
    for col in range(1, board_size + 1):
        print(f"   {col}    ", end='')
    print()


def draw_line1() -> None:
    print('   ', end='')
    for col in range(board_size):
        print('       ', end='')
        if col != board_size - 1:
            print('|', end='')
    print()


def draw_line2(row: int) -> None:
    print(f" {row} ", end='')
    for col in range(board_size):
        print(f"   {drawing_points[row - 1][col]}   ", end='')
        if col != board_size - 1:
            print('|', end='')
    print()


def draw_line3(row: int) -> None:
    print('   ', end='')
    for col in range(board_size):
        if row != board_size:
            print('_______', end='')
        else:
            print('       ', end='')
        if col != board_size - 1:
            print('|', end='')
    print()


def draw_board() -> None:
    draw_header()
    for row in range(1, board_size + 1):
        draw_line1()
        draw_line2(row)
        draw_line3(row)
