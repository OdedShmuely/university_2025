from Mood import Mood
from Angry import Angry

class Furious(Mood):
    def __init__(self, strength = 2):
        super().__init__(strength)

    def get_patience_factor(self, waiting_time):
        factor = Angry(self.strength).get_patience_factor(waiting_time)*2
        return factor

    def __repr__(self):
        return 'Furious'

'''
furi = Furious(3)
print(furi.get_patience_factor(15))
'''