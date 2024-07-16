class Task:
    def __init__(self, title, description, due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = 'Not Complete'

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status}\nDue Date: {self.due_date}\n"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date=None):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("------ Tasks List ------")
            for task in self.tasks:
                print(task)
            print("------------------------")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].status = 'Complete'
            print(f"Task '{self.tasks[task_index].title}' marked as complete.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted.")
        else:
            print("Invalid task index.")

# Main function to run the application
def main():
    todo_list = TodoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            todo_list.add_task(title, description, due_date)

        elif choice == '2':
            todo_list.list_tasks()

        elif choice == '3':
            task_index = int(input("Enter task index to mark as complete: "))
            todo_list.complete_task(task_index)

        elif choice == '4':
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)

        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
