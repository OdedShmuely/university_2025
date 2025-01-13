import abc
from abc import ABC
class Personality(ABC):
    @abc.abstractmethod
    def adjust_mood(self, mood, waiting_time):
        pass
