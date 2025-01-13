import copy
from Dish import Dish
from Customer import Customer
from exceptions import NoSuchIngredientException, NotCustomerDishException, OrderOutOfBoundsException, NoSuchOrderException



class FalafelStall:
    def __init__(self, strategy, ingredient_prices):
        self.__orders = {}
        self.strategy = strategy
        self.ingredient_prices = ingredient_prices
        self.__money = 0.0
        self.order_counter = 0

    def order(self, customer, dish):
        """
        add an order to the orders list, raises no ingredient if the one of the ingredients does not exist
        :param customer: Customer instance
        :param dish: Dish instance
        :return:
        """
        for ingredient in dish.get_ingredients():
            if ingredient not in self.ingredient_prices:
                raise NoSuchIngredientException(ingredient)
        self.order_counter += 1
        self.__orders[self.order_counter] = (customer,dish)
        return self.order_counter

    def get_next_order_id(self):
        try:
            next_order_id = self.strategy.select_next_order(self.get_orders())
            return next_order_id
        except OrderOutOfBoundsException:
            raise OrderOutOfBoundsException()

    def serve_dish(self, order_id, dish):
        if order_id not in self.__orders:
            raise NoSuchOrderException(order_id)
            pass
        if dish != self.__orders[order_id][1]:
            raise NotCustomerDishException(dish, self.__orders[order_id][1])
            pass
        else:
            self.__money += self.calculate_cost(dish) # add money to self money according to the price
            pass
        ######check that the order is being deleted

    def remove_order(self, order_id):
        if order_id not in self.__orders:
            raise NoSuchOrderException(order_id)
        self.__orders.pop(order_id)

    def get_order(self, order_id):
        if order_id not in self.__orders:
            raise NoSuchOrderException(order_id)
        order_selected = self.__orders[order_id]
        return order_selected

    def calculate_cost(self, dish):
        dish_cost = 0
        for ingredient in dish.get_ingredients():
            price = self.ingredient_prices[ingredient]
            if ingredient not in self.ingredient_prices:
                raise NoSuchIngredientException(ingredient)
                pass
            dish_cost += price
        return dish_cost

    def get_orders(self):
        return self.__orders

    def get_earning(self):
        return self.__money

