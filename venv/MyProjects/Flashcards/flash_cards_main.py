from flash_cards import Flash_cards


filename = "flash_cards1.txt"
flashcards = Flash_cards(filename)

while True:
    print("\nWelcome to the Flashcard App!")
    print("1. Show all flashcards")
    print("2. Add a new flashcard")
    print("3. Remove a flashcard")
    print("4. Edit a flashcard")
    print("5. Start a test")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        flashcards.show_all_flashcards()

    elif choice == '2':
        flashcards.addFlashcard()

    elif choice == '3':
        flashcards.removeFlashcard()

    elif choice == '4':
        flashcards.editFlashcard()

    elif choice == '5':
        flashcards.start_test()

    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")