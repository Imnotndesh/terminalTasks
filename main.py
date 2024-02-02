class Task:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(Task(task_name))

    def mark_task_done(self, task_name, filename):
        for task in self.tasks:
            if task.name == task_name:
                task.done = True
                self.save_tasks(filename)
                return True
        return False

    def display_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            status = "Done" if task.done else "Not Done"
            print(f"{i}. {task.name} - {status}")

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                if not task.done:
                    f.write(f"{task.name},{task.done}\n")

    def load_tasks(self, filename):
        self.tasks = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    name, done = line.strip().split(',')
                    done = done == 'True'  # Convert string to boolean
                    self.tasks.append(Task(name, done))
        except FileNotFoundError:
            print("No tasks file found. Starting with an empty task list.")

def main():
    task_list = TaskList()
    tasks_file = "tasks.txt"
    task_list.load_tasks(tasks_file)

    while True:
        print(" ")
        print("1. Add Task\n2. Mark Task as Done\n3. Display Tasks\n4. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("\nEnter task name: ")
            task_list.add_task(task_name)
            print(f"> Task : '{task_name}' added successfully!")
        elif choice == "2":
            task_name = input("\nEnter task name to mark as done (will also remove from list): ")
            if task_list.mark_task_done(task_name, tasks_file):
                print(f"> Task: '{task_name}' marked as done")
                print("-----Remaining tasks------")
                print(" ")
                task_list.save_tasks(tasks_file)
                task_list.display_tasks()
                print("--------------------------")
            else:
                print("\nTask not found.")
        elif choice == "3":
            print("-----Current saved tasks------")
            print(" ")
            task_list.display_tasks()
            print("------------------------------")
        elif choice == "4":
            task_list.save_tasks(tasks_file)
            print("\nTasks saved. Exiting program.")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    print("Welcome to terminal tasks: A Python task manager.")
    main()

