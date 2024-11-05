""" A class to manage the to-do list. """
class ToDolist:
    def __init__(self):
        # Initialize the to-do list.
        self.tasks = []

    def add_task(self, task):
        # Add a new task to the to-do list.
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' has been added to the list.")

    def remove_task(self, task_index):
        # Remove a task by its index from the to-do list.
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task'{removed_task['task']}' has been removed.")
        else:
            print("Invalid task number. Please try again.")

    def mark_completed(self, task_index):
        # Mark a task as completed by its index.
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Task '{self.tasks[task_index]['task']}' has been marked as completed.")
        else:
            print("Invalid task number. Please try again.")

    def view_tasks(self):
        # View all tasks in the to-do list.
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List: ")

            for index, task in enumerate(self.tasks, start=1):
                status = "completed" if task["completed"] else "pending" 
                print(f"{index}.{task['task']} - {status}")

        print("\n")

def main():
    todo_list = ToDolist()

    while True:
        print("To-Do list Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == '2':
            try:
                task_number = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.mark_completed(task_number)
            except ValueError:
                 print("Invalid input. Please enter a valid task number.")

        elif choice == '3':
            try:
                 task_number = int(input("Enter the task number to mark as completed: ")) - 1
                 todo_list.mark_completed(task_number)
            except ValueError:
                  print("Invalid input. Please enter a valid task number.")

        elif choice == '4':
            todo_list.view_tasks()

        elif choice == '5':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        
        else:
           print("Invalid choice. Please select a valid option.")
        

if __name__ == "__main__":
    main()                                                                                             