import random

random_number = random.randint(1, 100)

level = {
    "E": 10,
    "M": 7,
    "D": 5}


def check_number(number1, random_number1):
    if random_number1 == number1:
        print("Congratulations! You've guessed the number.")
    elif random_number1 > number1:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


user_choice = input("Enter your choice Easy(E), Medium(M), Difficult(D): ").capitalize()
attempts = level[user_choice]
number = None

while attempts > 0:
    number = int(input("Guess a number: "))
    check_number(number, random_number)
    if number == random_number:
        break
    attempts -= 1
    if attempts == 0:
        print(f"You lost! The correct number was {random_number}.")
    print(f"Attempts left: {attempts}")
