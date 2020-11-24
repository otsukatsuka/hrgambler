from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def specify_column(self, specify_list: list):
        pass

    @abstractmethod
    def all_column(self):
        pass
