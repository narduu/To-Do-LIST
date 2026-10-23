def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def todo_app():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nTasks:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
        elif choice == '2':
            new_task = input("Enter the task: ")
            if new_task.strip():
                tasks.append(new_task)
                print(f"Added: '{new_task}'")
            else:
                print("Task cannot be empty.")
        elif choice == '3':
            if not tasks:
                print("No tasks to delete.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Removed: '{removed}'")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                print("Goodbye! Have a productive day!")  # Updated exit message
                break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    todo_app()