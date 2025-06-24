# To-Do List Application

todo_list = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for index, task in enumerate(todo_list, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{index}. [{status}] {task['title']}")

def add_task():
    title = input("Enter the task title: ")
    todo_list.append({"title": title, "completed": False})
    print("Task added successfully.")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 0 < task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(todo_list):
            deleted = todo_list.pop(task_num - 1)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
