import os.path


class Flash_cards:
        def __init__(self,filename):
            self.filename=filename
            self.flashcards=[]

            if not os.path.exists(self.filename):
                with open(filename ,'w') as file:
                    file.write("New FlashCard")
                print("File not found. Created a new one.")

            with open(filename,'r') as file:
                lines = file.readlines()
                self.flashcards_name=lines[0].strip()
                for line in lines[1:]:
                    word, translation = line.strip().split(",")
                    self.flashcards.append({"word": word, "translation": translation})
                print("File has been loaded.")

        def __str__(self):
            return '\n'.join([f"{card['word']},{card['translation']}" for card in self.flashcards])