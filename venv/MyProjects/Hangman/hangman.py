import random
import hangman_stages
import hangman_words

random_word = random.choice(hangman_words.words)
word_length = len(random_word)
letters = ["_"] * len(random_word)
lives = 6

print(random_word)  # For debugging, can be removed

print("Word", end=": ")
print("".join(letters))

max_lives = lives


def letterfinder():
    global lives
    letter = input("Please enter a letter: ").lower()
    found = False
    for i, char in enumerate(random_word):
        if letter == char:
            letters[i] = char
            found = True
    if not found:
        lives -= 1

    print(hangman_stages.stages[max_lives - lives])
    if found:
        print(f"{letter} is a correct letter!")
    else:
        print(f"{letter} is not in the word.")

    print(f"Lives remaining: {lives}")
    print("".join(letters))


while "_" in letters and lives > 0:
    letterfinder()

if "_" not in letters:
    print("Congratulations, you guessed the word!")
    print(hangman_stages.win)
else:
    print("Unfortunately, you did not guess the word.")
    print(hangman_stages.try_again)
