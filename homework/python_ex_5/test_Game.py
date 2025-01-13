from contextlib import redirect_stdout
from unittest import TestCase
from Angry import Angry
from Customer import Customer
from Dish import Dish
from LeastPatienceCustomerServingStrategy import LeastPatienceCustomerServingStrategy
from FixedOrdersStrategy import FixedOrdersStrategy
from Game import Game
from TypeA import TypeA
import sys
from io import StringIO


class TestGame(TestCase):

    def simulate_game(self, game, lst_input):
        stdout_buffer = StringIO()
        output = None
        with redirect_stdout(stdout_buffer):
            input_data = '\n'.join(lst_input)
            with StringIO(input_data) as test_input:
                original_stdin = sys.stdin
                sys.stdin = test_input
                try:
                    game.run()
                finally:
                    sys.stdin = original_stdin
            output = stdout_buffer.getvalue()
        return output


class TestRun(TestGame):
    def test_1(self):
        INGREDIENTS_PRICES = {'green salad': 3,
                              'falafel': 5,
                              'french fries': 4,
                              'coleslaw': 2,
                              'fried eggplants': 3,
                              'tachina': 0,
                              'humus': 1
                              }

        self.lst_orders = [
            [
                (Customer(0, Angry(), TypeA()), Dish(['french fries', 'humus', 'humus', 'humus']))
            ]
        ]
        self.random_strategy = FixedOrdersStrategy(self.lst_orders)
        self.serving_strategy = LeastPatienceCustomerServingStrategy()
        g = Game(self.random_strategy, self.serving_strategy, INGREDIENTS_PRICES)

        list_inputs = ['4 6 6 6'] # each input in a different cell
        output = self.simulate_game(g, list_inputs)
        self.assertEqual(output, 'Customer:\n**********************\n* name: 0            *\n* mood: Angry        *\n* personality: TypeA *\n* patience: 100      *\n**********************\nDish: * french fries, humus, humus, humus *\nInsert ingredients:\n0: green salad\n1: falafel\n2: french fries\n3: coleslaw\n4: fried eggplants\n5: tachina\n6: humus\nGame Over\nscore: 7.0\n')





