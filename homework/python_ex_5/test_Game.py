from contextlib import redirect_stdout
from unittest import TestCase
from Angry import Angry
from ArrivalTimeServingStrategy import ArrivalTimeServingStrategy
from Calm import Calm
from Chill import Chill
from Customer import Customer
from Explosive import Explosive
from Furious import Furious
from LeastPatienceCustomerServingStrategy import LeastPatienceCustomerServingStrategy
from FixedOrdersStrategy import FixedOrdersStrategy
from LongestWaitingTimeServingStrategy import LongestWaitingTimeServingStrategy
from TypeA import TypeA
import sys
from io import StringIO
from unittest.mock import MagicMock, patch, call
from Game import Game
from Dish import Dish
from TypeB import TypeB


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

    def has_calls(self, mock_obj, expected_calls, any_order=False):
        try:
            mock_obj.assert_has_calls(expected_calls, any_order=any_order)
            return True
        except AssertionError:
            return False


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

        list_inputs = ['2 6 6 6'] # each input in a different cell
        output = self.simulate_game(g, list_inputs)
        self.assertTrue(output in {'Customer:\n**********************\n* name: 0            *\n* mood: Angry        *\n* personality: TypeA *\n* patience: 100      *\n**********************\nDish: * french fries, humus, humus, humus *\nInsert ingredients:\n0: green salad\n1: falafel\n2: french fries\n3: coleslaw\n4: fried eggplants\n5: tachina\n6: humus\nGame Over\nscore: 7.0\n',
                                   'Customer:\n**********************\n* name: 0            *\n* mood: Angry        *\n* personality: TypeA *\n* patience: 100.0    *\n**********************\nDish: * french fries, humus, humus, humus *\nInsert ingredients:\n0: green salad\n1: falafel\n2: french fries\n3: coleslaw\n4: fried eggplants\n5: tachina\n6: humus\nGame Over\nscore: 7.0\n'})


def infinite_time_mock(start, step = 2):
    base_time = start
    while True:
        yield base_time
        base_time += step  # Increment by 2 seconds for each call


class TestGameSimulation(TestGame):
    @patch("time.time", side_effect=infinite_time_mock(1735511760))
    def setUp(self, mock_time):
        self.ingredient_prices = {
            'green salad': 3,
            'falafel': 5,
            'french fries': 4,
            'coleslaw': 2,
            'fried eggplants': 3,
            'tachina': 0,
            'humus': 1
        }

        self.lst_orders = [
            [
                (Customer(0, Angry(), TypeB()), Dish(['french fries', 'humus', 'humus', 'humus'])),
                (Customer(1, Angry(), TypeB()), Dish(['humus', 'fried eggplants', 'fried eggplants', 'falafel']))
            ],
            [
                (Customer(2, Explosive(), TypeB()), Dish(['french fries', 'humus', 'fried eggplants'])),
                (Customer(3, Furious(), TypeA()),
                 Dish(['french fries', 'falafel', 'fried eggplants', 'fried eggplants'])),
                (Customer(4, Calm(), TypeA()), Dish(['humus', 'coleslaw'])),
                (Customer(5, Furious(), TypeA()), Dish(['humus'])),
                (Customer(6, Chill(), TypeB()), Dish(['fried eggplants']))
            ],
            [
                (Customer(7, Chill(), TypeB()), Dish(['falafel', 'humus', 'humus'])),
                (Customer(8, Calm(), TypeA()), Dish(['fried eggplants', 'french fries', 'fried eggplants', 'falafel'])),
                (Customer(9, Angry(), TypeA()), Dish(['fried eggplants'])),
                (Customer(10, Angry(), TypeB()), Dish(['humus', 'fried eggplants', 'tachina', 'falafel']))
            ]
        ]


    @patch("Game.time.time", side_effect=infinite_time_mock(1735511760, 2))
    def test_game_run_19(self, mock_time):
        orders_strategy = FixedOrdersStrategy(self.lst_orders)
        serving_strategy = LeastPatienceCustomerServingStrategy()
        game = Game(orders_strategy, serving_strategy, self.ingredient_prices)
        expected_calls1 = [call('Customer:\n**********************\n* name: 0            *\n* mood: Angry        *\n* personality: TypeB *\n* patience: 100      *\n**********************\nDish: * french fries, humus, humus, humus *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Failed to serve a Dish to customer\nError:\nThe suggested dish:\t* humus, fried eggplants, fried eggplants, falafel *\nis not as expected:\t* french fries, humus, humus, humus *.'),
                           call('Customer:\n**********************\n* name: 0            *\n* mood: Angry        *\n* personality: TypeB *\n* patience: 93.66    *\n**********************\nDish: * french fries, humus, humus, humus *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Customer:\n**********************\n* name: 3            *\n* mood: Furious      *\n* personality: TypeA *\n* patience: 85.9     *\n**********************\nDish: * french fries, falafel, fried eggplants, fried eggplants *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Customer:\n**********************\n* name: 2            *\n* mood: Explosive    *\n* personality: TypeB *\n* patience: 56.27    *\n**********************\nDish: * french fries, humus, fried eggplants *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Customer:\n**********************\n* name: 4            *\n* mood: Explosive    *\n* personality: TypeA *\n* patience: 44.86    *\n**********************\nDish: * humus, coleslaw *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Game Over'),
                           call('score: 33.0')]

        expected_calls2 = [call('Customer:\n**********************\n* name: 0            *\n* mood: Angry        *\n* personality: TypeB *\n* patience: 100.0    *\n**********************\nDish: * french fries, humus, humus, humus *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Failed to serve a Dish to customer\nError:\nThe suggested dish:\t* humus, fried eggplants, fried eggplants, falafel *\nis not as expected:\t* french fries, humus, humus, humus *.'),
                           call('Customer:\n**********************\n* name: 0            *\n* mood: Angry        *\n* personality: TypeB *\n* patience: 93.66    *\n**********************\nDish: * french fries, humus, humus, humus *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Customer:\n**********************\n* name: 3            *\n* mood: Furious      *\n* personality: TypeA *\n* patience: 85.9     *\n**********************\nDish: * french fries, falafel, fried eggplants, fried eggplants *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Customer:\n**********************\n* name: 2            *\n* mood: Explosive    *\n* personality: TypeB *\n* patience: 56.27    *\n**********************\nDish: * french fries, humus, fried eggplants *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Customer:\n**********************\n* name: 4            *\n* mood: Explosive    *\n* personality: TypeA *\n* patience: 44.86    *\n**********************\nDish: * humus, coleslaw *'),
                           call('Insert ingredients:'),
                           call('0: green salad'),
                           call('1: falafel'),
                           call('2: french fries'),
                           call('3: coleslaw'),
                           call('4: fried eggplants'),
                           call('5: tachina'),
                           call('6: humus'),
                           call('Game Over'),
                           call('score: 33.0')]

        with patch("Customer.time.time", side_effect=infinite_time_mock(1735511782, 2)):
            with patch("builtins.input",
                       side_effect=["6 4 4 1", "2 6 6 6", "1 2 4 4", "2 6 4", "6 3", "2 4 6", "2 4 6", "6 3"] * 10):
                with patch("builtins.print") as mock_print:
                    game.run()

        option1 = self.has_calls(mock_print, expected_calls1, any_order=True)
        option2 = self.has_calls(mock_print, expected_calls2, any_order=True)
        self.assertTrue(option1 or option2)