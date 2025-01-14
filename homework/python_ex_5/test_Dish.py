from unittest import TestCase
from Dish import Dish


class TestInit(TestCase):
    def test_empty_dish(self):
        self.dish = Dish()
        self.assertEqual(self.dish._Dish__ingredients,[])
    def test_non_empty_dish(self):
        self.not_empty_dish = Dish(['humus','falafel'])
        self.assertEqual(self.not_empty_dish._Dish__ingredients,['humus','falafel'])

class TestAddIngredient(TestCase):
    def add_1_ingredient(self):
        self.dish = Dish()
        self.dish.add_ingredient('falafel')
        self.assertEqual(self.dish.get_ingredients(),['falafel'])

    def test_add_3_ingredients(self):
        self.dish = Dish()
        for i in range(1,4):
            self.dish.add_ingredient('a'*i)
        self.assertEqual(self.dish.get_ingredients(),['a','aa','aaa'])

class TestGetIngredient(TestCase):
    def test_on_empty_dish(self):
        self.dish = Dish()
        self.assertEqual(self.dish.get_ingredients(),[])
    def test_non_empty_dish(self):
        self.not_empty_dish = Dish(['humus','falafel'])
        self.assertEqual(self.not_empty_dish.get_ingredients(),['humus','falafel'])

class TestEqual(TestCase):
    def test_equal_humus_and_humus(self):
        self.dish1 = Dish(['humus'])
        self.dish2 = Dish(['humus'])
        self.assertEqual(self.dish1,self.dish2)
    def test_not_equal_humus_falafel_and_humus(self):
        self.dish1 = Dish(['falafel','humus'])
        self.dish2 = Dish(['humus'])
        self.assertEqual(self.dish1,self.dish2,'Not equal')

