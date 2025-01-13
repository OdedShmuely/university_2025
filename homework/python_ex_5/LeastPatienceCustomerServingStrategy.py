from ServingStrategy import ServingStrategy
from exceptions import OrderOutOfBoundsException

class LeastPatienceCustomerServingStrategy(ServingStrategy):

    def select_next_order(self, orders):
        """
        chosen patience is a none type and chosen key are temp variables to help go over all the orders,
        key set to base value of -1 because the keys are always positive. and patience to None for a first base case
        :param orders: gets the dict with the orders keys and customer and dish per order
        :return: the key of the next order in line according to the patience levels of the customer
        """
        if len(orders) == 0: #exception if orders is empty
            raise OrderOutOfBoundsException
        chosen_patience = None
        chosen_key = -1

        for key in orders:
            order = orders[key]
            customer = order[0]
            current_patience_per_key = customer.get_patience() # Define customer patience
            if (chosen_patience is None) or (current_patience_per_key < chosen_patience):
                chosen_patience = current_patience_per_key
                chosen_key = key
                continue
            if current_patience_per_key == chosen_patience:
                chosen_key = min (key, chosen_key)
            pass
        return chosen_key