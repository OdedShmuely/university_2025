
from OrderStrattegy import OrderStrategy
from Dish import Dish
from Customer import Customer

class FixedOrdersStrategy(OrderStrategy):
    def __init__(self,  lst_orders):
        self.lst_orders = lst_orders
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.lst_orders):
            raise StopIteration
        orders_to_return = self.lst_orders[self.index-1]
        self.index += 1
        return orders_to_return



'''
test = FixedOrdersStrategy([[[1,'falafel'],[1,'falafel'],[1,'falafel'],[1,'falafel']], [[1,'falafel'],[1,'falafel']] ])
for i in tests:
    print(test.__next__())
'''