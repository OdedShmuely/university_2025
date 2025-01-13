import time

from FalafelStall import FalafelStall
from Dish import Dish
from Customer import Customer
from LeastPatienceCustomerServingStrategy import LeastPatienceCustomerServingStrategy
from ArrivalTimeServingStrategy import ArrivalTimeServingStrategy
from LongestWaitingTimeServingStrategy import LongestWaitingTimeServingStrategy
from exceptions import NoSuchIngredientException, NotCustomerDishException, NoSuchOrderException
from exceptions import OrderOutOfBoundsException


class Game:

    def __init__(self, orders_strategy, serving_strategy, ingredient_prices):
        self.orders_strategy = orders_strategy
        self.serving_strategy = serving_strategy
        self.ingredient_prices = ingredient_prices
        self.game_start = int(time.time())
        self.__lives = 3
        self.ingredient_dictionary = {}

    def get_lives(self):
        return self.__lives

    def get_game_duration(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        game_duration = current_time - self.game_start
        return game_duration

    def run(self):
        falafelia = FalafelStall(self.orders_strategy,self.ingredient_prices)
        ingredient_lst = [key for key in falafelia.ingredient_prices]
        for i in range(len(falafelia.ingredient_prices)): # fill ingredient list
            self.ingredient_dictionary[str(i)] = ingredient_lst[i]
        try:
            while self.__lives > 0:
                orders_lst_to_dict = next(falafelia.strategy)
                for order in orders_lst_to_dict: #give
                    falafelia.order(order[0],order[1])
                next_desired_order_id = self.serving_strategy.select_next_order(falafelia.get_orders())
                desired_order = falafelia.get_order(next_desired_order_id)
                desired_dish = desired_order[1]
                desired_customer = desired_order[0]
                print(f'Customer: \n{desired_customer}\nDish: {desired_dish}')
                print_dictionary = 'Insert ingredients:\n'
                for i in range(len(self.ingredient_dictionary)):
                    print_dictionary = f'{print_dictionary}{i}: {self.ingredient_dictionary[str(i)]}\n'
                while True:
                    print(print_dictionary)
                    try:
                        composed_dish = Dish()
                        input_str_lst = input().split()
                        for digit in input_str_lst:
                            # ' check if all the ingredients in the user dish is in the dictionary '
                            if digit in self.ingredient_dictionary:
                                composed_dish.add_ingredient(self.ingredient_dictionary[digit])
                                pass
                            else:
                                raise NoSuchIngredientException('')
                                pass
                        break

                    except NoSuchIngredientException as e:
                        print(f'Failed to create a Dish\n{e}\nPlease retry.')
                try:
                    falafelia.serve_dish(next_desired_order_id,composed_dish)
                    falafelia.remove_order(next_desired_order_id)
                except NoSuchOrderException as e:
                    print(e)
                except NotCustomerDishException as e:
                    print(f'Failed to serve a Dish to customer\n{e}')
                for i in falafelia.get_orders():
                    customer = falafelia.get_orders()[i][0]
                    customer.update()
                    if customer.get_patience()<=0:
                        falafelia.remove_order(i)
                        self.__lives -= 1
        except OrderOutOfBoundsException:
            print('no more orders')
        print(f'Game Over\nScores: {falafelia.get_earning()}')




'''

ingredient_dictionary = {0: 'green salad', 1:'falafel',2:'french fries',3:'coleslaw',4:'fried eggplants',5:'tachina',6:'humus'}

print_dictionary = 'Insert ingredients:\n'
for i in range(len(ingredient_dictionary)):
    print_dictionary = f'{print_dictionary}{i}: {ingredient_dictionary[i]}\n'
print(print_dictionary)

'''