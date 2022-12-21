from random import randint


def check_str_to_int(s):
    s = s.strip()
    return s and \
           (s.isdigit() or
            (s[0] == '-' and
             len(s) > 1 and
             s[1:].isdigit()))


def check_str_to_float(s):
    s = s.strip()
    check = s and \
            s.count('.') == 1 and \
            len(s) > 1 and \
            ((s[0] == '.' and
              s[1:].isdigit()) or
             (s[-1] == '.' and
              s[:-1].isdigit()) or
             (s[:s.index('.')].isdigit() and
              s[s.index('.') + 1:].isdigit()) or
             (s[0] == '-' and
              len(s) > 2 and
              (s[1] == '.' and
               s[2:].isdigit()) or
              (s[-1] == '.' and
               s[1:-1].isdigit()) or
              (s[1:s.index('.')].isdigit() and
               s[s.index('.') + 1:].isdigit())))
    return check


def check_str_to_number(s):
    s = s.strip()
    return check_str_to_int(s) or check_str_to_float(s)


def ask_for_name() -> tuple[str, str]:
    while True:
        first_name: str = input("Enter first name: ")
        if first_name != '':
            break
        print("Your first name must consist of some characters.")
    while True:
        last_name: str = input("Enter last name: ")
        if last_name != '':
            break
        print("Your last name must consist of some characters.")
    print('-----------\n')
    return first_name, last_name


def ask_for_class(class_options: list[str]) -> str:
    print("Your class options are: ")
    for i, class_ in enumerate(class_options):
        print(f"- {i + 1} - {class_.capitalize()} class")
    while True:
        class_str: str = input(f"Enter which class you'd like (1-{len(class_options)}): ").strip()
        if class_str.isdigit() and 1 <= int(class_str) <= len(class_options):
            class_int: int = int(class_str)
            break
        print("Invalid input.")
    print('-----------\n')
    return class_options[class_int - 1]


# dict{str: tuple[int, int], str: list[tuple(int, int)], int: int, ..., str: tuple(list[int], int)}
def ask_for_line(line_options: dict) -> int:
    print("Your line options are: ")
    for i, lines in enumerate(line_options['options']):
        print(f"- {lines[0]}-{lines[1]} - \tcost: {line_options[i]}$")
    if line_options.get('extra'):
        special_lines: list[int] = line_options['extra'][0]
        print(f"Extra cost of {line_options['extra'][1]}$ for line(s) ", end='')
        for j in range(len(special_lines)):
            if j == 0:
                print(f"{special_lines[j]}", end='')
            elif j < len(special_lines) - 1:
                print(f", {special_lines[j]}", end='')
            else:
                print(f" and {special_lines[j]}")
    while True:
        line_str = input("Enter which line you'd like: ").strip()
        if line_str.isdigit() and \
                line_options['range'][0] <= int(line_str) <= line_options['range'][1]:
            line: int = int(line_str)
            break
        print("Invalid input.")
    print('-----------\n')
    return line


# dict{str: list[str], str: int}
def ask_for_seat(seat_options: dict) -> str:
    seats: list[str] = seat_options['options']
    print("Your line options are: ")
    for j in range(len(seats)):
        if j == 0:
            print(f"{seats[j]}", end='')
        elif j < len(seats) - 1:
            print(f", {seats[j]}", end='')
        else:
            print(f" and {seats[j]}")
    print(f"Window seats cost an extra {seat_options['window']}$")
    while True:
        seat: str = input("Enter which seat you'd like: ").strip().upper()
        if seat in seats:
            break
        print(f"Invalid input. Seat has to be between \'{seats[0]}\' and \'{seats[-1]}\'")
    print('-----------\n')
    return seat


def choose_from_luxury_menus() -> int:
    print("~ Luxury Menus ~")
    print(luxury_menus)
    while True:
        menu_str: str = input("Enter which menu number you'd like: ").strip()
        if menu_str.isdigit() and \
                1 <= int(menu_str) <= 3:
            menu_int: int = int(menu_str)
            break
        print("Invalid input. Must choose from available menu numbers.")
    return menu_int


def ask_for_meal(meal_options: list[str]) -> tuple[str, int]:
    print("Your meal options are: ")
    for i, meal in enumerate(meal_options):
        print(f"- {i + 1} - {meal.capitalize()}")
    while True:
        meal_str: str = input(f"Enter which meal you'd like (1-{len(meal_options)}): ").strip()
        if meal_str.isdigit() and \
                1 <= int(meal_str) <= len(meal_options):
            meal_int: int = int(meal_str)
            break
        print("Invalid input.")
    if meal_int == 1:
        print('-----------\n')
        menu: int = choose_from_luxury_menus()
    else:
        menu: int = 0
    print('-----------\n')
    return meal_options[meal_int - 1], menu


def ask_for_luggage() -> float:
    while True:
        weight_str: str = input("Enter weight of your luggage in kilograms: ").strip()
        if check_str_to_number(weight_str) and weight_str[0] != '-':
            weight: float = float(weight_str)
            break
        print("Invalid input. Must be a non-negative number.")
    print('-----------\n')
    return weight


def calc_base_cost() -> int:
    line_options: list[tuple[int, int]] = flight_data[my_class]['lines']['options']
    for i, pair in enumerate(line_options):
        if my_line < pair[1]:
            return flight_data[my_class]['lines'][i]


