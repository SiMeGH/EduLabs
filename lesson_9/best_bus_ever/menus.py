from abc import ABC, abstractmethod
from general_menu_functions import *


class Menu(ABC):

    def __init__(self, options: list):
        self.__options = options

    def get_options(self) -> list:
        return self.__options

    def choose_option(self, text: str = "Choose menu option: "):
        while True:
            choice: str = input(text).strip()
            if not choice.isdigit():
                print("Invalid input. Must be an integer.")
                continue
            if not (1 <= int(choice) <= len(self.__options)):
                print("Invalid input. Not part of the menu options.")
                continue
            return self.__options[int(choice) - 1]

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class UpdateRouteMenu(Menu):
    __OPTIONS: list = ['Origin', 'Destination', "Middle Stops", "None - Go back to the Manager Menu"]

    def __init__(self, bus_company: BusCompany):
        super().__init__(self.__OPTIONS)
        self.bus_company: BusCompany = bus_company

    def __str__(self):
        return "Update Route Menu"

    def __repr__(self):
        return "Update Route Menu"


class SearchRouteMenu(Menu):
    __OPTIONS: list = ['Line', 'Origin', 'Destination', "Bus Stop", "None - Go back to the Passenger Menu"]

    def __init__(self, bus_company: BusCompany):
        super().__init__(self.__OPTIONS)
        self.bus_company: BusCompany = bus_company

    def __str__(self):
        return "Search Route Menu"

    def __repr__(self):
        return "Search Route Menu"


class PassengerMenu(Menu):

    __OPTIONS: list = ["Search Route", "Report Delay", "Back to Main Menu"]

    def __init__(self, bus_company: BusCompany):
        super().__init__(self.__OPTIONS)
        self.__bus_company: BusCompany = bus_company
        self.__all_routes: dict = self.__bus_company.get_bus_routes()
        self.__all_rides: dict = self.__bus_company.get_scheduled_rides()

    def _is_location_in_line(self, choice: str, line: int, location: str):
        if (choice == "Origin" and self.__bus_company.get_origin(line) == location) or \
                (choice == "Destination" and self.__bus_company.get_destination(line) == location) or \
                (choice == "Bus Stop" and location in self.__bus_company.get_stops(line).split(', ')):
            return True
        return False

    def search_route(self) -> None:
        if is_pointless_action(self.__all_routes, "No routes available.", self.__bus_company):
            return

        search_menu: SearchRouteMenu = SearchRouteMenu(self.__bus_company)
        print_menu(search_menu.get_options())
        choice: str = search_menu.choose_option()
        check: bool = False
        match choice:
            case "Line":
                line: int = check_route_line_available("Search Route:", self.__bus_company)
                if line is None:
                    return
                print(self.__bus_company.get_bus_routes(line))
                print_scheduled_rides(self.__all_rides, line)
            case "Origin" | "Destination" | "Bus Stop":
                print_gap()
                location: str = input(f"Enter {choice.lower()}: ").strip()
                for line in self.__all_routes:
                    if self._is_location_in_line(choice, line, location):
                        print(self.__bus_company.get_bus_routes(line))
                        check = True
                if not check:
                    print(f"Route with {choice.lower()} \'{location}\' \
doesn't exist in {self.__bus_company.get_name()}'s database.")
            case _:
                print("Returning to Passenger Menu...")
                return

    @staticmethod
    def _input_ride_from_presented_list(text: str, ride_ids: list[int]) -> int:
        while True:
            try:
                choice: str = input(text)
                if not choice.isdigit():
                    raise InputNotAnInteger()
                if int(choice) not in ride_ids:
                    raise InputNotInList()
                return int(choice)
            except MenuException as error:
                print(error)

    @staticmethod
    def _input_line_from_presented_list(text: str, max_: int) -> int:
        while True:
            try:
                choice: str = input(text)
                if not choice.isdigit():
                    raise InputNotAnInteger()
                if 0 < int(choice) < max_:
                    raise InputOutOfRange()
                return int(choice)
            except MenuException as error:
                print(error)

    def _choose_ride_to_delay(self, line: int):
        scheduled_ride_list: list = self.__bus_company.get_scheduled_rides(line)
        if not scheduled_ride_list:
            print("No rides to report a delay for.")
            return
        ride_ids: list[int] = []
        for ride in scheduled_ride_list:
            ride_ids.append(self.__bus_company.get_ride_id(ride))
            print(ride)
        print_gap()
        ride_choice_txt: str = "Choose which ride you'd like to report the delay for by \'ID\': "
        ride_choice: int = self._input_ride_from_presented_list(ride_choice_txt, ride_ids)
        self.__bus_company.add_delay(self.__bus_company.get_ride_by_id(line, ride_choice))
        print(f"~~ Delay for ride ID \'{ride_choice}\' \
in line \'{line}\' has been reported successfully! ~~")

    def report_delay(self) -> None:
        if is_pointless_action(self.__all_rides, "No scheduled rides available.", self.__bus_company):
            return

        search_menu: SearchRouteMenu = SearchRouteMenu(self.__bus_company)
        print_menu(search_menu.get_options())
        choice: str = search_menu.choose_option()
        check: bool = False
        match choice:
            case "Line":
                print_all_bus_routes(self.__bus_company)
                line: int = check_route_line_available("Search Route:", self.__bus_company)
                if line is None:
                    return
                self._choose_ride_to_delay(line)
            case "Origin" | "Destination" | "Bus Stop":
                print_gap()
                location: str = input(f"Enter {choice.lower()}: ").strip()
                print()
                lines: list[int] = []
                line_index: int = 0
                for line in self.__all_routes:
                    if self._is_location_in_line(choice, line, location):
                        line_index += 1
                        print(f" {line_index} - {self.__bus_company.get_bus_routes(line)}")
                        lines.append(line)
                        check = True
                if not check:
                    print(f"No data available for this particular {choice.lower()}.")
                    return
                print()
                route_choice_txt: str = "Choose which route you'd like to get the schedule list from: "
                route_choice: int = self._input_line_from_presented_list(route_choice_txt, len(lines))
                chosen_line: int = lines[route_choice - 1]
                print()
                self._choose_ride_to_delay(chosen_line)
            case _:
                print("Returning to Passenger Menu...")
                return

    def __str__(self):
        return 'Passenger'

    def __repr__(self):
        return 'Passenger'


