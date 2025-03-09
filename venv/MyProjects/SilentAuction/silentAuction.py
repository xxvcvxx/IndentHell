print("Welcome to the silent auction!")
transactions = {}


def add_transaction():
    user_name = input("Enter name: ")
    amount = input("Enter amount in $: ")

    while not amount.isdigit():
        print("The input is not a valid number.")
        amount = input("Enter amount in $: ")
    transactions[user_name] = amount


def select_winner():
    winner = {'name': '', 'value': 0}
    for key, value in transactions.items():
        value = int(value)
        if value > winner['value']:
            winner['name'] = key
            winner['value'] = value
    print(f"Winner!: {winner['name']} with the highest bid of ${winner['value']}")


while True:
    add_transaction()

    continue_response = input("Do you want to continue? (y/n): ").strip().lower()

    while continue_response != 'y' and continue_response != 'n':
        print("Invalid answer, please try again.")
        continue_response = input("Do you want to continue? (y/n): ").strip().lower()
    if continue_response == 'n':
        print("\n" * 100)
        break
    elif continue_response == 'y':
        print("Next person")
        print("\n" * 100)

select_winner()
