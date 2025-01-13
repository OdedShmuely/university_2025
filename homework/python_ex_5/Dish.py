class Dish:
    def __init__(self, ingredients = None):
        self.__ingredients = ingredients if ingredients else []

    def add_ingredient(self, ingredient):
        self.__ingredients.append(ingredient)

    def get_ingredients(self):
        return self.__ingredients

    def __eq__(self, other):
        other_ing_copy = [ingredient for ingredient in other.__ingredients]
        if not isinstance(other, Dish):
            return False
        if not isinstance(self,Dish):
            return False
        if len(self.__ingredients) != len(other.__ingredients):
            return False
        for item in self.__ingredients:
            if item not in other_ing_copy:
                return False
            other_ing_copy.remove(item)
        return True

    def __repr__(self):
        to_print = ', '.join(ingredient for ingredient in self.__ingredients)
        return f'* {to_print} *'


'''tests'''
# dish1 = Dish(['humus', 'french fries', 'bacon'])
# dish1.add_ingredient('falafel')
# dish2 = Dish(['humus', 'french fries', 'bacon', 'falafel'])
# print(dish2 == dish1)
# print(dish1)