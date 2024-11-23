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


choice = 'y'
while choice == 'y':
    print(draw_cards())
    print(cards_in_game)
    choice = input("again:")
