import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_in_game = []


def draw_cards():
    if len(cards) == 0:
        return "end"

    card = random.choice(cards)
    cards.remove(card)
    cards_in_game.append(card)
    return card


def calculate_score(list):
    if 11 in list and sum(list) > 21:
        index = list.index(11)
        list[index] = 1
        print("Ace is 1 now")
    total = sum(list)
    if total == 21:
        return 0
    elif total > 21:
        return -1
    else:
        return total


user_cards = [draw_cards(), draw_cards()]
computer_cards = [draw_cards(), draw_cards()]

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards: {user_cards}")
print(f"Computers cards: [{computer_cards[0]}, _]")

if user_score == 0 or computer_score == 0 or user_score == -1:
    print("END!")
else:
    choice = input("Y/N")
    if choice == 'y':
        user_cards.append(draw_cards())
        calculate_score(user_cards)
