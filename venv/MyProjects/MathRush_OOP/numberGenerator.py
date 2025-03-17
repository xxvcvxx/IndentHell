import random


class NumberGenerator:

    def __init__(self):
        random_three_digit_numer = random.randint(101,999)
        print(random_three_digit_numer)

    @staticmethod
    def pick_numbers():
        big_numbers = [25, 50, 75, 100]
        list_number = []
        while True:
            try:
                choice = int(input("How many big numbers (0-4)? "))
                if 0 <= choice <= 4:
                    for i in range(choice):
                        list_number.append(random.choice(big_numbers))
                    for i in range(6 - choice):
                        list_number.append(random.randint(1, 10))
                    return list_number
                else:
                    print("Please enter a number between 0 and 4!")
            except ValueError:
                print("Error! Please enter a valid number.")


def perform_calculation(self):
    pass