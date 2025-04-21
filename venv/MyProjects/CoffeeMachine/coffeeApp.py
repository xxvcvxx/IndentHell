from coffeeMachine import recipes, resources
from typing import Dict

class CoffeApp:
    @staticmethod
    def brew(coffee_type: str, recipes: dict, resources: dict):
        recipe = recipes[coffee_type]
        for ingredien, amount in recipe.items():
            if resources[ingredien] < amount:
                print(f"Not enough {ingredient}")
                return
        for ingredient, amount in recipe.items():
            resources[ingredient] -= amount
        print("Here is your coffee!")