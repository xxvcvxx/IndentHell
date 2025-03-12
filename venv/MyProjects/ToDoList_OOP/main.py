from taskManager import TaskManager

if __name__ == "__main__":
    task_lists = {'1': 'toDo1.txt', '2': 'toDo2.txt', '3': 'toDo3.txt'}

    print("Available task lists:")
    for index, (key, filename) in enumerate(task_lists.items(), start=1):
        print(f"{index}. {filename}")

    file_path = ''
    while True:
        choice = input("Select a task list (1-3): ")
        file_path = task_lists.get(choice)
        if file_path:
            break
        print("Please enter a number between 1 and 3!")

    manager = TaskManager(file_path)
    manager.show_tasks()
    manager.add_task()
    manager.show_tasks()
    manager.list_rename()
