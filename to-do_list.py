tasks = []

def add_task(task):
    tasks.append(task)
    print(f"✅ Task added: {task}")

def view_tasks():
    if not tasks:
        print("📝 No tasks in the list.")
    else:
        print("📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"❌ Task removed: {removed}")
    else:
        print("⚠ Invalid task number!")

def clear_tasks():
    tasks.clear()
    print("🚮 All tasks cleared!")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        except ValueError:
            print("⚠ Enter a valid number!")
    elif choice == "4":
        clear_tasks()
    elif choice == "5":
        print("👋 Exiting... Have a productive day!")
        break
    else:
        print("❗ Invalid choice. Please select 1–5.")