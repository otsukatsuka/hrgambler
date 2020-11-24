from hrgambler.enums.gender_type import GenderType
from hrgambler.converter.converter import Converter


class GenderAgeConverter(Converter):

    def convert(self, val) -> tuple:
        obj = GenderType.from_key(val[0])
        return obj, int(val[1])

    def revert(self, val):
        pass

