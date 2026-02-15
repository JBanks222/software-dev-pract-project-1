import os

class TaskManager:
    def __init__(self):
        self.task_file = os.path.join(os.path.dirname(__file__), 'tasks.txt')
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.task_file, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.task_file, 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"Task {index}: {task}")

    # Student B deliberate bug (Task 5 Step 1)
    def delete_task(self, index):
        if self.tasks:
            self.tasks.pop(0)  # BUG: always deletes the first task
            self.save_tasks()
            print("⚠ Bug introduced: Deleted first task instead of selected one")
        else:
            print("No tasks to delete.")
