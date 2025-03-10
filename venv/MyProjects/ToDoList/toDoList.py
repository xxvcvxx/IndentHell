tasks = [{"done": False, "text": "task1"}, {"done": False, "text": "task2"}]

def add_task():
    text = input("New task: ")
    tasks.append({"done": False, "text": text})

def remove_task():
    while True:
        try:
            choice = int(input("Which task would you like to remove? "))

            if 1 <= choice <= len(tasks):
                print(f"Task {tasks[choice - 1]['text']} has been removed.")
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
                tasks[choice - 1]["done"] = True
                print(f"Task {tasks[choice - 1]['text']} marked as done!")
                break
            else:
                print(f"Please enter a number between 1 and {len(tasks)}!")
        except ValueError:
            print("Error! Please enter a valid task number (a number).")

def print_tasks():
    for index, task in enumerate(tasks, start=1):
        checkbox = "[√]" if task["done"] else "[ ]"
        print(f"{index}. {checkbox} {task['text']}")

add_task()
remove_task()
mark_task_as_done()
print_tasks()
