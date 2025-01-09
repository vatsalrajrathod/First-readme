class TaskManager:
    """A simple task manager to handle tasks."""

    def __init__(self):
        """Initialize the task manager with an empty task list."""
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the task list.

        Args:
            task (str): The task description.
        """
        if not task.strip():
            print("Task cannot be empty!")
        else:
            self.tasks.append(task.strip())
            print(f"Task added: {task}")

    def remove_task(self, index):
        """
        Remove a task by its index.

        Args:
            index (int): The index of the task to remove.
        """
        try:
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task}")
        except IndexError:
            print("Invalid task index!")

    def list_tasks(self):
        """List all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    """Main function to interact with the task manager."""
    manager = TaskManager()
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task description: ")
            manager.add_task(task)
        elif choice == "2":
            index = int(input("Enter the task index to remove: ")) - 1
            manager.remove_task(index)
        elif choice == "3":
            manager.list_tasks()
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
