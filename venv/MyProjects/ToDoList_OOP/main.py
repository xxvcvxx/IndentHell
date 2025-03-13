from taskManager import TaskManager
import os


def get_list_name(filename):
    if not os.path.exists(filename):
        return "empty"
    with open(filename,"r") as file:
        return file.readline().strip()


if __name__ == "__main__":
    task_lists = {'1': 'toDo1.txt', '2': 'toDo2.txt', '3': 'toDo3.txt'}

    print("Available task lists:")

    for index, (key, filename) in enumerate(task_lists.items(), start=1):
        list_name = get_list_name(filename)
        print(f"{index}. {list_name}")

    file_path = ''
    while True:
        choice = input("Select a task list (1-3): ")
        file_path = task_lists.get(choice)
        if file_path:
            break
        print("Please enter a number between 1 and 3!")

    manager = TaskManager(file_path)
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Rename the list")
        print("3. Mark task as done")
        print("4. Mark task as undone")
        print("5. Remove a task")
        print("6. Exit")
        manager.show_tasks()
        choice = input("Choose an option: ")

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.list_rename()
        elif choice == "3":
            manager.mark_task_as_done()
        elif choice == "4":
            manager.mark_task_as_undone()
        elif choice == "5":
            manager.remove_task()
        elif choice == "6":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid option, please choose again!")


