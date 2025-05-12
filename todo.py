#todo.py

TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    try:
        with open(TASKS_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def show_menu():
    print("\n===Todo List===")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"    {idx}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print (f"Task '{task}' added.")
    else:
        print("No task added. Nothing to do.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed}' removed.")
    except (ValueError, IndexError):
        print("Invalid task number. No task removed.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()