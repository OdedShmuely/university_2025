from Personality import Personality

from Explosive import Explosive
from Furious import Furious
from Angry import Angry


class TypeA(Personality):
    def __init__(self):
        pass
    def adjust_mood(self, mood, waiting_time):
        if waiting_time > 40:
            return Explosive
        if waiting_time > 30 and mood != Explosive:
            return Furious
        if waiting_time > 20 and mood is not (Furious or Explosive):
            return Angry
        return mood

    def __repr__(self):
        return 'TypeA'
