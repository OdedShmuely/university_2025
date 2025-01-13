from Mood import Mood

class Calm(Mood):

    def __init__(self, strength = 2):
        super().__init__(strength)

    def get_patience_factor(self, waiting_time):
        factor = round(1.05 ** (waiting_time / 5) * self.strength, 2)
        return factor

    def __repr__(self):
        return 'Calm'
