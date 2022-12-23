class Address:

    def __init__(self, country: str, city: str, street: str, house: int, flat: int):
        self.country: str = country
        self.city: str = city
        self.street: str = street
        self.house: int = house
        self.flat: int = flat


class Bathroom:

    def __init__(self, size: int, toilet: bool, sink: bool, bath: bool, shower: bool):
        self.size: int = size
        self.toilet: bool = toilet
        self.sink: bool = sink
        self.bath: bool = bath
        self.shower: bool = shower


class Flat:

    def __init__(self, address: Address, floor: int, floors_in_building: int,
                 rooms: list[int], bathrooms: list[Bathroom],
                 kitchen: int, balconies: list[int], size: int):
        self.address: Address = address
        self.floor: int = floor
        self.floors_in_building: int = floors_in_building
        self.rooms: list[int] = rooms
        self.bathrooms: list[Bathroom] = bathrooms
        self.kitchen: int = kitchen
        self.balconies: list[int] = balconies
        self.size: int = size

    def get_number_of_rooms(self):
        return len(self.rooms)

    def get_total_living_space(self):
        return sum(self.rooms)

    def get_total_bathroom_space(self):
        return sum([i.size for i in self.bathrooms])

    def get_total_balcony_space(self):
        return sum(self.balconies)

    def get_annual_arnona(self, monthly_tarif: float):
        arnona: float = 12 * \
                        (monthly_tarif * (self.get_total_living_space() +
                                          self.get_total_bathroom_space()) +
                         0.75 * monthly_tarif * self.get_total_balcony_space())
        return arnona
