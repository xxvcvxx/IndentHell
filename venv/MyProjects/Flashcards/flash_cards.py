import os.path


class Flash_cards:
    def __init__(self, filename):
        self.filename = filename
        self.flashcards = []

        if not os.path.exists(self.filename):
            with open(filename, 'w') as file:
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

    def start_test(self):
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
