from abc import ABCMeta, abstractmethod
from hrgambler.data.csv_loader import Loader


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def _create_shape(self, loader: Loader):
        pass

    def create(self, loader):
        self.__s = self._create_shape(loader)
        return self.__s

