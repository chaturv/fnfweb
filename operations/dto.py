# Data Transfer Objects. Not Models


class DishQuantities:

    def __init__(self, dish_id, dish_name, dish_qty):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.dish_qty = dish_qty


class IngredientShoppingList:

    def __init__(self, ingredient_name, total_ingredient_weight, total_cost_price):
        self.ingredient_name = ingredient_name
        self.total_ingredient_weight = total_ingredient_weight
        self.total_cost_price = total_cost_price
