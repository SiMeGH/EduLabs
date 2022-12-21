from bus_exceptions import *


class ScheduledRide:

    def __init__(self, ride_id: int, origin: str, destination: str, driver: str):
        self.__ride_id: int = ride_id
        self.__origin_time: str = origin
        self.__destination_time: str = destination
        self.__driver: str = driver
        self.__delays: int = 0

    def get_ride_id(self):
        return self.__ride_id

    def add_delay(self) -> None:
        self.__delays += 1

    def __str__(self):
        return f"// ID: {self.__ride_id} | \
Origin: {self.__origin_time} | \
Destination: {self.__destination_time}"

    def __repr__(self):
        return f"// ID: {self.__ride_id} | \
Origin: {self.__origin_time} | \
Destination: {self.__destination_time}"


class BusRoute:

    def __init__(self, line: int, origin: str, destination: str, stops: str = ''):
        self.__line: int = line
        self.__origin: str = origin
        self.__destination: str = destination
        if stops is None:
            self.__stops: str = ''
        else:
            self.__stops: str = stops
        self.__scheduled_rides: list = []

    def get_line(self) -> int:
        return self.__line

    def get_origin(self) -> str:
        return self.__origin

    def get_destination(self) -> str:
        return self.__destination

    def get_stops(self) -> str:
        return self.__stops

    def get_journey(self) -> str:
        if self.__stops == '':
            return f"{self.__origin}, {self.__destination}"
        return f"{self.__origin}, {self.__stops}, {self.__destination}"

    def get_scheduled_rides(self) -> list:
        return self.__scheduled_rides

    def get_total_scheduled_rides(self) -> int:
        return len(self.__scheduled_rides)

    def set_origin(self, new_origin: str) -> None:
        self.__origin = new_origin

    def set_destination(self, new_destination: str) -> None:
        self.__destination = new_destination

    def set_stops(self, new_stops: str) -> None:
        self.__stops = new_stops

    def add_scheduled_ride(self, scheduled_ride: ScheduledRide) -> None:
        self.__scheduled_rides.append(scheduled_ride)

    def __str__(self):
        return f"|| Line: {self.__line} | \
Origin: {self.__origin} | \
Destination: {self.__destination} | \
Stops: {self.__stops} | \
Scheduled Rides: {self.get_total_scheduled_rides()}]"

    def __repr__(self):
        return f"|| Line: {self.__line} | \
Origin: {self.__origin} | \
Destination: {self.__destination} | \
Stops: {self.__stops} | \
Scheduled Rides: {self.get_total_scheduled_rides()}"


class BusCompany:

    def __init__(self, name: str):
        self.__name: str = name
        self.__bus_routes: dict[int, BusRoute] = {}
        self.__scheduled_rides: dict[int, list[ScheduledRide]] = {}
        self.__ride_id: int = 1

    def get_name(self) -> str:
        return self.__name

    def _get_specific_bus_route(self, specific_route: int) -> BusRoute:
        try:
            if not isinstance(specific_route, int) or specific_route == 0:
                raise ValueError()
            if specific_route not in self.__bus_routes:
                raise LineDoesNotExist()
            return self.__bus_routes[specific_route]
        except Exception as error:
            print(error)

    def _get_specific_scheduled_rides(self, specific_route: int) -> list[ScheduledRide]:
        try:
            if not isinstance(specific_route, int) or specific_route == 0:
                raise ValueError
            if specific_route not in self.__bus_routes:
                raise LineDoesNotExist()
            if not len(self.__scheduled_rides):
                raise NoScheduledRidesForRoute()
            return self.__scheduled_rides[specific_route]
        except Exception as error:
            print(error)

    def get_bus_routes(self, specific_route: int = None) -> dict[int, BusRoute] | BusRoute:
        if specific_route:
            return self._get_specific_bus_route(specific_route)
        return self.__bus_routes

    def get_scheduled_rides(self, specific_route: int = None) -> dict[int, list[ScheduledRide]] | list[ScheduledRide]:
        if specific_route:
            return self._get_specific_scheduled_rides(specific_route)
        return self.__scheduled_rides

    def get_origin(self, line: int) -> str:
        return self.__bus_routes[line].get_origin()

    def get_destination(self, line: int) -> str:
        return self.__bus_routes[line].get_destination()

    def get_stops(self, line: int) -> str:
        return self.__bus_routes[line].get_stops()

    def get_journey(self, line: int) -> str:
        return self.__bus_routes[line].get_journey()

    @staticmethod
    def get_ride_id(ride: ScheduledRide) -> int:
        return ride.get_ride_id()

    def get_ride_by_id(self, line: int, ride_id: int) -> ScheduledRide:
        for ride in self.__scheduled_rides[line]:
            if ride.get_ride_id() == ride_id:
                return ride

    def delete_route(self, line: int) -> None:
        self.__bus_routes.pop(line)

    def update_route(self, line: int, attribute: str, new_value) -> None:
        route: BusRoute = self.__bus_routes[line]
        match attribute:
            case 'Origin':
                route.set_origin(new_value)
            case 'Destination':
                route.set_destination(new_value)
            case 'Middle Stops':
                route.set_stops(new_value)

    def add_route(self, line: int, origin: str, destination: str, stops: str) -> bool:
        try:
            if line in self.__bus_routes.keys():
                raise LineAlreadyExists()
            self.__bus_routes[line] = BusRoute(line, origin, destination, stops)
            return True
        except LineAlreadyExists as error:
            print(error)
            return False

    def add_scheduled_ride(self, line: int, origin: str, destination: str, driver: str) -> None:
        scheduled_ride: ScheduledRide = ScheduledRide(self.__ride_id, origin, destination, driver)
        self.__ride_id += 1
        if line in self.__scheduled_rides:
            self.__scheduled_rides[line].append(scheduled_ride)
        else:
            self.__scheduled_rides[line] = [scheduled_ride]
        self.__bus_routes[line].add_scheduled_ride(scheduled_ride)

    @staticmethod
    def add_delay(ride: ScheduledRide) -> None:
        ride.add_delay()

    def __str__(self):
        return f"- Name: \'{self.__name}\'\n\
- Bus Routes: {self.__bus_routes}\n\
- Scheduled Rides: {self.__scheduled_rides}"

    def __repr__(self):
        return f"Name: \'{self.__name}\', \
Bus Routes: {self.__bus_routes}, \
Scheduled Rides: {self.__scheduled_rides}"
