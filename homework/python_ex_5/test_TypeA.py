from unittest import TestCase
from TypeA import TypeA
from Explosive import Explosive
from Angry import Angry
from Furious import Furious
from Calm import Calm

class TestTypeA(TestCase):
    def setUp(self):
        self.test_type_a = TypeA()

class TestInit(TestTypeA):
    def test_angry_w_t35(self):
        self.assertIsInstance(self.test_type_a.adjust_mood(Angry(),35),Furious)
    def test_explosive_w_t35(self):
        self.assertIsInstance(self.test_type_a.adjust_mood(Explosive(),35),Explosive)
    def test_calm_w_t25(self):
        self.assertIsInstance(self.test_type_a.adjust_mood(Calm(),25),Angry)

