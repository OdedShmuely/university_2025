from Mood import Mood
class Explosive(Mood):
    def __init__(self, strength = 2):
        super().__init__(strength)

    def get_patience_factor(self, waiting_time):
        factor = round(1.3 ** ((waiting_time * self.strength)/ 5), 2)
        return factor

    def __repr__(self):
        return 'Explosive'