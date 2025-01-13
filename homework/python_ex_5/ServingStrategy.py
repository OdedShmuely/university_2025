import abc
from abc import ABC

class ServingStrategy(ABC):
    @abc.abstractmethod
    def select_next_order(self, orders):
        pass