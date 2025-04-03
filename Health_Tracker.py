
health_tasks = []

def greet(name="Champion"):
    return f"Hello, {name}!"

print(greet())

def add_task():
    task_description = input("Enter the health-related task (e.g., 'Take medication at 8 AM'): ")
    health_tasks.append(task_description)
    print(f"Task added: {task_description}")

def view_tasks():
    print("\nYour Health Tracker Tasks:")
    if not health_tasks:
        print("No tasks added yet.")
    else:
        for index, task in enumerate(health_tasks, start=1):
            print(f"{index}. {task}")

def main():
    while True:
        print("\nHealth Tracker App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye! Stay healthy! 🌟")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
