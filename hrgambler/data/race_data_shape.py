from hrgambler.data.framework.shape import Shape
from typing import List
from hrgambler.enums.race_data_column_type import RaceDataColumnType


class RaceDataShape(Shape):
    def __init__(self, csv_row_data):
        self.__row_data = csv_row_data

    def specify_column(self, specify_list: List[RaceDataColumnType]):
        out = [{spec.ja: row[spec.column_order]} for row in self.__row_data for spec in specify_list]
        print(out)

    def all_column(self):
        out = [{col.ja: row[col.column_order]} for row in self.__row_data for col in RaceDataColumnType]
        print(out)