from enum import Enum


class GenderType(Enum):
    STALLION = '牡'
    MARE = '牝'
    gelding = 'セ'

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        if isinstance(other, str):
            return self.value == other
        return False

    @staticmethod
    def from_key(key):
        for gt in GenderType:
            if gt.__eq__(key):
                return gt
