class TaskManager:

    def __init__(self):
        self.tasks = []
        with open("toDo.txt", "r") as file:
            for line in file:
                text, done = line.strip().split(",")
                self.tasks.append({"text": text, "done": done == "True"})
        print("File has been loaded.")

    def add_task(self):
        text = input("New task: ")
        self.tasks.append({"done": False, "text": text})
        print("Task has been added.")
    def show_tasks(self):
        print("\n--- Task List ---")
        for index, task in enumerate(self.tasks, start=1):
            checkbox = "[√]" if task["done"] else "[ ]"
            print(f"{index}. {checkbox} {task['text']}")
        print("-----------------\n")