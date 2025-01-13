import abc
from abc import ABC


class OrderStrategy(ABC):

    @abc.abstractmethod
    def __iter__(self):
        pass

    @abc.abstractmethod
    def __next__(self):
        pass