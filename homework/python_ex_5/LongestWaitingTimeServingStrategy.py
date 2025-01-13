import time
from ServingStrategy import ServingStrategy
from Customer import Customer
from exceptions import OrderOutOfBoundsException


class LongestWaitingTimeServingStrategy(ServingStrategy):
    def select_next_order(self, orders):
        """
        chosen waiting time and chosen key are temp variables to help go over all the orders,
        both set to base values of -1 because the time and keys are always positive.
        :param orders: gets the dict with the orders keys and customer and dish per order
        :return: the key of the next order in line according to the waiting time of the customer
        """
        if len(orders) == 0: #exception if orders is empty
            raise OrderOutOfBoundsException
        chosen_waiting_time = -1
        chosen_key = -1
        for key in orders:
            order = orders[key]
            customer = order[0]
            waiting_time_per_key = customer.get_waiting_time() # Define customer waiting time
            if waiting_time_per_key > chosen_waiting_time:
                chosen_waiting_time = waiting_time_per_key
                chosen_key = key
                continue
            if waiting_time_per_key == chosen_waiting_time:
                chosen_key = min (key, chosen_key)
            pass

        return chosen_key
