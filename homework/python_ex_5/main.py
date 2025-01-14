from Angry import Angry
from Calm import Calm
from TypeB import TypeB
from TypeA import TypeA
from Customer import Customer
from Dish import Dish
from Explosive import Explosive
from Furious import Furious
from Chill import Chill
from LeastPatienceCustomerServingStrategy import LeastPatienceCustomerServingStrategy
from Game import Game
from RandomOrdersStrategy import RandomOrdersStrategy
from FixedOrdersStrategy import FixedOrdersStrategy
from python_ex_5.ArrivalTimeServingStrategy import ArrivalTimeServingStrategy

INGREDIENTS_PRICES = { 'green salad': 3,
                       'falafel': 5,
                       'french fries': 4,
                       'coleslaw': 2,
                       'fried eggplants': 3,
                       'tachina': 0,
                       'humus': 1
                       }
lst_orders = [
    [
        (Customer(0, Angry(), TypeB()), Dish(['french fries', 'humus', 'humus', 'humus'])),
        (Customer(1, Angry(), TypeB()), Dish(['humus', 'fried eggplants', 'fried eggplants', 'falafel']))
    ],
    [
        (Customer(2, Explosive(), TypeB()), Dish(['french fries', 'humus', 'fried eggplants'])),
        (Customer(3, Furious(), TypeA()), Dish(['french fries', 'falafel', 'fried eggplants', 'fried eggplants'])),
        (Customer(4, Calm(), TypeA()), Dish(['humus', 'coleslaw'])), (Customer(5, Furious(), TypeA()), Dish(['humus'])),
        (Customer(6, Chill(), TypeB()), Dish(['fried eggplants']))
    ],
    [
        (Customer(7, Chill(), TypeB()), Dish(['falafel', 'humus', 'humus'])),
        (Customer(8, Calm(), TypeA()), Dish(['fried eggplants', 'french fries', 'fried eggplants', 'falafel'])),
        (Customer(9, Angry(), TypeA()), Dish(['fried eggplants'])),
        (Customer(10, Angry(), TypeB()), Dish(['humus', 'fried eggplants', 'tachina', 'falafel']))
    ]
]


# order_strategy = FixedOrdersStrategy(lst_orders)
order_strategy = RandomOrdersStrategy(3, 2, list(INGREDIENTS_PRICES.keys()), -1)
serving_strategy = ArrivalTimeServingStrategy()
g = Game(order_strategy, serving_strategy, INGREDIENTS_PRICES)
g.run()
