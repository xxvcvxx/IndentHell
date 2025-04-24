from coffeeMachine import recipes, resources
from coffeeApp import CoffeeApp

def show_menu():

    option = {
        "1": "Brew coffee",
        "2": "Refill ingredient",
        "3": "Show resources",
        "4": "Exit"
        }

    while True:
        for key, label in option.items():
            print(f"{key}. {label}")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Available coffees: " + ", ".join(recipes))
            coffee = input("Select coffee type: ").strip()
            if coffee in recipes:
                CoffeeApp.brew(coffee, recipes, resources)
            else:
                print("Unknown coffee type. Please choose again.")

        if choice == "2":
            ingredient = input("Ingredient name: ").strip()
            try:
                amount = int(input("Amount to add: ").strip())
                CoffeeApp.add_ingredient(ingredient, amount, resources)
            except ValueError:
                print("Amount must be an integer.")

        if choice == "3":
            CoffeeApp.show_resources(resources)

        if choice == "4":
            print("Bye")
            print("""     ( (
      ) )
   ........
   |      |]
   \      /  
    `----'
""")

show_menu()