import os
class TaskManager:

    def __init__(self,filename):
        self.filename = filename
        self.tasks = []

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                file.write("Unnamed List\n")
            print("File not found. Created a new one.")

        with open(filename, "r") as file:
            lines = file.readlines()  # Creating a list of items
            self.list_name = lines[0].strip()
            for line in lines[1:]:  # Starting from the second line
                text, done = line.strip().split(",")
                self.tasks.append({"text": text, "done": done == "True"})
        print("File has been loaded.")

    def add_task(self):
        text = input("New task: ")
        self.tasks.append({"done": False, "text": text})
        print("Task has been added.")
        self.save_tasks_to_file()

    def show_tasks(self):
        print("\n--- Task List ---")
        for index, task in enumerate(self.tasks, start=1):
            checkbox = "[√]" if task["done"] else "[ ]"
            print(f"{index}. {checkbox} {task['text']}")
        print("-----------------\n")

    def save_tasks_to_file(self):
        with open(self.filename, "w") as file:
            file.write(f"{self.list_name}\n")
            for task in self.tasks:
                file.write(f"{task['text']},{task['done']}\n")
    print("File has been saved.")

    def list_rename(self):
        self.list_name = input("Enter new list name: ")

        with open(self.filename, 'w') as file:
            file.write(f"{self.list_name}\n")

            for task in self.tasks:
                file.write(f"{task['text']},{task['done']}\n")

    def remove_task(self):
        if not self.tasks:
            print("The task list is empty!")
            return

        while True:
            try:
                choice = int(input("Which task would you like to remove? "))
                if 1 <= choice <= len(self.tasks):
                    print(f"Task '{self.tasks[choice - 1]['text']}' has been removed.")
                    del self.tasks[choice - 1]
                    self.save_tasks_to_file()
                    break
                else:
                    print(f"Please enter a number between 1 and {len(self.tasks)}!")
            except ValueError:
                print("Error! Please enter a valid task number (a number).")

    def mark_task_as_done(self):
        if not self.tasks:
            print("The task list is empty!")
            return
        while True:
            try:
                choice = int(input("Which task would you like to mark as done? "))
                if 1 <= choice <= len(self.tasks):
                    self.tasks[choice - 1]["done"] = True
                    print(f"Task '{self.tasks[choice - 1]['text']}' marked as done!")
                    self.save_tasks_to_file()
                    break
                else:
                    print(f"Please enter a number between 1 and {len(self.tasks)}!")
            except ValueError:
                print("Error! Please enter a valid task number (a number).")

    def mark_task_as_undone(self):
        if not self.tasks:
            print("The task list is empty!")
            return
        while True:
            try:
                choice = int(input("Which task would you like to mark as undone? "))
                if 1 <= choice <= len(self.tasks):
                    self.tasks[choice - 1]["done"] = False
                    print(f"Task '{self.tasks[choice - 1]['text']}' marked as undone!")
                    self.save_tasks_to_file()
                    break
                else:
                    print(f"Please enter a number between 1 and {len(self.tasks)}!")
            except ValueError:
                print("Error! Please enter a valid task number (a number).")
