from typing import Dict

class CoffeeApp:
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
        if ingredient in resources:
            resources[ingredient] += amount
            print(f"{ingredient} has been added")
            print( resources[ingredient])
        else:
            print("Unknown ingredient type. Please choose again.")

    @staticmethod
    def show_resources(resources: dict):
        print("\nCurrent resources:")
        for ingredient, amount in resources.items():
            print(f"{ingredient.capitalize()}: {amount}")


