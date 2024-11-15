import random


stages = ['''
 +---+
 |   |
     |
     |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


words = [
    "apple", "banana", "grape", "orange", "cherry",
    "peach", "pear", "plum", "lemon", "lime",
    "mango", "papaya", "kiwi", "melon", "strawberry",
    "blueberry", "raspberry", "blackberry", "coconut", "pineapple",
    "dragonfruit", "watermelon", "fig", "apricot", "grapefruit",
    "nectarine", "pomegranate", "cranberry", "guava", "meep"
]
random_word = random.choice(words)
word_lenght = len(random_word)
letters = ["_"] * len(random_word)
live = 6


print(random_word)  # Do skasowania


print("Word", end=":")
print("".join(letters))




def letterfinder():
    global live
    max_live = 6
    letter = input("Prosze o literke:").lower()
    found = False
    for i in range(word_lenght):
        if letter == random_word[i]:
            letters[i] = letter
            found = True
    if not found:
        live -= 1


    print(stages[max_live-live])


    print("".join(letters))




while "_" in letters and live > 0:
    letterfinder()
    print(live)


if "_" not in letters:
    print("Gratulacje, odgadłeś słowo!")
else:
    print("Niestety, nie odgadłeś całego słowa.")

