from enum import IntFlag, auto


class DataType(IntFlag):
    RACE = auto()
    HORSE = auto()

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
