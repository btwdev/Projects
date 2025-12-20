Tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter the Choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        Tasks.append(task)
        print("Task was added..!!")

    elif choice == "2":
        if len(Tasks) == 0:
            print("No task is present, please first enter a task")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(Tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(Tasks) == 0:
            print("No tasks to delete.")
        else:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(Tasks):
                removed = Tasks.pop(task_no - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")