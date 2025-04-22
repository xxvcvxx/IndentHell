from coffeeMachine import recipes, resources
from typing import Dict

class CoffeApp:
    @staticmethod
    def brew(coffee_type: str, recipes: dict, resources: dict):
        recipe = recipes[coffee_type]
        missing_ingrediens = []

        for ingredient, amount in recipe.items():
            if resources[ingredient] < amount:
                missing_ingrediens.append(ingredient)

        if  missing_ingrediens:
            print(f"Missing ingredients: {', '.join(missing_ingrediens)}")
            return

        for ingredient, amount in recipe.items():
            resources[ingredient] -= amount
        print("Here is your coffee!")

    @staticmethod
    def add_ingredient(ingredient, amount, resources: dict):
        resources[ingredient] += amount
        print(f"{ingredient} has been added")
        print( resources[ingredient])
