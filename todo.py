def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

def todo_app():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 3.")

if __name__ == "__main__":
    todo_app()