class ManagerMenu(Menu):

    __OPTIONS: list = ["Add Route", "Delete Route", "Update Route", "Add Scheduled Ride", "Back to Main Menu"]

    __PASSWORD: str = 'RideWithUs'

    def _is_manager(self) -> bool:
        for i in range(2, -1, -1):
            password: str = input("Enter manager password: ")
            if password == self.__PASSWORD:
                return True
            print(f"{i} attempts left")
        print("Returning to the Main Menu...")
        return False

    def __init__(self, bus_company: BusCompany):
        if not self._is_manager():
            raise WrongManagerPassword()
        super().__init__(self.__OPTIONS)
        self.__bus_company: BusCompany = bus_company
        self.__all_routes: dict = self.__bus_company.get_bus_routes()
        self.__all_rides: dict = self.__bus_company.get_scheduled_rides()

    @staticmethod
    def _input_stops_list(origin: str, destination: str) -> str:
        print("Enter all stops, each separated with a comma:")
        stops: str = input(f"- Stops: ")
        stops_list: list[str] = stops.split(',')
        # removes all empty strings
        filtered_stops_list: list[str] = [stop.strip() for stop in stops_list if stop.strip() != '']
        # removes input duplicates
        no_dupes_stops_list: list[str] = list(dict.fromkeys(filtered_stops_list))
        # removes origin and destination duplicates
        if origin in no_dupes_stops_list:
            no_dupes_stops_list.remove(origin)
        if destination in no_dupes_stops_list:
            no_dupes_stops_list.remove(destination)
        return ', '.join(no_dupes_stops_list)

    @staticmethod
    def _input_single_location(title: str) -> str:
        while True:
            try:
                location: str = input(title).strip()
                if location == '':
                    raise StringMustNotBeEmpty
                return location
            except StringMustNotBeEmpty as error:
                print(error)

    def add_route(self) -> None:
        print_gap()
        print("Route details:")

        line: int = input_route_line("- Line Number: ")
        origin: str = self._input_single_location("- Origin: ")
        destination: str = self._input_single_location("- Destination: ")
        stops: str = self._input_stops_list(origin, destination)

        if self.__bus_company.add_route(line, origin, destination, stops):
            print(f"~~ Line \'{line}\' has been added successfully! ~~")
        return

    def delete_route(self) -> None:
        if is_pointless_action(self.__all_routes, "No routes available.", self.__bus_company):
            return

        line: int = check_route_line_available("Delete route:", self.__bus_company)
        if line is None:
            return

        print(f"Are you sure you want to delete line \'{line}\'?")
        confirmation: str = input("- Type 'yes' to confirm: ").strip()
        if confirmation == 'yes':
            self.__bus_company.delete_route(line)
            print(f"~~ Line \'{line}\' has been removed successfully! ~~")
            return
        print(f"~~ Line \'{line}\' has not been removed. ~~")
        return

    def update_route(self) -> None:
        if is_pointless_action(self.__all_routes, "No routes available.", self.__bus_company):
            return

        line: int = check_route_line_available("Update route:", self.__bus_company)
        if line is None:
            return

        print(f"Bus line \'{line}\' goes through the following route:")
        print(self.__bus_company.get_journey(line))  # change
        menu: UpdateRouteMenu = UpdateRouteMenu(self.__bus_company)
        print_menu(menu.get_options())
        menu_choice: str = menu.choose_option("Which one would you like to change? ")
        if menu_choice == 'None - Go back to the Manager Menu':
            print("Returning to the Manager Menu...")
            return
        if menu_choice == 'Middle Stops':
            origin: str = self.__bus_company.get_origin(line)
            destination: str = self.__bus_company.get_destination(line)
            new_value: str = self._input_stops_list(origin, destination)
        else:
            new_value: str = self._input_single_location(f"- {menu_choice}: ")
        self.__bus_company.update_route(line, menu_choice, new_value)
        print(f"~~ Line \'{line}\' has been updated successfully! ~~")

    @staticmethod
    def _input_ride_time(text) -> str:
        while True:
            try:
                ride_time: str = input(text).strip()
                if len(ride_time) != 5:
                    raise InputNotMadeOfFiveCharacters()
                if ride_time.count(':') != 1:
                    raise InputMustContainExactlyOneSemicolon()
                if ride_time.index(':') != 2:
                    raise InputMustContainOneSemicolonInTheMiddle()
                if not ride_time[:2].isdigit() and not ride_time[3:].isdigit():
                    raise InputMustContainDigitsOnTheSides()
                if int(ride_time[:2]) >= 24:
                    raise HoursCantBeHigherThan23()
                if int(ride_time[3:]) >= 60:
                    raise MinutesCantBeHigherThan59()
                return ride_time
            except MenuException as error:
                print(error)

    def add_scheduled_ride(self):
        if is_pointless_action(self.__all_routes, "No routes available.", self.__bus_company):
            return

        line: int = check_route_line_available("Add Scheduled Ride:", self.__bus_company)
        if line is None:
            return

        if line in self.__all_rides:
            print(self.__bus_company.get_bus_routes(line))
            print_scheduled_rides(self.__all_rides, line)
            print_gap()

            print(f"Do you still want to add a scheduled ride to line \'{line}\'?")
            confirmation: str = input("- Type 'yes' to confirm: ").strip()
            if confirmation != 'yes':
                print("Returning to the Manager Menu...")
                return

        print_gap()
        origin_time: str = self._input_ride_time("Enter origin station time. Use \'hh:mm\' format: ")
        destination_time: str = self._input_ride_time("Enter destination station time. Use \'hh:mm\' format: ")
        driver: str = input("Enter the driver's name for this ride: ")
        self.__bus_company.add_scheduled_ride(line, origin_time, destination_time, driver)
        print(f"~~ Scheduled ride to line \'{line}\' has been added successfully! ~~")
        return

    def __str__(self):
        return 'Manager'

    def __repr__(self):
        return 'Manager'


