tasks = []
def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        n = int(input("Enter task number to delete: "))
        if 0 < n <= len(tasks):
            tasks.pop(n-1)
            print("Task deleted")
        else:
            print("Invalid number")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
