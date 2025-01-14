from unittest import TestCase
from Calm import Calm
from Customer import Customer
from TypeA import TypeA


class TestCalm(TestCase):
    def setUp(self):
        self.calm_instance = Calm()
        self.customer_instance = Customer('test',self.calm_instance,TypeA,100,5)

class TestInit(TestCalm):
    def test_initialization(self):
        self.assertEqual(self.calm_instance.strength,2)

class TestGetPatienceFactor(TestCalm):
    def test_strength_3(self):
        self.calm_instance.strength = 3
        self.assertEqual(self.calm_instance.get_patience_factor(self.customer_instance.get_waiting_time(7)),3.06)
    def test_strength_4(self):
        self.calm_instance.strength = 4
        self.assertEqual(self.calm_instance.get_patience_factor(self.customer_instance.get_waiting_time(7)),4.08)
    def test_strength_2_waiting_time_4(self):
        self.assertEqual(self.calm_instance.get_patience_factor(self.customer_instance.get_waiting_time(9)),2.08)
