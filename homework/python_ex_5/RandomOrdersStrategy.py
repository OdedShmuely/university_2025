import random
from OrderStrattegy import OrderStrategy
from random import choice
from random import choices
from random import random, randint
from Mood import Mood
from Personality import Personality
from Customer import Customer
from Dish import Dish


class RandomOrdersStrategy(OrderStrategy):
    def __init__(self, max_dishes, max_ingredients, ingredients, n_orders=-1):
        self.current = 0
        self.n_orders = n_orders
        self.max_dishes = max_dishes
        self.ingredients = ingredients
        self.max_ingredients = max_ingredients
        self.__runner = n_orders

    def __iter__(self):
        self.runner = self.n_orders #############
        return self


    def __next__(self):
        if self.__runner == 0:
            raise StopIteration
        ### reset current?
        orders_quantity = randint(1,self.max_dishes) # including max dishes
        lst_of_orders_rnd = []
        for _ in range(orders_quantity):
            self.current += 1
            customers_mood = choice(Mood.__subclasses__())
            customers_personality = choice(Personality.__subclasses__())
            customer_name = self.current
            ingredients_num = randint(1,self.max_ingredients)
            dish_ingredients = choices(self.ingredients, k=ingredients_num)
            new_customer = Customer(customer_name,customers_mood,customers_personality)
            new_dish = Dish(dish_ingredients)
            order = (new_customer,new_dish)
            lst_of_orders_rnd.append(order)
        self.__runner-=1
        return lst_of_orders_rnd

'''
test = RandomOrdersStrategy(2,2,['humus', 'french fries', 'bacon'])
# for i in range(5):
print(test.__next__())
'''