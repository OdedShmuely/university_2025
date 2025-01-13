from Mood import Mood

class Chill(Mood):
    def __init__(self, strength=2, chill_modifier=0.5):
        super().__init__(strength)
        self.chill_modifier = chill_modifier  ######### check only between 0 to 1

    def get_patience_factor(self, waiting_time):
        factor = round(1.05 ** (waiting_time / 5) * self.strength * self.chill_modifier, 2)
        return factor

    def __repr__(self):
        return 'Chill'