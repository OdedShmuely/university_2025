import abc
from abc import ABC
class Mood(ABC):
    def __init__(self, strength = 2):
        self.strength = strength  ######## check minus inputs

    @abc.abstractmethod
    def get_patience_factor(self, waiting_time):
        pass
