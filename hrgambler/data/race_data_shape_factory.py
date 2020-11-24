from hrgambler.data.framework.factory import Factory
from hrgambler.data.race_data_shape import RaceDataShape
from hrgambler.data.csv_loader import Loader


class RaceDataShapeFactory(Factory):
    def __init__(self):
        self.__loader = None

    def _create_shape(self, loader: Loader):
        self.__loader = loader
        self.__loader.data_load()
        return RaceDataShape(csv_row_data=loader.row_data)

    def __del__(self):
        self.__loader.close_file()

