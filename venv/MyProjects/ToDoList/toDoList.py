tasks = []

def load_tasks_from_file():
    with open("toDo.txt", "r") as file:
        for line in file:
            text, done = line.strip().split(",")
            tasks.append({"text": text, "done": done == "True"})
    print("File has been loaded.")

def save_tasks_to_file():
    with open("toDo.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['text']},{task['done']}\n")
    print("File has been saved.")

def add_task():
    text = input("New task: ")
    tasks.append({"done": False, "text": text})
    print("Task has been added.")

def remove_task():
    while True:
        try:
            choice = int(input("Which task would you like to remove? "))
            if 1 <= choice <= len(tasks):
                print(f"Task '{tasks[choice - 1]['text']}' has been removed.")
                del tasks[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(tasks)}!")
        except ValueError:
            print("Error! Please enter a valid task number (a number).")

def mark_task_as_done():
    while True:
        try:
            choice = int(input("Which task would you like to mark as done? "))
            if 1 <= choice <= len(tasks):
                tasks[choice - 1]["done"] = False
                print(f"Task '{tasks[choice - 1]['text']}' marked as done!")
                break
            else:
                print(f"Please enter a number between 1 and {len(tasks)}!")
        except ValueError:
            print("Error! Please enter a valid task number (a number).")

def mark_task_as_undone():
    while True:
        try:
            choice = int(input("Which task would you like to mark as undone? "))
            if 1 <= choice <= len(tasks):
                tasks[choice - 1]["done"] = False
                print(f"Task '{tasks[choice - 1]['text']}' marked as undone!")
                break
            else:
                print(f"Please enter a number between 1 and {len(tasks)}!")
        except ValueError:
            print("Error! Please enter a valid task number (a number).")

def print_tasks():
    print("\n--- Task List ---")
    for index, task in enumerate(tasks, start=1):
        checkbox = "[√]" if task["done"] else "[ ]"
        print(f"{index}. {checkbox} {task['text']}")
    print("-----------------\n")

def main():
    load_tasks_from_file()

    while True:
        print("--- To-Do List Manager ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as done")
        print("5. Mark task as undone")
        print("6. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_as_done()
        elif choice == "5":
            mark_task_as_undone()
        elif choice == "6":
            save_tasks_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
main()