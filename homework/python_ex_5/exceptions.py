from Dish import Dish

class NoSuchIngredientException(Exception):
    def __init__(self, ingredient):
        self.ingredient = ingredient

    def __str__(self):
        error_text = f'Error:\n”{self.ingredient}” is an invalid ingredient.'
        return error_text

class NotCustomerDishException(Exception):
    def __init__(self, suggested_dish, expected_dish):
        self.suggested_dish = suggested_dish
        self.expected_dish = expected_dish

    def __str__(self):
        error_txt = f'Error:\nThe suggested dish:\t{self.suggested_dish}\nis not as expected:\t{self.expected_dish}.'
        return error_txt

class NoSuchOrderException(Exception):
    def __init__(self, order_id):
        self.order_id = order_id
    def __str__(self):
        error_txt = f'Error:\nOrderID: “{self.order_id}” does not exist.'
        return error_txt

class OrderOutOfBoundsException(Exception):
    pass
'''
try:
    raise NoSuchIngredientException("banana")
except Exception as e:
    print(e)

try:
    raise NotCustomerDishException(Dish(['a']), Dish(['a','b']))
except Exception as e:
    print(e)

try:
    raise OrderOutOfBoundsException
except Exception as e:
    print("Caught the exception")

aa = 5
try:
    if aa < 6:
        raise NotCustomerDishException
except Exception as e:
    print(e)

finally:
    print('i survived')
'''