class MainMenu(Menu):

    __OPTIONS: list = ['Passenger', 'Manager', 'Exit Program']

    def __init__(self, bus_company: BusCompany):
        super().__init__(self.__OPTIONS)
        self.bus_company: BusCompany = bus_company

    def run(self):
        while True:
            print_menu(self.get_options(), 3)

            main_menu_choice: str = self.choose_option()
            match main_menu_choice:
                case 'Passenger':
                    sub_menu: PassengerMenu = PassengerMenu(self.bus_company)
                    while True:
                        print_menu(sub_menu.get_options(), 2)
                        sub_menu_choice: str = sub_menu.choose_option()
                        match sub_menu_choice:
                            case 'Search Route':
                                sub_menu.search_route()
                            case 'Report Delay':
                                sub_menu.report_delay()
                            case _:
                                print("Returning to the Main Menu...")
                                break
                case 'Manager':
                    try:
                        print_gap()
                        sub_menu: ManagerMenu = ManagerMenu(self.bus_company)
                        while True:
                            print_menu(sub_menu.get_options(), 2)
                            sub_menu_choice: str = sub_menu.choose_option()
                            match sub_menu_choice:
                                case "Add Route":
                                    sub_menu.add_route()
                                case "Delete Route":
                                    sub_menu.delete_route()
                                case "Update Route":
                                    sub_menu.update_route()
                                case "Add Scheduled Ride":
                                    sub_menu.add_scheduled_ride()
                                case _:
                                    print("Returning to the Main Menu...")
                                    break
                    except WrongManagerPassword:
                        continue
                case _:
                    break

    def __str__(self):
        return "Main Menu"

    def __repr__(self):
        return "Main Menu"