def calc_extra_line_cost() -> int:
    if flight_data[my_class]['lines'].get('extra') and \
            my_line in flight_data[my_class]['lines']['extra'][0]:
        return flight_data[my_class]['lines']['extra'][1]
    return 0


def calc_window_cost() -> int:
    if my_seat == 'A' or my_seat == flight_data[my_class]['seats']['options'][-1]:
        return flight_data[my_class]['seats']['window']
    return 0


def calc_luggage_cost() -> float:
    luggage: tuple[int, int] = flight_data[my_class]['luggage']
    if my_luggage <= luggage[1]:
        return 0
    return (my_luggage - luggage[1]) * luggage[0]


def calc_meal_cost() -> int:
    return flight_data[my_class]['meal'][my_meal[0]]


def calculate_costs() -> dict[str, float]:
    costs: dict[str, float] = dict()
    costs['base'] = float(calc_base_cost())
    costs['extra'] = float(calc_extra_line_cost())
    costs['window'] = float(calc_window_cost())
    costs['luggage'] = float(calc_luggage_cost())
    costs['meal'] = float(calc_meal_cost())
    return costs


def print_base_flight_receipt() -> None:
    print(f"{my_name[0]} {my_name[1]}, your base ticket cost is: {'%.2f' % my_cost['base']}$")


def print_extra_flight_receipt() -> None:
    total_extra = 0
    print("Extra payments:")
    for key, value in my_cost.items():
        if value != 0 and key != 'base':
            print(f"- {key}: {'%.2f' % value}$")
            total_extra += value
    if total_extra == 0:
        print("None")
    else:
        print(f"Total Extra: {'%.2f' % total_extra}$")
    print('-----------\n')


def print_flight_receipt():
    print_base_flight_receipt()
    print_extra_flight_receipt()


def print_flight_receipt_final():
    total_cost: float = 0
    for value in my_cost.values():
        total_cost += value
    print(f"Your total cost is {'%.2f' % round(total_cost, 2)}$")
    print('-----------\n')


def my_discount() -> None:
    while True:
        lucky_number_str: str = input("Enter a lucky number between 1 and 9 for a chance at a discount: ")
        if lucky_number_str.isdigit() and 1 <= int(lucky_number_str) <= 9:
            lucky_number: int = int(lucky_number_str)
            break
        print("Invalid input.")
    name_length: int = len(my_name[0]) + len(my_name[1])
    rand_number: int = randint(1, 5)
    remainder: int = (name_length * rand_number) // lucky_number
    if 0 < remainder <= 5:
        print(f"You won! You got a {remainder}% discount!")
    else:
        print(f"Sorry, you didn't win a discount.")


if __name__ == '__main__':
    luxury_menus = """Menu #1 : STARTER - Roast veal sweetbread
          MAIN    - Cornish turbot
          DESERT  - Hazelnut souffle

Menu #2 : STARTER - Ravioli lobster
          MAIN    - 100-Day aged Cumbrian Blue Grey
          DESERT  - Pecan praline

Menu #3 : STARTER - Scallops from the Isle of Skye
          MAIN    - Aynhoe Park fallow deer
          DESERT  - Caramelised apple Tarte Tatin"""

    flight_data = {
        'class_list': ['first', 'business', 'economy'],
        'meal_list': ['luxury', 'business', 'economy'],
        'first': {
            'lines': {
                'range': (1, 4),
                'options': [(1, 4)],
                0: 4_000
            },
            'seats': {
                'options': ['A', 'B', 'C', 'D'],
                'window': 0
            },
            'luggage': (0, 0),
            'meal': {
                'luxury': 0,
                'business': 0,
                'economy': 0
            }
        },
        'business': {
            'lines': {
                'range': (5, 10),
                'options': [(5, 7), (8, 10)],
                0: 3_000,
                1: 2_300
            },
            'seats': {
                'options': ['A', 'B', 'C', 'D'],
                'window': 55
            },
            'luggage': (10, 50),
            'meal': {
                'luxury': 42,
                'business': 0,
                'economy': 0
            }
        },
        'economy': {
            'lines': {
                'range': (11, 60),
                'options': [(11, 20), (21, 40), (41, 60)],
                0: 1_700,
                1: 1_500,
                2: 1_200,
                'extra': ([12, 22, 42], 15)
            },
            'seats': {
                'options': ['A', 'B', 'C', 'D', 'E', 'F'],
                'window': 10
            },
            'luggage': (10, 20),
            'meal': {
                'luxury': 42,
                'business': 22,
                'economy': 7
            }
        }
    }

    # 1.
    print("Welcome!")

    # 2.
    my_name: tuple[str, str] = ask_for_name()

    # 3.
    my_class: str = ask_for_class(flight_data['class_list'])

    # 4.
    my_line: int = ask_for_line(flight_data[my_class]['lines'])

    # 5.
    my_seat: str = ask_for_seat(flight_data[my_class]['seats'])

    # 6.
    my_meal: tuple[str, int] = ask_for_meal(flight_data['meal_list'])

    # 7.
    my_luggage: float = ask_for_luggage()

    # 8.
    my_cost: dict[str, float] = calculate_costs()

    # 8. a.
    print_flight_receipt()

    # 8. b.
    print_flight_receipt_final()

    # 9.
    my_discount()
