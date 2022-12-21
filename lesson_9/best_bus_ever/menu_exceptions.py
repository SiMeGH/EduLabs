class MenuException(Exception):
    def __init__(self):
        super().__init__(f"{self.__class__.__name__}")


class WrongManagerPassword(MenuException):
    pass


class LineIsNotAPositiveInteger(MenuException):
    pass


class StringMustNotBeEmpty(MenuException):
    pass


class InputNotAnInteger(MenuException):
    pass


class InputOutOfRange(MenuException):
    pass


class InputNotInList(MenuException):
    pass


class InputNotMadeOfFiveCharacters(MenuException):
    pass


class InputMustContainExactlyOneSemicolon(MenuException):
    pass


class InputMustContainOneSemicolonInTheMiddle(MenuException):
    pass


class InputMustContainDigitsOnTheSides(MenuException):
    pass


class HoursCantBeHigherThan23(MenuException):
    pass


class MinutesCantBeHigherThan59(MenuException):
    pass
