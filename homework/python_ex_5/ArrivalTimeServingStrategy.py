import time

from ServingStrategy import ServingStrategy
from Customer import Customer
from exceptions import OrderOutOfBoundsException

class ArrivalTimeServingStrategy(ServingStrategy):

    def select_next_order(self, orders):
        """
        chosen arrive time and chosen key are temp variables to help go over all the orders,
        key is set to base value of -1 because the keys are always positive and time is set to None
        in order to change itself to int
        :param orders: gets the dict with the orders keys and customer and dish per order
        :return: the key of the next order in line according to the arrival time of the customer
        """
        if len(orders) == 0: #exception if orders is empty
            raise OrderOutOfBoundsException
        chosen_arrival_time = None
        chosen_key = -1
        for key in orders:
            order = orders[key]
            customer = order[0]
            arrival_time_per_key = customer.arrive_time
            if chosen_arrival_time is None or arrival_time_per_key < chosen_arrival_time:
                chosen_key = key
                chosen_arrival_time = arrival_time_per_key
                continue
            if  arrival_time_per_key == chosen_arrival_time: #######################
                chosen_key = min(key, chosen_key)
                pass
        return chosen_key
