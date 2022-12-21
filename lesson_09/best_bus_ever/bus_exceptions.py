class BusException(Exception):
    def __init__(self):
        super().__init__(f"{self.__class__.__name__}")


class LineAlreadyExists(BusException):
    pass


class LineDoesNotExist(BusException):
    pass


class NoScheduledRidesForRoute(BusException):
    pass
