import os.path
import difflib

class Flash_cards:
    def __init__(self, filename):
        self.filename = filename
        self.flashcards = []

        if not os.path.exists(self.filename):
            with open(filename, 'w') as file: # To do Check for empty lines or lines without a comma (e.g. spaces, incomplete lines)
                file.write("New FlashCard")
            print("File not found. Created a new one.")

        with open(filename, 'r') as file:
            lines = file.readlines()
            self.flashcards_name = lines[0].strip()
            for line in lines[1:]:
                word, translation = line.strip().split(",")
                self.flashcards.append({"word": word, "translation": translation})
            print("File has been loaded.")

    def __str__(self):
        return '\n'.join([f"{card['word']},{card['translation']}" for card in self.flashcards])

    def has_flashcards(self):
        if len(self.flashcards) == 0:
            print("No flashcards available.")
            return False
        return True

    def show_all_flashcards(self):
        for card in self.flashcards:
            print(f"Word: {card['word']}, Translation: {card['translation']}")

    def generate_exercises(self, repetitions):

        pass

    def convert_points_to_grade(self, points, max_points):
        percent = points / max_points
        if percent >= 0.8:
            return '5'
        elif percent >= 0.6:
            return '4'
        elif percent >= 0.5:
            return '3'
        elif percent >= 0.3:
            return '2'
        else:
            return 'Fail'

    def similarity(self,answer,user_answer):
        ratio = difflib.SequenceMatcher(None, user_answer, answer).ratio()
        return ratio >=0.9

    def start_test(self):
        if not self.has_flashcards():
            return
        points = 0
        max_points = len(self.flashcards)
        for card in self.flashcards:
            print(f"Please translate the following word: {card['word']}")
            answer = input("Your translation: ")
            if answer.strip().lower() == card['translation'].strip().lower():
                print("Correct answer!")
                points += 1
            else:
                print(f"Incorrect answer. The correct translation is: {card['translation']}")
        print(f"Total points: {points} out of {max_points}")
        print(f"Final grade: {self.convert_points_to_grade(points, max_points)}")


    def multiple_choice(self):
        pass

    def save_to_file(self):
        with open(self.filename, "w") as file:
            file.write(f"{self.flashcards_name}\n")
            for card in self.flashcards:
                file.write(f"{card['word']},{card['translation']}\n")


    def addFlashcard(self):
        word_input = input("Enter a new English word: ").strip()
        translation_input = input("Enter its translation: ").strip()
        self.flashcards.append({
            "word": word_input,
            "translation": translation_input
        })

        with open(self.filename, "a") as file:
            last_flashcard = self.flashcards[-1]
            file.write(f"{last_flashcard['word']},{last_flashcard['translation']}\n")

        print(f"Flashcard added: '{word_input}' → '{translation_input}'")


    def removeFlashcard(self):
        if not self.has_flashcards():
            return

        word_input = input("Enter the word to delete: ")

        for card in self.flashcards:
            if word_input == card['word']:
                self.flashcards.remove(card)
                print(f"Flashcard removed: '{word_input}'")
            else:
                print(f"Flashcard with word '{word_input}' not found.")
        self.save_to_file()

    def editFlashcard(self):
        if not self.has_flashcards():
            return
        self.show_all_flashcards()
        word_input = input("Enter the word to edit: ")

        for card in self.flashcards:
            if word_input == card['word']:
                choice = input("What would you like to edit? (w/t): ")
                if choice == 'w':
                    new_word = input("Enter the new word: ")
                    card['word'] = new_word
                    print(f"Flashcard updated: '{new_word}'")
                    self.save_to_file()
                elif choice == 't':
                    new_translation = input("Enter the new translation: ")
                    card['translation'] = new_translation
                    print(f"Flashcard updated: '{new_translation}'")
                    self.save_to_file()
                else:
                    print("Invalid choice. Exiting edit mode.")
                    return
            else:
                print(f"Flashcard with word '{word_input}' not found.")








