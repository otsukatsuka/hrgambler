from abc import ABCMeta, abstractmethod


class Converter(metaclass=ABCMeta):

    @abstractmethod
    def convert(self, val):
        pass

    @abstractmethod
    def revert(self, val):
        pass
