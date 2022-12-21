from menu_exceptions import *
from bus_company import BusCompany


def print_gap(n: int = 1):
    for i in range(n):
        print("__________")
    print()


def print_menu(menu_options: list, n_gap: int = 1):
    print_gap(n_gap)
    print("Options menu:")
    for i, option in enumerate(menu_options, start=1):
        print(f" {i} - {option}")


def input_route_line(input_text: str = "Enter route line number: ") -> int:
    while True:
        try:
            line_str: str = input(input_text).strip()
            if not line_str.isdigit() or int(line_str) == 0:
                raise LineIsNotAPositiveInteger()
            return int(line_str)
        except LineIsNotAPositiveInteger as error:
            print(error)


def check_route_line_available(title: str, bus_company: BusCompany) -> int | None:
    print_gap()
    print(title)
    line: int = input_route_line()
    if line in bus_company.get_bus_routes():
        return line
    print(f"Route with line \'{line}\' doesn't exist in {bus_company.get_name()}'s database.")
    return None


def is_empty(iterable: list | dict, text) -> bool:
    if not len(iterable):
        print(f"\n{text}")
        return True
    return False


def print_all_bus_routes(bus_company: BusCompany) -> None:
    print_gap()
    print("All Routes:")
    for route_line in bus_company.get_bus_routes():
        print(bus_company.get_bus_routes(route_line))


def print_scheduled_rides(rides: dict[int, list], line: int) -> None:
    for ride in rides[line]:
        print(f"\t{ride}")


def is_pointless_action(iterable: list | dict, text: str, bus_company: BusCompany) -> bool:
    if is_empty(iterable, text):
        return True
    print_all_bus_routes(bus_company)
    return False
